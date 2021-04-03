from utils.api_errors import APIConnectException
import requests
import random
import config

""" This service calls the APIs using the requests module"""


def callApi(url, member_id):
    if not config.useMock:
        return {'deductible': random.randrange(900, 1300, 10), 'stop_loss': random.randrange(
            10000, 20000, 100), 'oop_max': random.randrange(4000, 8000, 100)}
    try:
        result = requests.get(f'{url}?member_id={member_id}', timeout=5)
        return result.json()
    except Exception as e:
        raise APIConnectException(f'{url}?member_id={member_id}', str(e))
