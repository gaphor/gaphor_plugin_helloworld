import pytest
from gaphor.application import Application


@pytest.fixture
def application():
    app = Application()
    yield app
    app.shutdown()


@pytest.fixture
def session(application):
    return application.new_session()


@pytest.fixture
def hello_world(session):
    return session.get_service("hello_world")


def test_hello_world_action(hello_world):
    hello_world.helloworld_action()