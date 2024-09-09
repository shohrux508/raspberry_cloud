from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from smart_home.keyboards import myHome_kb, RoomManager_kb
from hardware.myhouse_backend import MyHouse
from shortcuts import filter_data
import time


@dp.message_handler(Text(contains='rooms'))
async def allRooms(msg: Message):
    await msg.answer("Управление комнатами: ", reply_markup=myHome_kb().main_rooms())


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('home, room'))
async def manageRoom(call: CallbackQuery):
    room_name = filter_data(call.data, 'home, room=')
    keyboard = RoomManager_kb(room_name=room_name)
    await call.message.edit_text(text=f'Выберите действие над комнатой: {room_name}.',
                                 reply_markup=keyboard.manage_room())


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('manage-room, light'))
async def manageLight(call: CallbackQuery):
    status, room_name = (filter_data(call.data, 'manage-room, light-')).split('=')
    room = MyHouse().get_room(room_name)
    response = room.set_light_status(status=status)
    keyboard = RoomManager_kb(room_name=room_name)
    await call.answer(f'{room}\n{response}')
    time.sleep(1)
    await bot.edit_message_text(chat_id=call.message.from_user.id, message_id=call.message.message_id,
                                text=f'Действие над комнатой {room}: ',
                                reply_markup=keyboard.manage_room())


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('manage-room, windows'))
async def manageWindows(call: CallbackQuery):
    status, room_name = (filter_data(call.data, 'manage-room, windows-')).split('=')
    room = MyHouse().get_room(room_name)
    response = room.windows()
