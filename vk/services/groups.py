from vk.session.api import VkAPI


class VkGroup(VkAPI):
    def __init__(self, group_id: int) -> None:
        self._group_id = group_id

    def get_members(self) -> list[int]:
        api = self.get_vk_api()
        members: dict = api.groups.getMembers(group_id=self._group_id)
        return members['item']


print(VkGroup(group_id=222477990).get_members())