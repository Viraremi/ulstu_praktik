# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI_settings_del_ignore.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSettingsIgnoreListHeader = QLabel(Dialog)
        self.labelSettingsIgnoreListHeader.setObjectName(u"labelSettingsIgnoreListHeader")

        self.verticalLayout.addWidget(self.labelSettingsIgnoreListHeader)

        self.listWidgetSheetsList = QListWidget(Dialog)
        QListWidgetItem(self.listWidgetSheetsList)
        QListWidgetItem(self.listWidgetSheetsList)
        QListWidgetItem(self.listWidgetSheetsList)
        QListWidgetItem(self.listWidgetSheetsList)
        QListWidgetItem(self.listWidgetSheetsList)
        self.listWidgetSheetsList.setObjectName(u"listWidgetSheetsList")
        self.listWidgetSheetsList.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout.addWidget(self.listWidgetSheetsList)

        self.btnSaveSelect = QPushButton(Dialog)
        self.btnSaveSelect.setObjectName(u"btnSaveSelect")

        self.verticalLayout.addWidget(self.btnSaveSelect)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelSettingsIgnoreListHeader.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043b\u0438\u0441\u0442\u044b \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0443\u0436\u043d\u043e \u0438\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))

        __sortingEnabled = self.listWidgetSheetsList.isSortingEnabled()
        self.listWidgetSheetsList.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetSheetsList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04401", None));
        ___qlistwidgetitem1 = self.listWidgetSheetsList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04402", None));
        ___qlistwidgetitem2 = self.listWidgetSheetsList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04403", None));
        ___qlistwidgetitem3 = self.listWidgetSheetsList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04404", None));
        ___qlistwidgetitem4 = self.listWidgetSheetsList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u04405", None));
        self.listWidgetSheetsList.setSortingEnabled(__sortingEnabled)

        self.btnSaveSelect.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440", None))
    # retranslateUi

