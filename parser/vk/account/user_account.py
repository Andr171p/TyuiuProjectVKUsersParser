from parser.vk.auth.session import VkSession

from loguru import logger


class VkUserAccountData:
    from datetime import datetime
    year = datetime.now().year

    def __init__(self, user: dict, vk: VkSession.session) -> None:
        self.user = user
        self.vk = vk

    def get_id(self) -> int:
        user_id = self.user['id']
        return user_id

    def get_name(self) -> str:
        name = self.user['first_name']
        return name

    def get_surname(self) -> str:
        surname = self.user['last_name']
        return surname

    def get_age(self) -> int | None:
        if 'bdate' in self.user:
            bdate: str = self.user['bdate']
            age = self.year - int(bdate.split('.')[2])
            return age

    def get_city(self) -> str | None:
        if 'city' in self.user:
            city = self.user['city']['title']
            return city

    def get_posts(self) -> dict | None:
        user_id = self.get_id()
        try:
            posts = self.vk.wall.get(
                owner_id=user_id,
                count=5
            )
            logger.info(posts)
            return posts
        except Exception as _ex:
            logger.warning(_ex)

    def get_groups(self) -> dict | None:
        user_id = self.get_id()
        try:
            groups = self.vk.groups.get(
                user_id=user_id,
                extended=1
            )
            logger.info(groups)
            return groups
        except Exception as _ex:
            logger.warning(_ex)

    def get_subscriptions(self) -> dict | None:
        user_id = self.get_id()
        try:
            subscriptions = self.vk.users.getSubscriptions(user_id=user_id)
            logger.info(subscriptions)
            return subscriptions
        except Exception as _ex:
            logger.warning(_ex)
