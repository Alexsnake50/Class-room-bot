import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime
import random
import time
from Meta_Data import Name, mt, Metadata 
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
                for x in Name:
                    if x == event.obj.text:
                        DataName = Name.index(x)
                        if DataName == 2 or DataName == 3 or DataName == 8 or DataName == 9 and week == 2:
                            m = 0
                            if DataName == 2 or DataName == 3 :
                                m = mt.Tuesday2
                            elif DataName == 8 or DataName == 9 :
                                m = mt.Friday2
                            session_api.messages.send(
                                user_id=event.obj.from_id,
                                random_id = 0,
                                message=m
                            )
                        else :
                            session_api.messages.send(
                                user_id=event.obj.from_id,
                                random_id = 0,
                                message= Metadata[DataName]
                            )
                if Name.count(event.obj.text)  == 0 and event.obj.text != "Начать" :
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= "Такой команды к сожалению нету :*<",
                    )
                if event.obj.text == "Начать": 
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= "Команды для получения расписания, это всего лишь название дня недели на которое вы хотите получить расписание, к примеру “Понедельник” заглавность первой буквы не играет роли." "<br>" "Если вы хотите получить расписание на всю неделю, напишите “Неделя”, однако неделя может работать немного не так как нужно",
                    )     