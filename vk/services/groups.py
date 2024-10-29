from vk.manager.session import VkSession
from vk.schemas.user import UserSchema

from typing import List
from loguru import logger


def get_users_data(users: List[dict]) -> List[UserSchema]:
    data = []
    for user in users:
        id = user['id']
        first_name = user['first_name']
        last_name = user['last_name']
        try:
            bdate = user['bdate']
        except Exception as _ex:
            bdate = "нет"
            logger.warning(_ex)
        sex = user['sex']
        try:
            country = user['country']['title']
        except Exception as _ex:
            country = "нет"
            logger.warning(_ex)
            logger.info("User not has country")
        try:
            city = user['city']['title']
        except Exception as _ex:
            city = "нет"
            logger.warning(_ex)
            logger.info("User not has city")
        photo = user['photo_max_orig']
        schema = UserSchema(user_id=id, first_name=first_name, last_name=last_name, bdate=bdate, sex=sex, country=country, city=city, photo=photo)
        data.append(schema)
    return data


class GroupsService(VkSession):
    _fields = 'sex, bdate, city, country, city, photo_max_orig, subscriptions'

    def __init__(self, token: str) -> None:
        super().__init__(token)
        self._vk = self.get_vk_session()

    def members(self, group_id: int) -> List[UserSchema]:
        response = self._vk.groups.getMembers(
            group_id=group_id,
            fields=self._fields
        )
        logger.info(f"Group Id: {group_id}, count of users: {response['count']}")
        users = get_users_data(users=response['items'])
        return users


from vk.configuration.access import TOKEN
_id = 148637225
# print(GroupsService(token=TOKEN).members(group_id=222477990))
d = GroupsService(token=TOKEN).members(group_id=_id)
from data_service.table.create import UsersTable

table = UsersTable(users=d)
df = table.create()
table.save()
