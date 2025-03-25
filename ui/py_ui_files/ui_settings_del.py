# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI_settings_del.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(250, 150)
        Dialog.setMinimumSize(QSize(250, 150))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSettingsDelHeader = QLabel(Dialog)
        self.labelSettingsDelHeader.setObjectName(u"labelSettingsDelHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSettingsDelHeader.sizePolicy().hasHeightForWidth())
        self.labelSettingsDelHeader.setSizePolicy(sizePolicy)
        self.labelSettingsDelHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelSettingsDelHeader)

        self.comboBoxSelectList = QComboBox(Dialog)
        self.comboBoxSelectList.addItem("")
        self.comboBoxSelectList.addItem("")
        self.comboBoxSelectList.setObjectName(u"comboBoxSelectList")

        self.verticalLayout.addWidget(self.comboBoxSelectList)

        self.btnDeleteSelectedList = QPushButton(Dialog)
        self.btnDeleteSelectedList.setObjectName(u"btnDeleteSelectedList")

        self.verticalLayout.addWidget(self.btnDeleteSelectedList)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelSettingsDelHeader.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043b\u0438\u0441\u0442\u0430...", None))
        self.comboBoxSelectList.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04401", None))
        self.comboBoxSelectList.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04402", None))

        self.btnDeleteSelectedList.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

