import os

import serial
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal, QThreadPool, QRunnable, Slot
from PySide6.QtWidgets import QMainWindow
from .progress import ProgressWindow
from .port import PortWindow

from ui_main import Ui_mainWindow


class Signals(QObject):
    sent_to_port_finished = Signal(str, str, serial.Serial)
    sent_to_port_in_progress = Signal(int, int)


class Proga(QMainWindow):
    def __init__(self):
        # Инициализация родительского класса
        super(Proga, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.Button_download.clicked.connect(self.f_json_to_excel)  # кнопка открытия файла и преобр в эксель
        # self.comboBox_ports.addItems([port.device for port in usb])  # добавление портов в список
        self.progressWindow = ProgressWindow()
        self.ui.Button_send.clicked.connect(self.f_save_file)
        self.threadpool = QThreadPool()
        self.signals = Signals()
        self.signals.sent_to_port_finished.connect(self.sending_finished)
        self.signals.sent_to_port_in_progress.connect(self.print_sent_bytes)

        self.ui.But_settings_ports.clicked.connect(self.hide)
        self.ui.But_settings_ports.clicked.connect(self.change_port_settings)
        self.portWindow = PortWindow()
        self.portWindow.ui.backButton.clicked.connect(self.show)

        # открытие файла и преобразование его в эксель

    def f_json_to_excel(self):
        print('hi')
        # # выводит выбранный порт
        # chosen_port = self.comboBox_ports.currentText()
        # print(chosen_port)
        # # происходит чтение из файла и преобразование в эксель
        # try:
        #     ser = serial.Serial(port=chosen_port, baudrate=9600, bytesize=8, stopbits=serial.STOPBITS_ONE,
        #                         timeout=4.0)
        #
        #     worker = Worker(self.send_to_port, configr, ser, file_path, chosen_port)
        #     self.threadpool.start(worker)
        # except serial.SerialException as se:
        #     print("Serial port error:", str(se))
        # except KeyboardInterrupt:
        #     pass
        #     data = json.load(file)
        #
        # df = pd.json_normalize(data)
        # df.to_excel('data.xlsx', index=False)
        # print('JSON data has been converted to Excel')

    def change_port_settings(self):
        self.portWindow.show()
        self.hide()

    def f_save_file(self):

        with open(QtWidgets.QFileDialog.getOpenFileName(
                None,
                'Open File', './',
                'Files (*.bin),(*.txt)')[0], 'rb') as file:
            configr = file.read()
            file_path = file.name
            file_size = os.path.getsize(file_path)

        chosen_port = self.portWindow.ui.comboBox_ports.currentText()

        chosen_speed = int(self.portWindow.ui.speed_bod.currentText())

        chosen_parity_rus = self.portWindow.ui.parity_check.currentText()
        chosen_parity = self.portWindow.PARITY.get(chosen_parity_rus)

        chosen_stopbits_rus = self.portWindow.ui.stop_bits.currentText()
        chosen_stopbits = self.portWindow.STOPBITS.get(chosen_stopbits_rus)

        chosen_flowcontrol = self.portWindow.ui.flow_control.currentText()
        if chosen_flowcontrol == "Аппаратное":
            ch_xonooff = False
            ch_rtscts = True
        elif chosen_flowcontrol == "Программное":
            ch_xonooff = True
            ch_rtscts = False
        else:
            ch_xonooff = False
            ch_rtscts = False

        try:
            ser = serial.Serial(port=chosen_port, baudrate=chosen_speed, parity=chosen_parity, stopbits=chosen_stopbits,
                                timeout=4.0, xonxoff=ch_xonooff, rtscts=ch_rtscts)

            worker = Worker(self.send_to_port, configr, ser, file_path, chosen_port)
            self.threadpool.start(worker)
        except serial.SerialException as se:
            print("Serial port error:", str(se))
        except KeyboardInterrupt:
            pass

        # self.progressWindow.ui.stopButton.clicked.connect(self.progressWindow.stop_process)

    def send_to_port(self, configr, ser, file_path, choosen_port):
        total_bytes = len(configr)  # Общее количество байт в файле
        bytes_sent = 0  # Инициализируем счетчик переданных байт

        while bytes_sent < total_bytes:
            bytes_to_send = min(100, total_bytes - bytes_sent)  # Определяем количество байт для отправки
            sent = ser.write(configr[bytes_sent:bytes_sent + bytes_to_send])  # Отправляем данные
            bytes_sent += sent  # Обновляем счетчик переданных байт
            self.signals.sent_to_port_in_progress.emit(bytes_sent, total_bytes)
        self.signals.sent_to_port_finished.emit(file_path, choosen_port, ser)

    def print_sent_bytes(self, sent, total):
        print(f"Отправлено {sent} из {total} байт")
        self.progressWindow.show()
        self.progressWindow.ui.progress.setValue(sent / total * 100)

    def sending_finished(self, file_path, chosen_port, ser):
        print(f"File {file_path} sent to COM port {chosen_port} successfully.")
        if ser.is_open:
            ser.close()
            print("Serial connection closed.")


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        self.fn(*self.args, **self.kwargs)
