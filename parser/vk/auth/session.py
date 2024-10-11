import vk_api
from vk_api import VkApi

from parser.vk.auth.token import VkAuthToken

from loguru import logger


class VkSession:
    vk_session = None

    @classmethod
    def start(cls) -> VkApi:
        cls.vk_session = vk_api.VkApi(token=VkAuthToken.TOKEN)
        logger.info("VK session is started...")
        return cls.vk_session

    @classmethod
    def stop(cls) -> None:
        cls.vk_session = None
        logger.info("VK session is closed...")

    @classmethod
    def session(cls) -> VkApi.get_api:
        if cls.vk_session is None:
            vk_session = cls.start()
            api = vk_session.get_api()
            logger.info("VK API session get successfully...")
            return api
