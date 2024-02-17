import sys

from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from windows import MainWindow
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
