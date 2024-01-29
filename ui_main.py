# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(362, 398)
        mainWindow.setMinimumSize(QSize(0, 398))
        mainWindow.setMaximumSize(QSize(16777215, 398))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 80, 191, 24))
        self.progressBar.setMinimumSize(QSize(0, 16))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.comboBox_ports = QComboBox(self.centralwidget)
        self.comboBox_ports.addItem("")
        self.comboBox_ports.setObjectName(u"comboBox_ports")
        self.comboBox_ports.setGeometry(QRect(21, 33, 111, 21))
        self.label_send = QLabel(self.centralwidget)
        self.label_send.setObjectName(u"label_send")
        self.label_send.setGeometry(QRect(21, 60, 115, 16))
        self.label_table = QLabel(self.centralwidget)
        self.label_table.setObjectName(u"label_table")
        self.label_table.setGeometry(QRect(21, 164, 117, 16))
        self.Button_download = QPushButton(self.centralwidget)
        self.Button_download.setObjectName(u"Button_download")
        self.Button_download.setGeometry(QRect(21, 134, 91, 24))
        self.label_download = QLabel(self.centralwidget)
        self.label_download.setObjectName(u"label_download")
        self.label_download.setGeometry(QRect(21, 112, 101, 16))
        self.Button_send = QPushButton(self.centralwidget)
        self.Button_send.setObjectName(u"Button_send")
        self.Button_send.setEnabled(True)
        self.Button_send.setGeometry(QRect(22, 80, 91, 24))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(21, 186, 321, 192))
        self.label_ports = QLabel(self.centralwidget)
        self.label_ports.setObjectName(u"label_ports")
        self.label_ports.setGeometry(QRect(21, 11, 79, 16))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"testik", None))
        self.progressBar.setFormat(QCoreApplication.translate("mainWindow", u"%p%", None))
        self.comboBox_ports.setItemText(0, "")

#if QT_CONFIG(whatsthis)
        self.comboBox_ports.setWhatsThis(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_send.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0440\u043e\u0448\u0438\u0432\u043a\u0443:", None))
        self.label_table.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435:", None))
        self.Button_download.setText(QCoreApplication.translate("mainWindow", u"\u0421\u041a\u0410\u0427\u0410\u0422\u042c", None))
        self.label_download.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.Button_send.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c", None))
        self.label_ports.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u0440\u0442:", None))
    # retranslateUi

