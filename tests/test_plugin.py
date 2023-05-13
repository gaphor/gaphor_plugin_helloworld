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


def test_hello_world(session):
    hello_world = session.get_service("hello_world")

    assert hello_world