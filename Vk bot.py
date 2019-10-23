import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime, date
import random
import time
from Meta_Data import mt, Name, Metadata
vk_session = vk_api.VkApi(token='83b4c5cd93ff81cab83c0b4d85985aa648df73bf96d43f0eb1ec602a6bd738b8df5484893b658db0aebd0')
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 183006227)
longpoll = VkBotLongPoll(vk_session, 183006227) 
week = 0 
dt = datetime.now()
array = ["Как же не хочется на пары","Скоро сессия, а может и нет","Скоро отчисление","Прятного дня, но это не та команда","Опять бух учёт !","Нет завтра не выходной", "Прошу прощения, вы ошиблись","Извините, но такой команды нету", "Пидрила ебанный", "уёбак сранный","Хуесас дебил", "Нету такой команды","СКАЗАЛИ ЖЕ НЕТУ ТАКОЙ КОМАНДЫ","Ты дебил ?","НЕТ ТАКОЙ КОМАНДЫ !", "Уди отсюда","Ты это, это, НЕ ИСПЫТЫВАЙ МЕНЯ"]
if dt.isocalendar()[1] % 2 == 0:
    week = 1
else:
    week =  2
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
                            session_api.messages.send(
                                user_id=event.obj.from_id,
                                random_id = 0,
                                message= Metadata[DataName+1]
                            )
                        else :
                            session_api.messages.send(
                                user_id=event.obj.from_id,
                                random_id = 0,
                                message= Metadata[DataName]
                            )
                if Name.count(event.obj.text)  == 0:
                    session_api.messages.send(
                        user_id=event.obj.from_id,
                        random_id = 0,
                        message= array[random.randrange (0,17,1)],
                    )
