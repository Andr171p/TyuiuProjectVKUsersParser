from parser.vk.auth.session import VkSession
from parser.vk.schemas.primary_user_schema import VkPrimaryUserSchema

from loguru import logger


class VkSearchUsers:

    def __init__(self, user: VkPrimaryUserSchema, vk: VkSession.session) -> None:
        self.user = user
        self.vk = vk

    def search_users(self) -> dict:
        users = self.vk.users.search(
            q=f"{self.user.name} {self.user.surname}",
            count=5
        )
        logger.info(f"VK find {users['count']} count of users...")
        return users
