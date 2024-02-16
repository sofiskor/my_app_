import serial
from PySide6.QtWidgets import QWidget
import serial.tools.list_ports

from ui_port_settings import Ui_Dialog



# поиск портов
def f_find_ports():
    ports = serial.tools.list_ports.comports()
    # for port in ports:
    #     print(port.device)
    return ports


class PortWindow(QWidget):
    PARITY = {
        "none": serial.PARITY_NONE,
        "even": serial.PARITY_EVEN,
        "odd": serial.PARITY_ODD,
        "mark": serial.PARITY_MARK,
        "space": serial.PARITY_SPACE
    }

    STOPBITS = {
        "1": serial.STOPBITS_ONE,
        "1,5": serial.STOPBITS_ONE_POINT_FIVE,
        "2": serial.STOPBITS_TWO
    }
    SPEED = ["1200", "1800", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]

    BYTESIZE = {
        "5": serial.FIVEBITS,
        "6": serial.SIXBITS,
        "7": serial.SEVENBITS,
        "8": serial.EIGHTBITS
    }

    def __init__(self):
        super(PortWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.hide)
        usb = f_find_ports()  # поиск портов
        self.ui.comboBox_ports.addItems([port.device for port in usb])
        self.ui.speed_bod.addItems(self.SPEED)
        self.ui.parity_check.addItems(self.PARITY.keys())
        self.ui.data_size.addItems(self.BYTESIZE.keys())
        self.ui.stop_bits.addItems(self.STOPBITS.keys())

        self.ui.but_default.clicked.connect(self.default_settings)

        # port settings current
        self.ui.speed_bod.setCurrentIndex(4)
        self.ui.data_size.setCurrentIndex(3)


    def default_settings(self):
        self.ui.speed_bod.setCurrentIndex(4)
        self.ui.data_size.setCurrentIndex(3)
        self.ui.parity_check.setCurrentIndex(0)
        self.ui.stop_bits.setCurrentIndex(0)
        self.ui.flow_control.setCurrentIndex(0)


