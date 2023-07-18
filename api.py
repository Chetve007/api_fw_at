import allure
import requests
from assertpy import assert_that
from jsonschema import validate

from helper.load import load_json_schema
from helper.logger import log
from helper.parser import get_data


class Api:
    """The very main class for work with API"""

    _HEADERS = {'Content-Type': 'application/json; charset=utf-8'}
    _TIMEOUT = 10
    base_url = {}

    def __init__(self):
        self.response = None

    @allure.step("Send GET-request")
    def get(self, url: str, urn: str):  # todo add params and headers, maybe **kwargs
        with allure.step(f'GET-request to URI: {url}{urn}'):
            self.response = requests.get(url=f'{url}{urn}', headers=self._HEADERS, timeout=self._TIMEOUT)
        log(response=self.response)
        return self

    @allure.step("Send POST-request")
    def post(self, url: str, urn: str, params: dict = None, payload: dict = None):  # fix headers, not only json
        with allure.step(f'POST-request to URI: {url}{urn}\n payload: \n {payload}'):
            self.response = requests.post(url=f'{url}{urn}', headers=self._HEADERS, params=params, json=payload,
                                          timeout=self._TIMEOUT)
        log(self.response, payload)
        return self

    @allure.step("Response status code equal {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Check response status code - 'actual_code' == 'expected_code'"""
        act_code = self.response.status_code
        assert_that(expected_code, f'\nExpected: {expected_code}\n but was: {act_code}\n').is_equal_to(act_code)
        return self

    @allure.step("Expected: Response json-schema is valid")
    def json_schema_should_be_valid(self, path_json_scheme: str, name_json_schema: str = 'schema'):
        json_schema = load_json_schema(path_json_scheme, name_json_schema)
        validate(self.response.json(), json_schema)
        return self

    @allure.step("Expected: Objects are equal")
    def objects_should_be(self, exp_obj, act_obj):
        """Comparing two objects"""
        assert_that(exp_obj, f'\nExpected: {exp_obj}\n but was: {act_obj}\n').is_equal_to(act_obj)
        return self

    @allure.step("Expected: Response contains value")
    def have_value_in_response_parameter(self, keys: list, value: str):
        """Comparing param value"""
        payload = self.get_payload(keys)
        assert_that(value, f'\nExpected: {value}\n but was: {payload}\n').is_equal_to(payload)
        return self

    def get_payload(self, keys: list):
        """Get payload by keys"""
        response = self.response.json()
        payload = get_data(keys, response)
        return payload
