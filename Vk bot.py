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
                if event.obj.text == "Неделя 1":
                    week = 1
                elif event.obj.text == "Неделя 2":
                    week = 2
                if event.obj.text == "Понедельник" or event.obj.text == "понедельник":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= '----' '<br>' 'Безопасность жизнедеятельности: каб.212' '<br>' 'Иностранный язык: каб.207' '<br>' 'Теория вероятности и математическая статистика: каб.214' '<br>' '----'
                )
                if event.obj.text == "Вторник" or event.obj.text == "вторник":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= ""
                    )
                if event.obj.text == "Среда" or event.obj.text == "среда":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message=""
                    )
                if event.obj.text == "Четверг" or event.obj.text == "четверг":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message=""
                    )
                if event.obj.text == "Пятница" or event.obj.text == "пятница":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message=""
                    )
                print(week);
                