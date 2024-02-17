# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressbar.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_progressWindow(object):
    def setupUi(self, progressWindow):
        if not progressWindow.objectName():
            progressWindow.setObjectName(u"progressWindow")
        progressWindow.resize(411, 110)
        self.stopButton = QPushButton(progressWindow)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(170, 70, 75, 24))
        self.frame = QFrame(progressWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 0, 371, 66))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progress = QProgressBar(self.frame)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(0)
        self.progress.setTextVisible(False)

        self.verticalLayout.addWidget(self.progress)


        self.retranslateUi(progressWindow)

        QMetaObject.connectSlotsByName(progressWindow)
    # setupUi

    def retranslateUi(self, progressWindow):
        progressWindow.setWindowTitle(QCoreApplication.translate("progressWindow", u"Progress", None))
        self.stopButton.setText(QCoreApplication.translate("progressWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("progressWindow", u"Downloading file", None))
    # retranslateUi

