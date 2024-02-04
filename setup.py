import sys

from PySide6.QtWidgets import QApplication
from main import Proga

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Proga()
    window.show()

    sys.exit(app.exec())