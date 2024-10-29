from vk_api.vk_api import VkApiMethod

from vk.manager.session import VkSession
from vk.schemas.user import UserSchema


class UsersService:
    _fields = 'sex, bdate, city, country, photo_max_orig, subscriptions'
    _v = '5.131'

    def __init__(self, vk_session: VkApiMethod) -> None:
        self._vk = vk_session

    def user(self, user_id: int) -> UserSchema:
        user = self._vk.users.get(
            user_ids=user_id,
            fields=self._fields,
            v=self._v
        )
        return user