from config import validKeys, validateKeys
from flask import request
from utils.api_errors import APIBadRequestError
import config


def checkKey(key):
    if not validateKeys or key in validKeys:
        return key
    else:
        raise Exception(f'Invalid Key: {key}')


def getMemberId():
    member_id = request.args.get('member_id')
    if not member_id and config.errorOnNoMemberId:
        raise APIBadRequestError('No member_id provided')
    return member_id or config.defaultMemberId
