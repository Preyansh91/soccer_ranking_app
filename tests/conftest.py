import pytest
import logging


@pytest.fixture(scope='session', autouse=True)
def start_tests():
    print("Starting tests")
    yield
    print("\nTests completed")

