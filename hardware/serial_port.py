import serial
import time


class Ports:
    def __init__(self, port_name, baud_rate):
        ser = serial.Serial(port_name, baud_rate)
        self.ser = ser

    def clear_buffer(self):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        return True

    def send_command(self, command):
        self.clear_buffer()
        response_lines = []
        self.ser.write((command + '\n').encode())
        time.sleep(1)
        while self.ser.in_waiting > 0:  # Пока есть данные в буфере
            line = self.ser.readline().decode().strip()
            if line:
                response_lines.append(line)
        print(response_lines)
        return response_lines

    def read(self):
        response_lines = []
        while self.ser.in_waiting > 0:  # Пока есть данные в буфере
            line = self.ser.readline().decode().strip()
            if line:
                response_lines.append(line)
        return response_lines

# class Ports:
#     def __init__(self):
#         self.com_ports = {'P1': {'port': 'COM15', 'baud_rate': 9600}}
#     @staticmethod
#     def connect(port_name, baud_rate):
#         ser = serial.Serial(port_name, baud_rate)
#         return ser
#
#     def add_com_port(self, title, port_name, baud_rate):
#         """
#         Подключение последовательного порта.
#         title - Название по желанию для ориентации по портам.
#         port_name - Сам последовательный порт, и baud_rate - скорость передачи данных.
#         """
#         self.com_ports[title] = {'port': port_name, 'baud_rate': baud_rate}
#
#     def get_com_port(self, name):
#         """ Подключаем последовательный порт с помощью названия(name) порта, которого мы сами задали. """
#         port = self.com_ports[name]
#         ser = serial.Serial(port['port'], port['baud_rate'])
#         time.sleep(2)
#         return ser
#
#
# class Serial:
#     def __init__(self, port_name):
#         self.p = Ports().get_com_port(name=port_name)
#
#     def clear_buffer(self):
#         self.p.reset_input_buffer()
#         self.p.reset_output_buffer()
#         return True
#
#     def send_command(self, command):
#         self.clear_buffer()
#         response_lines = []
#         self.p.write((command + '\n').encode())
#         time.sleep(1)
#         while self.p.in_waiting > 0:  # Пока есть данные в буфере
#             line = self.p.readline().decode().strip()
#             if line:
#                 response_lines.append(line)
#         return response_lines
#
#     def read(self):
#         response_lines = []
#         while self.p.in_waiting > 0:  # Пока есть данные в буфере
#             line = self.p.readline().decode().strip()
#             if line:
#                 response_lines.append(line)
#         return response_lines
