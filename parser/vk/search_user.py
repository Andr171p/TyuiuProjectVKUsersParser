from parser.vk.auth.session import VkSession
from parser.vk.schemas.primary_schema import VkPrimaryUserSchema

from loguru import logger


class VkSearchUsers:
    vk_session = VkSession
    vk = vk_session.session()

    def __init__(self, user: VkPrimaryUserSchema) -> None:
        self.user = user

    def search_user(self) -> dict:
        users = self.vk.users.search(
            q=f"{self.user.name} {self.user.surname}",
            count=1000
        )
        logger.info(f"VK find {users['count']} count of users...")
        return users
