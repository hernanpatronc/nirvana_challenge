from flask import Flask, request, jsonify
import random
import time
"""
Mock API for testing possible errors with API responses
"""
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/<api>', methods=['GET'])
def index(api):
    result = {'deductible': random.randrange(900, 1300, 10), 'stop_loss': random.randrange(
        10000, 20000, 100), 'oop_max': random.randrange(4000, 8000, 100)}
    rand = random.randint(0, 10)
    """
    Uncomment below if want to check for APIs returning data with errors
    """
    # if rand == 1:
    #     del result[random.choice(list(result.keys()))]
    # elif rand == 2:
    #     result['test'] = 1
    # elif rand == 3:
    #     result[random.choice(list(result.keys()))] = 'test'
    # elif rand == 4:
    #     return 'Error in api', 500
    # elif rand == 5:
    #     return 'Error in request', 400
    # elif random.randint(0, 100) <= 5:
    #     time.sleep(60)
    #     return 'Error in api', 500
    return result


app.run(port=3001)
