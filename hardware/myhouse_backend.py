import time
from num2words import num2words

words_to_numbers = {num2words(i, lang='en'): str(i) for i in range(1, 20)}


class Arduino_pins:
    @staticmethod
    def window_pins(room_name=None, pin=None):
        titles_dict = {'hall': 'one', 'kitchen': 'two', 'bedroom': 'three', 'balcony': 'four'}
        if room_name:
            numword = titles_dict[room_name]
            pin = words_to_numbers.get(numword)
            return pin
        if pin:
            numword = num2words(number=pin)
            for key, value in titles_dict:
                if value == numword:
                    return key
        else:
            return False

    @staticmethod
    def light_pins(room_name=None, pin=None):
        """
        Returns the opposite, if you enter a pin, then the name of the room, if the name of the room, then the pin
        """
        titles_dict = {'free': 'five', 'hall': 'six', 'kitchen': 'seven', 'bedroom': 'eight', 'balcony': 'nine',
                       'warehouse': 'ten', 'wc': 'eleven', 'bathroom': 'twelve', 'free2': 'thirteen'}
        if room_name:
            numword = titles_dict[room_name]
            pin = words_to_numbers.get(numword)
            return pin
        elif pin:
            numword = num2words(number=pin)
            for key, value in titles_dict:
                if value == numword:
                    return key
        else:
            return False


class Room:
    def __init__(self, name, light_port='P1', windows_port='P2'):
        self.name = name
        self.light_pin = Arduino_pins.light_pins(room_name=name)
        self.pin_word = num2words(number=self.light_pin, lang='en')
        self.light_control_port = Serial(port_name=light_port)
        self.windows_control_port = Serial(port_name=windows_port)

    def get_light_status(self):
        response = self.light_control_port.send_command(command=f'LIGHT-STATUS-{self.light_pin}')
        return ((response[0]).split('-'))[1]

    def set_light_status(self, status: str):
        response = self.light_control_port.send_command(command=f'{self.pin_word}-{status}')
        return response

    def set_windows_state(self, state: str):
        response = self.windows_control_port.send_command(command=f'WINDOWS-SET-STATUS-{self.pin_word}')
        return response


class MyHouse:
    def __init__(self):
        self.rooms = {'hall': Room(name='hall'), 'kitchen': Room(name='kitchen'), 'bedroom': Room(name='bedroom'),
                      'balcony': Room(name='balcony'), 'warehouse': Room(name='warehouse'), 'bathroom': Room(name='bathroom')}

    def add_room(self, name):
        self.rooms[name] = Room(name)

    def get_room(self, name):
        return self.rooms.get(name)
