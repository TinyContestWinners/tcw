import os
import pytest
from tcw import create_app
from tcw.utils import expires_time
from tcw.config import Development


@pytest.fixture()
def app():
    config = Development
    config.SQLALCHEMY_DATABASE_URI = 'sqlite://'
    app = create_app('test_app', config)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_contest(client):
    response = client.post("/contest", data={
        "name": "test",
        "title": "test contest",
        "max_entrants": 10,
        "winners": 2,
        "expires": expires_time(),
    })
    assert response.status_code == 200


def test_add_entrant(client):
    response = client.post("/signup?name=test", data={
        "name": "contestant #1",
    })
    assert response.status_code == 200
