from hardware.serial_port import Ports
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.inline.arduino_keyboards import Arduino_kb
from shortcuts import filter_data

port16 = Ports('COM16', 9600)


@dp.message_handler(Text(contains='arduino'))
async def arduino_handler(msg: Message):
    await msg.answer("Управление устройствами: ", reply_markup=Arduino_kb.keyboard())


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('arduino'))
async def answer(call: CallbackQuery):
    data = filter_data(call.data, 'arduino,')
    if data == 'relay':
        keyboard = Arduino_kb.relay_keyboard()
    elif data == 'rgb-led':
        keyboard = Arduino_kb.rgb_led_keyboard()
    else:
        keyboard = False
    if not keyboard:
        await call.answer('Ошибка!')
        return
    await bot.send_message(chat_id=call.from_user.id, text=data, reply_markup=keyboard)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('switch-relay'))
async def switch_relay(call: CallbackQuery):
    dict = {5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}
    relay_number = int(filter_data(call.data, 'switch-relay='))
    response = port16.send_command(f'STATUS-{relay_number}')
    status = (response[0].split('-'))[1]
    new_status = 'on' if status == 'off' else 'off'
    relay_word_number = dict[relay_number]
    response2 = port16.send_command(f'{relay_word_number}-{new_status}')
    await call.answer(response2)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('switch-led'))
async def switch_led(call: CallbackQuery):
    dict = {'red': 13, 'green': 12, 'blue': 11}
    dict2 = {11: 'eleven', 12: 'twelve', 13: 'thirteen'}

    color = filter_data(call.data, 'switch-led=')
    led_number = dict[color]
    led_word_number = dict2[led_number]
    response = port16.send_command(f'STATUS-{led_number}')
    status = (response[0].split('-'))[1]
    new_status = 'on' if status == 'off' else 'off'
    response2 = port16.send_command(f'{led_word_number}-{new_status}')
    await call.answer(response2)
