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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(260, 392)
        mainWindow.setMinimumSize(QSize(260, 320))
        mainWindow.setMaximumSize(QSize(16777215, 398))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 241, 381))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(10)
        self.label_ports = QLabel(self.frame)
        self.label_ports.setObjectName(u"label_ports")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_ports)

        self.But_settings_ports = QPushButton(self.frame)
        self.But_settings_ports.setObjectName(u"But_settings_ports")
        self.But_settings_ports.setEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.But_settings_ports)

        self.label_send = QLabel(self.frame)
        self.label_send.setObjectName(u"label_send")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_send)

        self.Button_send = QPushButton(self.frame)
        self.Button_send.setObjectName(u"Button_send")
        self.Button_send.setEnabled(True)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.Button_send)

        self.label_download = QLabel(self.frame)
        self.label_download.setObjectName(u"label_download")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_download)

        self.Button_download = QPushButton(self.frame)
        self.Button_download.setObjectName(u"Button_download")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.Button_download)

        self.label_table = QLabel(self.frame)
        self.label_table.setObjectName(u"label_table")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_table)

        self.comments = QListWidget(self.frame)
        self.comments.setObjectName(u"comments")
        self.comments.setMinimumSize(QSize(221, 0))
        self.comments.setWordWrap(True)

        self.formLayout_2.setWidget(7, QFormLayout.SpanningRole, self.comments)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"testik", None))
        self.label_ports.setText(QCoreApplication.translate("mainWindow", u"Port settings:", None))
        self.But_settings_ports.setText(QCoreApplication.translate("mainWindow", u"Change", None))
        self.label_send.setText(QCoreApplication.translate("mainWindow", u"Send firmware:", None))
        self.Button_send.setText(QCoreApplication.translate("mainWindow", u"Send", None))
        self.label_download.setText(QCoreApplication.translate("mainWindow", u"Save data:", None))
        self.Button_download.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.label_table.setText(QCoreApplication.translate("mainWindow", u"Comments:", None))
    # retranslateUi

