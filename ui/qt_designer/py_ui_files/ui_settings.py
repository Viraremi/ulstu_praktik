# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(250, 300)
        SettingsWindow.setMinimumSize(QSize(250, 300))
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelSheetSettings = QLabel(self.centralwidget)
        self.labelSheetSettings.setObjectName(u"labelSheetSettings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSheetSettings.sizePolicy().hasHeightForWidth())
        self.labelSheetSettings.setSizePolicy(sizePolicy)
        self.labelSheetSettings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelSheetSettings)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnSettingsShow = QPushButton(self.centralwidget)
        self.btnSettingsShow.setObjectName(u"btnSettingsShow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSettingsShow.sizePolicy().hasHeightForWidth())
        self.btnSettingsShow.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btnSettingsShow)

        self.btnSettingsAdd = QPushButton(self.centralwidget)
        self.btnSettingsAdd.setObjectName(u"btnSettingsAdd")
        sizePolicy1.setHeightForWidth(self.btnSettingsAdd.sizePolicy().hasHeightForWidth())
        self.btnSettingsAdd.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btnSettingsAdd)

        self.btnSettingsDelete = QPushButton(self.centralwidget)
        self.btnSettingsDelete.setObjectName(u"btnSettingsDelete")
        sizePolicy1.setHeightForWidth(self.btnSettingsDelete.sizePolicy().hasHeightForWidth())
        self.btnSettingsDelete.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btnSettingsDelete)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.labelSheetSettings.setText(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043b\u0438\u0441\u0442\u043e\u0432", None))
        self.btnSettingsShow.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0438\u043c\u0435\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btnSettingsAdd.setText(QCoreApplication.translate("SettingsWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0438\u0441\u0442", None))
        self.btnSettingsDelete.setText(QCoreApplication.translate("SettingsWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043b\u0438\u0441\u0442", None))
    # retranslateUi

