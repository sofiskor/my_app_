from PySide6.QtWidgets import QWidget

from ui_progressbar import Ui_progressWindow


class ProgressWindow(QWidget):
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.ui = Ui_progressWindow()
        self.ui.setupUi(self)

