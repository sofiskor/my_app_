# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_port_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(275, 408)
        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-10, 0, 291, 361))
        self.frame_6.setMinimumSize(QSize(241, 230))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_comboBox_ports = QLabel(self.frame_3)
        self.label_comboBox_ports.setObjectName(u"label_comboBox_ports")

        self.horizontalLayout_2.addWidget(self.label_comboBox_ports)

        self.comboBox_ports = QComboBox(self.frame_3)
        self.comboBox_ports.setObjectName(u"comboBox_ports")

        self.horizontalLayout_2.addWidget(self.comboBox_ports)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_send_5 = QLabel(self.frame_4)
        self.label_send_5.setObjectName(u"label_send_5")

        self.horizontalLayout_6.addWidget(self.label_send_5)

        self.speed_bod = QComboBox(self.frame_4)
        self.speed_bod.setObjectName(u"speed_bod")
        self.speed_bod.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.speed_bod)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_data_size = QLabel(self.frame_9)
        self.label_data_size.setObjectName(u"label_data_size")

        self.horizontalLayout_8.addWidget(self.label_data_size)

        self.data_size = QComboBox(self.frame_9)
        self.data_size.setObjectName(u"data_size")

        self.horizontalLayout_8.addWidget(self.data_size)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_parity_check = QLabel(self.frame_5)
        self.label_parity_check.setObjectName(u"label_parity_check")

        self.horizontalLayout_3.addWidget(self.label_parity_check)

        self.parity_check = QComboBox(self.frame_5)
        self.parity_check.setObjectName(u"parity_check")

        self.horizontalLayout_3.addWidget(self.parity_check)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.label_stop_bits = QLabel(self.frame)
        self.label_stop_bits.setObjectName(u"label_stop_bits")

        self.horizontalLayout_4.addWidget(self.label_stop_bits)

        self.stop_bits = QComboBox(self.frame)
        self.stop_bits.setObjectName(u"stop_bits")

        self.horizontalLayout_4.addWidget(self.stop_bits)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_flow_control = QLabel(self.frame_2)
        self.label_flow_control.setObjectName(u"label_flow_control")

        self.horizontalLayout_5.addWidget(self.label_flow_control)

        self.flow_control = QComboBox(self.frame_2)
        self.flow_control.addItem("")
        self.flow_control.addItem("")
        self.flow_control.addItem("")
        self.flow_control.setObjectName(u"flow_control")

        self.horizontalLayout_5.addWidget(self.flow_control)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.but_default = QPushButton(self.frame_7)
        self.but_default.setObjectName(u"but_default")

        self.verticalLayout_3.addWidget(self.but_default)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(Dialog)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 360, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Port setting", None))
        self.label_comboBox_ports.setText(QCoreApplication.translate("Dialog", u"Name", None))
#if QT_CONFIG(whatsthis)
        self.comboBox_ports.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_send_5.setText(QCoreApplication.translate("Dialog", u"B\u0430udrate", None))
#if QT_CONFIG(whatsthis)
        self.speed_bod.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_data_size.setText(QCoreApplication.translate("Dialog", u"Data size", None))
#if QT_CONFIG(whatsthis)
        self.data_size.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_parity_check.setText(QCoreApplication.translate("Dialog", u"Parity", None))
#if QT_CONFIG(whatsthis)
        self.parity_check.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_stop_bits.setText(QCoreApplication.translate("Dialog", u"Stopbits", None))
#if QT_CONFIG(whatsthis)
        self.stop_bits.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_flow_control.setText(QCoreApplication.translate("Dialog", u"Handshake", None))
        self.flow_control.setItemText(0, QCoreApplication.translate("Dialog", u"OFF", None))
        self.flow_control.setItemText(1, QCoreApplication.translate("Dialog", u"RTS/CTS", None))
        self.flow_control.setItemText(2, QCoreApplication.translate("Dialog", u"Xon/Xoff", None))

#if QT_CONFIG(whatsthis)
        self.flow_control.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u0440\u0442\u044b</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.but_default.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.backButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

