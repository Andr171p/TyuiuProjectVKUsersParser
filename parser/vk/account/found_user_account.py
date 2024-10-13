from parser.vk.auth.session import VkSession
from parser.vk.schemas.find_user_schema import VkUserSchema
from parser.vk.account.user_account import VkUserAccountData

from loguru import logger

from typing import Type


class VkFoundUserAccount(VkUserAccountData):
    def __init__(self, user: dict, vk: VkSession.session) -> None:
        super().__init__(user, vk)

        self.user_id = self.get_id()
        self.name = self.get_name()
        self.surname = self.get_surname()
        self.age = self.get_age()
        self.city = self.get_city()
        self.posts = self.get_posts()
        self.groups = self.get_groups()
        self.subscriptions = self.get_subscriptions()

    def found_user(self) -> VkUserSchema:
        user = VkUserSchema
        user.add(
            user_id=self.user_id,
            name=self.name,
            surname=self.surname,
            age=self.age,
            city=self.city,
            posts=self.posts,
            groups=self.groups,
            subscriptions=self.subscriptions
        )
        logger.info(user)
        return user
