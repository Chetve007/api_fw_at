import pytest

from reqres_api import ReqResApi


@pytest.fixture
def reqres_api_fixture() -> ReqResApi:
    """Connect to ReqRes API"""
    return ReqResApi()
