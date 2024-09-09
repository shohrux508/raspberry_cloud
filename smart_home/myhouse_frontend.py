from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from .keyboards import myHome_kb
from shortcuts import filter_data


@dp.message_handler(Text(contains='myhouse'))
async def SmartHome(msg: Message):
    await msg.answer("/rooms - Комнаты.\n\n"
                     "/windows - Все окна.\n\n"
                     "/security - Безопасность.\n\n"
                     "/lights - Управление освещением.\n\n"
                     "/shutdown - Вырубить питание.\n")


@dp.message_handler(Text(contains='status'))
async def houseStatus(msg: Message, state: FSMContext):
    await msg.answer("Статус: ")
    """
    Статус всех комнат.
    Образец:
    Кухня: 
    1.Свет - включён.
    2.Температура - 25.5 градусов.
    3.Двери - открыты.

    """


@dp.message_handler(Text(contains='windows'))
async def allWindows(msg: Message, state: FSMContext):
    await msg.answer("Все окна: ")
    """
    Статус окон.
    Образец:
    1.Закрыть все окна.
    2.Открыть все окна.

    """


@dp.message_handler(Text(contains='security'))
async def homeSecurity(msg: Message, state: FSMContext):
    await msg.answer("Безопасноть: ")
    """ 
    1.Камеры видеонаблюдения.
    2.Сигнализация.
    3.Статус дверей.
    """


@dp.message_handler(Text(contains='lights'))
async def homeLights(msg: Message, state: FSMContext):
    await msg.answer("Освещение: ")
    """ 
    1.Включить все осветительные приборы.
    2.Выключить все осветительные приборы.
    """


@dp.message_handler(Text(contains='shutdown'))
async def shutdown(msg: Message, state: FSMContext):
    await msg.answer("Питание: ")
    """ 
    1.Вырубить питание.
    2.Установить таймер для выключения.
    """
