from flask import Flask, request, jsonify
from functools import reduce
from utils.strategies import strategies
from utils.api_errors import APIBadRequestError, APIError, APIConnectException
from services.call_api import callApi
from utils.utils import checkKey, getMemberId
import config

app = Flask(__name__)
app.config["DEBUG"] = config.dev


def applyStrategy(strategy):
    member_id = getMemberId()
    # We call each API and find all keys
    allApiData = [callApi(apiUrl, member_id) for apiUrl in config.apisToCall]
    allProperties = set([key for elem in allApiData for key in elem])
    if len(allProperties) == 0:
        raise APIBadRequestError('No properties in API responses')
    if not config.errorOnInvalidStrategy and strategy not in strategies:
        # We apply the default strategy as we don't want to invalidate the request
        strategy = config.defaultStrategy
    if strategy not in strategies:
        raise APIBadRequestError(f'Strategy not found: {strategy}')
    try:
        # We transform the data to an object applying the strategy to each array of values per key
        transformedObject = {checkKey(key): strategies[strategy](
            [float(elem[key]) for elem in allApiData if key in elem]) for key in allProperties}
    except Exception as e:
        # There was some issue with the data returned from the APIs
        raise APIBadRequestError(
            f'Invalid values found in API response. Error: {str(e)}')
    return transformedObject


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'success': True,
        'message': 'Server online'
    })


@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        'success': True,
        'message': 'API working'
    })


@app.route('/api/<version>', methods=['GET'])
def index(version):
    if version != f'v{config.version}':
        raise APIBadRequestError('Invalid API version')
    transformedObject = applyStrategy(
        request.args.get('strategy') or config.defaultStrategy)
    return jsonify(transformedObject)


@app.route('/api/<version>/<strategy>', methods=['GET'])
def byStrategy(version, strategy):
    if version != f'v{config.version}':
        raise APIBadRequestError('Invalid API version')
    transformedObject = applyStrategy(strategy)
    return jsonify(transformedObject)


@app.errorhandler(APIBadRequestError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # TODO: Add some logging so that we can monitor different types of errors
    return jsonify(response), err.code


@app.errorhandler(APIConnectException)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description,
                "url": err.args[0], "message": err.args[1]}
    # TODO: Add some logging so that we can monitor different types of errors
    return jsonify(response), err.code


@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    # TODO: Add some logging so that we can monitor different types of errors
    response = {
        "error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
    return jsonify(response), 500


if __name__ == '__main__':
    app.run(port=config.port)
