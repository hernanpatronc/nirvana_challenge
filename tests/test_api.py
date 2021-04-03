import pytest
import json
from api import app as flask_app
import config
from utils.strategies import strategies


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_api_version(app, client):
    """ Test API versioning works """
    for i in range(1, 5):
        res = client.get(f'/api/v{i}')
        assert res.status_code == 400 if i != config.version else res.status_code == 200


def test_no_member(app, client):
    """ Test API returns an error when no member_id is present and errorOnNoMemberId is True """
    config.errorOnNoMemberId = False
    res = client.get(f'/api/v1')
    assert res.status_code == 200
    config.errorOnNoMemberId = True
    res = client.get(f'/api/v1')
    assert res.status_code == 400
    res = client.get(f'/api/v1?member_id=1')
    assert res.status_code == 200
    config.errorOnNoMemberId = False


def test_strategies(app, client):
    """ Test All strategies """
    for strategy in strategies:
        res = client.get(f'/api/v1/{strategy}')
        assert res.status_code == 200


def test_strategies_invalid(app, client):
    """ Test Invalid strategies """
    config.errorOnInvalidStrategy = False
    res = client.get(f'/api/v1/unreal_strategy')
    assert res.status_code == 200
    config.errorOnInvalidStrategy = True
    res = client.get(f'/api/v1/unreal_strategy')
    assert res.status_code == 400


# TODO: implement testing for each strategy to check if they give correct results

# TODO: implement testing for APIs errors (similar to uncommenting the errors on mock_api.py)
