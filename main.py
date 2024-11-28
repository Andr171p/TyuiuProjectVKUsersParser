import vk_api


token = "vk1.a.8bzJ1a_gj5bfnSZU77sCtyPlaSFS1HBhV9TIXQoD2usDLAZqm0YEeFKekeJoG5NmOkOgs7OwfBjZCnElh7b9Vr8lBIckA9VYbPcbJa_c2eZJgtpBIUhjp82U8rHe5Jk0bjHoJtG_lnFyEnfrROAme-Lo7ilomquaSUZz2ssVJwYFZMaebytvP-Ra4Eosy5BlcOFGUa_V8yK2qmF56nXCqg"


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
response = vk.groups.getMembers(group_id=222477990)
print(response)

user_id = 416085550
user_info = vk.users.get(user_ids=user_id, fields='sex, bdate, city, country, subscriptions', v='5.131')
subscriptions = vk.users.getSubscriptions(user_id=user_id, fields='user')
groups = vk.groups.get(user_id=user_id)
print(user_info)
print("Подписки")
print(subscriptions)
print("Группы")
print(groups)
print(3 * '=')
data = vk.groups.getById(group_id=181609358, fields='name, photo_200, screen_name, members_count')
print(data)