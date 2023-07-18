import allure
import pytest

from helper.load import load_data


pytestmark = [allure.parent_suite('reqres'), allure.suite('single_user')]


@allure.title("Request to get user data with valid data")
@pytest.mark.parametrize(('user_id', 'exp_data'), load_data('single_user_data'))
def test_single_user_valid_parameters(reqres_api_fixture, user_id, exp_data):
    (reqres_api_fixture.reqres_single_user(user_id).status_code_should_be(200)
        .json_schema_should_be_valid('single_user_schema')
        .objects_should_be(exp_data, reqres_api_fixture.deserialize_single_user()))


@allure.title("Request to get user data with invalid data")
@pytest.mark.parametrize(('user_id', 'exp_data'), load_data('single_user_data', 'not_valid_data'))
def test_single_user_invalid_parameters(reqres_api_fixture, user_id, exp_data):
    (reqres_api_fixture.reqres_single_user(user_id)
        .status_code_should_be(404)
        .have_value_in_response_parameter([], exp_data))
