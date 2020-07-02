import pytest
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@pytest.yield_fixture()
def setUp():
    print("\nOpen url to login")
    yield
    print("\nCloseing browser after login")


def test_loginByEmail(setUp):
    logger.info('Login by email')
    print("Login by email")


def test_loginByFacebook(setUp):
    logger.info('Login by facebook')
    print("Login by facebook")


'''
pytest -v -s --html=report.html --self-contained-html 
'''
