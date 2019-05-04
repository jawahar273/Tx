from pytest import fixture
import logging

from Tx import app


@fixture
def sanic_app(request):
    return app


@fixture
def sanic_tester(loop, sanic_app, test_client):
    return loop.run_until_complete(test_client(sanic_app))


@fixture
def logger():
    logger = logging.getLogger(__name__)
    numeric_level = getattr(logging, "DEBUG", None)
    logger.setLevel(numeric_level)
    return logger
