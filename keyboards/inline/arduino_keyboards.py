from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_btn = InlineKeyboardButton(text='Назад', callback_data='arduino, keyboard')


class Arduino_kb:

    @staticmethod
    def keyboard():
        btn1 = InlineKeyboardButton(text='Реле', callback_data='arduino,relay')
        btn2 = InlineKeyboardButton(text='RGB Светодиод', callback_data='arduino,rgb-led')
        return InlineKeyboardMarkup().add(btn1).add(btn2)

    @staticmethod
    def relay_keyboard():
        btn1 = InlineKeyboardButton(text='Реле - 1', callback_data='switch-relay=5')
        btn2 = InlineKeyboardButton(text='Реле - 2', callback_data='switch-relay=6')
        btn3 = InlineKeyboardButton(text='Реле - 3', callback_data='switch-relay=7')
        btn4 = InlineKeyboardButton(text='Реле - 4', callback_data='switch-relay=8')
        keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4).add(back_btn)
        return keyboard

    @staticmethod
    def rgb_led_keyboard():
        btn1 = InlineKeyboardButton(text='Красный', callback_data='switch-led=red')
        btn2 = InlineKeyboardButton(text='Зелёный', callback_data='switch-led=green')
        btn3 = InlineKeyboardButton(text='Синий', callback_data='switch-led=blue')
        keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3).add(back_btn)
        return keyboard
