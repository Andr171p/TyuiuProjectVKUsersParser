'''import vk_api


token = "https://oauth.vk.com/blank.html#access_token=vk1.a.FDdFRA-6VbjS0Ried3VAvqdPpD1j0aV7ryzi02wCN_fYB7tfDA8x9UfbGH1TMq1WQTmDtubrKgtyL9wRu1DZeKtV6wMLDUvZGK5WDcomQ3Qtk-DSmGiUEXeOA_6G7gQzXP5Y4yHB7VvqSqDpmibayteHooV9neikAY0fnpPPeQSMXG51LrT0GcVYT3qa7cibbqj-0NmuBvZxZp1IhDZhag&expires_in=86400&user_id=573495756"

vk_session = vk_api.VkApi(token="vk1.a.FDdFRA-6VbjS0Ried3VAvqdPpD1j0aV7ryzi02wCN_fYB7tfDA8x9UfbGH1TMq1WQTmDtubrKgtyL9wRu1DZeKtV6wMLDUvZGK5WDcomQ3Qtk-DSmGiUEXeOA_6G7gQzXP5Y4yHB7VvqSqDpmibayteHooV9neikAY0fnpPPeQSMXG51LrT0GcVYT3qa7cibbqj-0NmuBvZxZp1IhDZhag")
vk = vk_session.get_api()'''


from parser.vk.auth.session import VkSession


session = VkSession
session_vk = session.session()
print(session_vk.users.get())

