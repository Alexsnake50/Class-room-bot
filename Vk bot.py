import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime
import random
import time
vk_session = vk_api.VkApi(token='83b4c5cd93ff81cab83c0b4d85985aa648df73bf96d43f0eb1ec602a6bd738b8df5484893b658db0aebd0')
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 183006227)
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()
            if event.from_user:
                if event.obj.text == "понедельник" or event.obj.text == "Понедельник":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message='----' '<br>' 'Безопасность жизнедеятельности: каб.212' '<br>' 'Иностранный язык: каб.207' '<br>' 'Теория вероятности и математическая статистика: каб.214' '<br>' '----'
                )