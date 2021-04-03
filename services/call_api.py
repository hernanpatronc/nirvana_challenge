from utils.api_errors import APIConnectException
import requests
import random

""" This service calls the APIs using the requests module"""


def callApi(url, member_id):
    try:
        result = requests.get(f'{url}?member_id={member_id}', timeout=5)
        return result.json()
    except Exception as e:
        raise APIConnectException(f'{url}?member_id={member_id}', str(e))
