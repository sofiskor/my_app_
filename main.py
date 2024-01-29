from PySide6.QtWidgets import QMainWindow, QApplication
from ui_main import Ui_mainWindow
from ui_progressbar import Ui_Dialog

import pandas as pd
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal, QRunnable, QObject, pyqtSlot, QThreadPool
import json
import sys
import serial.tools.list_ports
import serial
import os


# поиск портов
def f_find_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.device)
    return ports


class Signals(QObject):
    sent_to_port_finished = pyqtSignal(str, str, serial.Serial)
    sent_to_port_in_progress = pyqtSignal(int, int)


class Proga(QMainWindow, Ui_mainWindow):
    def __init__(self):
        # Инициализация родительского класса
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.Button_download.clicked.connect(self.f_json_to_excel)  # кнопка открытия файла и преобр в эксель
        usb = f_find_ports()  # поиск портов
        self.comboBox_ports.addItems([port.device for port in usb])  # добавление портов в список
        self.Button_send.clicked.connect(self.f_save_file)
        self.threadpool = QThreadPool()
        self.signals = Signals()
        self.signals.sent_to_port_finished.connect(self.sending_finished)
        self.signals.sent_to_port_in_progress.connect(self.print_sent_bytes)

    # открытие файла и преобразование его в эксель
    def f_json_to_excel(self):
        with open(QtWidgets.QFileDialog.getOpenFileName(
                None,
                'Open File', './',
                'Files (*.json)')[0], 'r') as file:
            print(file)
            data = json.load(file)

        df = pd.json_normalize(data)
        df.to_excel('data.xlsx', index=False)
        print('JSON data has been converted to Excel')

        ## добавить ошибку закрытия файла ##

    def f_save_file(self):
        with open(QtWidgets.QFileDialog.getOpenFileName(
                None,
                'Open File', './',
                'Files (*.bin),(*.txt)')[0], 'rb') as file:
            configr = file.read()
            file_path = file.name
            file_size = os.path.getsize(file_path)

        chosen_port = self.comboBox_ports.currentText()
        print(file_size)
        print(chosen_port)

        try:
            ser = serial.Serial(port=chosen_port, baudrate=9600, bytesize=8, stopbits=serial.STOPBITS_ONE,
                                timeout=4.0)

            worker = Worker(self.send_to_port, configr, ser, file_path, chosen_port)
            self.threadpool.start(worker)
        except serial.SerialException as se:
            print("Serial port error:", str(se))
        except KeyboardInterrupt:
            pass

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
        self.progressBar.setValue(sent / total * 100)

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

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        self.fn(*self.args, **self.kwargs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Proga()
    window.show()
    sys.exit(app.exec())
