import vk_api
from vk_api.vk_api import VkApiMethod

from vk.session.access import TOKEN


class VkAPI:
    _vk = vk_api.VkApi(token=TOKEN)

    @classmethod
    def get_vk_api(cls) -> VkApiMethod:
        return cls._vk.get_api()
