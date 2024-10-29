from vk_api.vk_api import VkApiMethod

from vk.manager.auth import Auth


class VkSession(Auth):
    vk_session: VkApiMethod = None

    def get_vk_session(self) -> VkApiMethod:
        vk_auth = self.auth()
        self.vk_session = vk_auth.get_api()
        return self.vk_session
