import os

import serial
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal, QThreadPool, QRunnable, Slot
from PySide6.QtWidgets import QMainWindow

from .progress import ProgressWindow
from .port import PortWindow, UpdatePorts
from ui_main import Ui_mainWindow


class Signals(QObject):
    sent_to_port_finished = Signal(str, str, int, int, serial.Serial)
    sent_to_port_in_progress = Signal(int, int)


class MainWindow(QMainWindow):
    cancel_send_flag = False

    def __init__(self):
        # Инициализация родительского класса
        super(MainWindow, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.Button_download.clicked.connect(self.f_json_to_excel)  # кнопка скачивания\\ не доделана

        # загрузка прошивки
        self.ui.Button_send.clicked.connect(self.send_file)  # кнопка отправки файла на мк
        self.progressWindow = ProgressWindow()  # окно с индикатором процессом
        self.progressWindow.ui.stopButton.clicked.connect(self.stop_sending)  # отмена загрузки файла
        self.threadpool = QThreadPool()
        self.signals = Signals()
        self.signals.sent_to_port_in_progress.connect(self.print_sent_bytes)  # отображение % загрузки
        self.signals.sent_to_port_finished.connect(self.sending_finished)  # конец отправки файла

        # настройка порта
        self.ui.But_settings_ports.clicked.connect(self.hide)  # скрытие главного окна
        self.portWindow = PortWindow()  # окно с настройкой порта
        self.ui.But_settings_ports.clicked.connect(self.change_port_settings)  # открытие окна "настройка порта"
        self.updatePorts = UpdatePorts()
        self.updatePorts.update_list_signal.connect(self.portWindow.update_comboBox)  # обновление списка портов
        self.ui.But_settings_ports.clicked.connect(self.updatePorts.update_list_signal)
        self.portWindow.ui.backButton.clicked.connect(self.show)  # возврат в главное меню

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

    # окно "настройка порта"
    def change_port_settings(self):
        self.portWindow.show()
        self.hide()

    # отправка файл при нажатии кнопки "загрузить"
    def send_file(self):
        self.cancel_send_flag = False
        # открытие файл с прошивкой
        with open(QtWidgets.QFileDialog.getOpenFileName(
                None,
                'Open File', './',
                'Files (*.bin),(*.txt)')[0], 'rb') as file:
            configr = file.read()
            file_path = file.name
            file_size = os.path.getsize(file_path)

        chosen_port = self.portWindow.ui.comboBox_ports.currentText()  # выбранный порт
        chosen_speed = int(self.portWindow.ui.speed_bod.currentText())  # выбранная скорость
        chosen_parity_rus = self.portWindow.ui.parity_check.currentText()
        chosen_parity = self.portWindow.PARITY.get(chosen_parity_rus)  # выбранная четность
        chosen_stopbits_rus = self.portWindow.ui.stop_bits.currentText()
        chosen_stopbits = self.portWindow.STOPBITS.get(chosen_stopbits_rus)  # выбранный стопбит
        chosen_bytesize_rus = self.portWindow.ui.data_size.currentText()
        chosen_bytesize = self.portWindow.BYTESIZE.get(chosen_bytesize_rus)  # выбранный стопбит
        chosen_flowcontrol = self.portWindow.ui.flow_control.currentText()
        # определенние контроля порта
        if chosen_flowcontrol == "RTS/CTS":
            ch_xonooff = False
            ch_rtscts = True
        elif chosen_flowcontrol == "Xon/Xoff":
            ch_xonooff = True
            ch_rtscts = False
        else:
            ch_xonooff = False
            ch_rtscts = False
        # открытие порта
        try:
            ser = serial.Serial(port=chosen_port, baudrate=chosen_speed, bytesize=chosen_bytesize,
                                parity=chosen_parity, stopbits=chosen_stopbits,
                                timeout=4.0, xonxoff=ch_xonooff, rtscts=ch_rtscts)

            worker = Worker(self.send_to_port, configr, ser, file_path, chosen_port)
            self.threadpool.start(worker)
        # прописывание исключений
        except serial.SerialException as se:
            print(f"Serial port error: {str(se)}")
            self.ui.comments.addItem(f"Serial port error: {str(se)}")
        except KeyboardInterrupt:
            pass

    # функция записи файла в мк
    def send_to_port(self, configr, ser, file_path, choosen_port):
        total_bytes = len(configr)  # Общее количество байт в файле
        bytes_sent = 0  # Инициализируем счетчик переданных байт

        while not self.cancel_send_flag and bytes_sent < total_bytes:
            bytes_to_send = min(100, total_bytes - bytes_sent)  # Определяем количество байт для отправки
            # запись файла в порт
            try:
                sent = ser.write(configr[bytes_sent:bytes_sent + bytes_to_send])  # Отправляем данные
                bytes_sent += sent  # Обновляем счетчик переданных байт
                self.signals.sent_to_port_in_progress.emit(bytes_sent, total_bytes)
            except serial.SerialException as exc:
                print(f"Произошла ошибка при работе с портом: {exc}")
                self.progressWindow.hide()
                self.ui.comments.addItem(f"Error: {exc}")
                break
        # закрывает порт
        self.signals.sent_to_port_finished.emit(file_path, choosen_port, bytes_sent, total_bytes, ser)

    # отсновка отправки файла
    def stop_sending(self):
        self.cancel_send_flag = True
        print("Interrupted by the user")
        self.ui.comments.addItem("Interrupted by the user")

    # отображение процесса отправленных бит
    def print_sent_bytes(self, sent, total):
        print(f"Отправлено {sent} из {total} байт")
        self.progressWindow.show()
        self.progressWindow.ui.progress.setValue(sent / total * 100)

    # конец отправки файла
    def sending_finished(self, file_path, chosen_port, bytes_sent, total_bytes, ser):
        if bytes_sent == total_bytes:
            print(f"File {file_path} sent to COM port {chosen_port} successfully.")
            self.ui.comments.addItem(f"File {file_path} sent to COM port {chosen_port} successfully.")

        else:
            print("File not sent")
            self.progressWindow.close()
            self.ui.comments.addItem("File not sent. Try again.")
        if ser.is_open:
            ser.close()
            print("Serial connection closed.")
            self.progressWindow.close()


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
