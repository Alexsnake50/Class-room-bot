import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime
from datetime import date
import random
import time
vk_session = vk_api.VkApi(token='83b4c5cd93ff81cab83c0b4d85985aa648df73bf96d43f0eb1ec602a6bd738b8df5484893b658db0aebd0')
session_api = vk_session.get_api()
<<<<<<< Updated upstream
longpoll = VkBotLongPoll(vk_session, 183006227)
=======
longpoll = VkBotLongPoll(vk_session, 183006227) 
week = 0 
dt = datetime.now()
if dt.isocalendar()[1] % 2 == 0:
    week = 1
else:
    week =  2
>>>>>>> Stashed changes
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()
            if event.from_user:
<<<<<<< Updated upstream
                if event.obj.text == "понедельник" or event.obj.text == "Понедельник":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message='----' '<br>' 'Безопасность жизнедеятельности: каб.212' '<br>' 'Иностранный язык: каб.207' '<br>' 'Теория вероятности и математическая статистика: каб.214' '<br>' '----'
                )
=======
                if event.obj.text == "Понедельник" or event.obj.text == "понедельник":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= '----' '<br>' 'Безопасность жизнедеятельности: каб.212' '<br>' 'Иностранный язык: каб.207' '<br>' 'Теория вероятности и математическая статистика: каб.214' '<br>' '----'
                    )

                if event.obj.text == "Вторник" or event.obj.text == "вторник":
                    if week == 1:
                        session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= 'Основы бухгалтерского учёта: каб.216' '<br>' 'Основы теории информации: каб.213' '<br>' 'Математика: каб.214' '<br>' 'Менеджмент: каб.301' '<br>' 'Основы бухгалтерского учёта: каб.216' ,
                        )
                    elif week == 2:
                        session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= 'История: каб.302' '<br>' 'Основы теории информации: каб.213' '<br>' 'Математика: каб.214' '<br>' 'Менеджмент: каб.301' '<br>' 'Основы бухгалтерского учёта: каб.216' ,
                        )
                            

                if event.obj.text == "Среда" or event.obj.text == "среда":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message='Обработка отраслевой информации: каб.210' '<br>' 'Основы теории информации: каб.213' '<br>' 'Менеджмент: каб.301' '<br>' 'Методы обработки отраслевой информации: каб.210' '<br>' '----'
                    )

                if event.obj.text == "Четверг" or event.obj.text == "четверг":
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message='математика: каб.214' '<br>' 'Основы бухгалтерского учёта: каб.216' '<br>' 'Основы философии: каб.302' '<br>' 'Русский язык и культура речи: каб.215' '<br>' '----',
                    )

                if event.obj.text == "Пятница" or event.obj.text == "пятница":
                    if week == 1:
                        session_api.messages.send(
                            user_id=event.obj.from_id,
                            random_id = 0,
                            message='----' '<br>' '----' '<br>' 'Физическая культура С/З' '<br>' 'История: каб.302' '<br>' 'Русский язык и культура речи: каб 215',
                        )

                    elif week == 2:
                        session_api.messages.send(
                            user_id=event.obj.from_id,
                            random_id = 0,
                            message='----' '<br>' '----' '<br>' 'Физическая культура С/З' '<br>' 'Основы Философии: каб.302' '<br>' 'Русский язык и культура речи: каб 215',
                        )
                   
>>>>>>> Stashed changes
