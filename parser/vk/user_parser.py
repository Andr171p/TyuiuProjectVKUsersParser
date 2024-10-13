from parser.vk.auth.session import VkSession
from parser.vk.search_users import VkSearchUsers
from parser.vk.account.found_user_account import VkFoundUserAccount
from parser.vk.schemas.find_user_schema import VkUserSchema
from parser.vk.schemas.primary_user_schema import VkPrimaryUserSchema

from typing import Type


class VkUserParser:
    session = VkSession
    vk = session.session()

    def __init__(self, user: VkPrimaryUserSchema):
        self.user = user

    def get_users(self) -> list[Type[VkUserSchema]]:
        data = []
        searcher = VkSearchUsers(
            user=self.user,
            vk=self.vk
        )
        users = searcher.search_users()
        for user in users['items']:
            account = VkFoundUserAccount(
                user=user,
                vk=self.vk
            ).found_user()
            data.append(account)
        self.session.stop()
        return data


user = VkPrimaryUserSchema(name="Андрей", surname="Косов", age=18, city="Тюмень")
parser = VkUserParser(user=user)
u = parser.get_users()
print(u)