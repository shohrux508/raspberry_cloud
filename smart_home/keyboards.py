from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from hardware.myhouse_backend import Room, MyHouse

cross_btn = InlineKeyboardButton(text='❌', callback_data='bot, msg, clear')
rooms_dict = {'kitchen': 'Кухня', 'bedroom': 'Спальня', 'hall': 'Зал', 'balcony': 'Балкон'}


class myHome_kb():
    @staticmethod
    def main_rooms():
        buttons = [InlineKeyboardButton(text=f'{value}', callback_data=f'home, room={key}') for key, value in
                   rooms_dict.items()]
        btn1, btn2, btn3, btn4 = buttons
        btn5 = InlineKeyboardButton(text='Маленькие комнаты', callback_data='home, rooms=small')
        return InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4).add(btn5).add(cross_btn)

    @staticmethod
    def small_rooms():
        btn1 = InlineKeyboardButton(text='Уборная', callback_data='home, room=wc')
        btn2 = InlineKeyboardButton(text='Ванная', callback_data='home, room=bathroom')
        btn3 = InlineKeyboardButton(text='Кладовка', callback_data='home, room=warehouse')
        btn4 = InlineKeyboardButton(text='Основные комнаты', callback_data='home, rooms=main')
        return InlineKeyboardMarkup().add(btn1, btn2).add(btn3).add(btn4).add(cross_btn)


class RoomManager_kb():
    def __init__(self, room_name):
        self.room_name = room_name
        self.room = MyHouse().get_room(name=self.room_name)

    def manage_room(self):
        status = self.room.get_light_status()
        btn1 = InlineKeyboardButton(text='Вкл-свет', callback_data=f'manage-room, light-on={self.room_name}')
        btn2 = InlineKeyboardButton(text='Выкл-свет', callback_data=f'manage-room, light-off={self.room_name}')
        light_btn = btn1 if status == 'off' else btn2
        btn3 = InlineKeyboardButton(text='Открыть окна', callback_data=f'manage-room, windows-open={self.room_name}')
        btn4 = InlineKeyboardButton(text='Закрыть окна', callback_data=f'manage-room, windows-close={self.room_name}')
        btn5 = InlineKeyboardButton(text='Управления розетками', callback_data=f'manage-room, ...={self.room_name}')
        keyboard = InlineKeyboardMarkup().add(light_btn).add(btn3).add(btn4).add(btn5).add(cross_btn)
        return keyboard
