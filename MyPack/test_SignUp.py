import pytest


@pytest.yield_fixture()
def setUp():
    print("\nOpen url to login")
    yield
    print("\nCloseing browser after login")


def test_signUpByEmail(setUp):
    print("Signuo by email")


def test_signUpByFacebook(setUp):
    print("Signup by facebook")
