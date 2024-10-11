from parser.vk.auth.session import VkSession
from parser.vk.search_user import VkSearchUsers
from parser.vk.schemas.user_schema import VkUserSchema


class VkUserParser(VkSearchUsers):

    def get_candidate(self) -> VkUserSchema:
        ...