import vk_api


token = "vk1.a.latexwkIbUgxzU-O4Xoe1hHWYmaZnoqdFzyIhP2ZH9FwcZTWEOrCWtZJQy81Q54KvjC9BSLV4Rlhl0xadQ52PB0E2YFO-YWM6DtS404G0oriMmUEmk_03TJgR0sEOM90wfcCT8eM2X3mAK83dJlVJp2IkmDtwB95sHjkop47nG_ggLwFIeBm06cryLoMaJR3w9y8QbTjjRNtlH-LXZDvXQ"


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
response = vk.groups.getMembers(group_id=222477990)
print(response)

user_id = 416085550
user_info = vk.users.get(user_ids=user_id, fields='sex, bdate, city, country, subscriptions', v='5.131')
subscriptions = vk.users.getSubscriptions(user_id=user_id)
groups = vk.groups.get(user_id=user_id)
print(user_info)
# print(user_info)
# print("Подписки")
# print(subscriptions)
# print("Группы")
# print(groups)