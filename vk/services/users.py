from vk.session.api import VkAPI


class VkUser(VkAPI):
    _fields = 'sex, bdate, city, country'
    _v = '5.131'

    def __init__(self, user_id: int) -> None:
        self._user_id = user_id
        self._api = self.get_vk_api()

    def get(self) -> dict:
        data = self._api.users.get(
            user_ids=self._user_id,
            fields=self._fields,
            v=self._v
        )
        return data[-1]

    def get_groups(self) -> list[int]:
        groups = self._api.groups.get(user_id=self._user_id)
        return groups['items']

    def get_subscriptions(self) -> list[int]:
        subscriptions = self._api.users.getSubscriptions(user_id=self._user_id)
        return subscriptions['users']['groups']['items']