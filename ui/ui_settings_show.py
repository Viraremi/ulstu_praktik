# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI_settings_show.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import test_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSettingsShowHeader = QLabel(Dialog)
        self.labelSettingsShowHeader.setObjectName(u"labelSettingsShowHeader")

        self.verticalLayout.addWidget(self.labelSettingsShowHeader)

        self.textEditShowSettings = QTextEdit(Dialog)
        self.textEditShowSettings.setObjectName(u"textEditShowSettings")
        self.textEditShowSettings.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEditShowSettings)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelSettingsShowHeader.setText(QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435 \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.textEditShowSettings.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0415\u0441\u043b\u0438 \u0432\u044b \u044d\u0442\u043e \u0447\u0438\u0442\u0430\u0435\u0442\u0435, \u0442\u043e \u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u043d\u0435\u0442!", None))
    # retranslateUi

