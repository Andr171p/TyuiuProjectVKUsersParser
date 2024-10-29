from vk_api import VkApi


class Auth:
    def __init__(self, token: str) -> None:
        self._token = token

    def auth(self) -> VkApi:
        vk_auth = VkApi(token=self._token)
        return vk_auth
