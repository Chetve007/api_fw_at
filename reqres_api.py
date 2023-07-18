import allure

from api import Api
from model.create_user_model import RequestCreateUserModel
from model.single_user_model import ResponseSingleUserModel


class ReqResApi(Api):

    _URL = 'https://reqres.in'  # todo move this static to config file
    _URN = '/api/users/'

    @allure.step("Send to 'create'")
    def reqres_create(self, param_request_body: RequestCreateUserModel):
        return self.post(url=self._URL, urn=self._URN, payload=param_request_body.to_dict())

    def deserialize_single_user(self):
        payload = self.get_payload([])
        return ResponseSingleUserModel(
            id_=payload['data']['id'],
            email=payload['data']['email'],
            first_name=payload['data']['first_name'],
            last_name=payload['data']['last_name'],
            avatar=payload['data']['avatar'],
            url=payload['support']['url'],
            text=payload['support']['text']
        )

    @allure.step("Send to 'single user'")
    def reqres_single_user(self, user_id: int):
        return self.get(url=self._URL, urn=f'{self._URN}{user_id}')
