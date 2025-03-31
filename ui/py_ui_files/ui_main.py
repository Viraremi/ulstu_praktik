# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QSize(400, 300))
        self.actionOpenSheetSettingsWindow = QAction(MainWindow)
        self.actionOpenSheetSettingsWindow.setObjectName(u"actionOpenSheetSettingsWindow")
        self.actionSettingsListIgnore = QAction(MainWindow)
        self.actionSettingsListIgnore.setObjectName(u"actionSettingsListIgnore")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.textEditSelectedFilePath = QTextEdit(self.centralwidget)
        self.textEditSelectedFilePath.setObjectName(u"textEditSelectedFilePath")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditSelectedFilePath.sizePolicy().hasHeightForWidth())
        self.textEditSelectedFilePath.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textEditSelectedFilePath)

        self.textEditResultPath = QTextEdit(self.centralwidget)
        self.textEditResultPath.setObjectName(u"textEditResultPath")
        sizePolicy.setHeightForWidth(self.textEditResultPath.sizePolicy().hasHeightForWidth())
        self.textEditResultPath.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEditResultPath)

        self.btnOpenFile = QPushButton(self.centralwidget)
        self.btnOpenFile.setObjectName(u"btnOpenFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnOpenFile.sizePolicy().hasHeightForWidth())
        self.btnOpenFile.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btnOpenFile)

        self.btnSelectResultPath = QPushButton(self.centralwidget)
        self.btnSelectResultPath.setObjectName(u"btnSelectResultPath")
        sizePolicy1.setHeightForWidth(self.btnSelectResultPath.sizePolicy().hasHeightForWidth())
        self.btnSelectResultPath.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.btnSelectResultPath)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayoutSettings = QFormLayout()
        self.formLayoutSettings.setObjectName(u"formLayoutSettings")
        self.labelYear = QLabel(self.centralwidget)
        self.labelYear.setObjectName(u"labelYear")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelYear.sizePolicy().hasHeightForWidth())
        self.labelYear.setSizePolicy(sizePolicy2)

        self.formLayoutSettings.setWidget(0, QFormLayout.LabelRole, self.labelYear)

        self.spinBoxFileYear = QSpinBox(self.centralwidget)
        self.spinBoxFileYear.setObjectName(u"spinBoxFileYear")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBoxFileYear.sizePolicy().hasHeightForWidth())
        self.spinBoxFileYear.setSizePolicy(sizePolicy3)
        self.spinBoxFileYear.setMinimum(2000)
        self.spinBoxFileYear.setMaximum(3000)
        self.spinBoxFileYear.setValue(2025)

        self.formLayoutSettings.setWidget(0, QFormLayout.FieldRole, self.spinBoxFileYear)

        self.labelFileType = QLabel(self.centralwidget)
        self.labelFileType.setObjectName(u"labelFileType")
        sizePolicy2.setHeightForWidth(self.labelFileType.sizePolicy().hasHeightForWidth())
        self.labelFileType.setSizePolicy(sizePolicy2)

        self.formLayoutSettings.setWidget(1, QFormLayout.LabelRole, self.labelFileType)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioBtnFullFile = QRadioButton(self.centralwidget)
        self.radioBtnFullFile.setObjectName(u"radioBtnFullFile")
        self.radioBtnFullFile.setChecked(True)

        self.verticalLayout.addWidget(self.radioBtnFullFile)

        self.radioBtnULFile = QRadioButton(self.centralwidget)
        self.radioBtnULFile.setObjectName(u"radioBtnULFile")

        self.verticalLayout.addWidget(self.radioBtnULFile)


        self.formLayoutSettings.setLayout(1, QFormLayout.FieldRole, self.verticalLayout)


        self.horizontalLayout.addLayout(self.formLayoutSettings)

        self.labelError = QLabel(self.centralwidget)
        self.labelError.setObjectName(u"labelError")
        sizePolicy.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy)
        self.labelError.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelError.setWordWrap(True)

        self.horizontalLayout.addWidget(self.labelError)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.btnDoFormatToCSV = QPushButton(self.centralwidget)
        self.btnDoFormatToCSV.setObjectName(u"btnDoFormatToCSV")

        self.verticalLayout_3.addWidget(self.btnDoFormatToCSV)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 400, 21))
        self.menu_settings = QMenu(self.menuBar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_file = QMenu(self.menuBar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.spinBoxFileYear, self.radioBtnFullFile)
        QWidget.setTabOrder(self.radioBtnFullFile, self.radioBtnULFile)
        QWidget.setTabOrder(self.radioBtnULFile, self.btnDoFormatToCSV)

        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_settings.menuAction())
        self.menu_settings.addAction(self.actionOpenSheetSettingsWindow)
        self.menu_settings.addAction(self.actionSettingsListIgnore)
        self.menu_file.addAction(self.actionImport)
        self.menu_file.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0434\u0440\u043e\u0432\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.actionOpenSheetSettingsWindow.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043b\u0438\u0441\u0442\u043e\u0432", None))
        self.actionSettingsListIgnore.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u043d\u043e\u0440\u0438\u0440\u0438\u0432\u0430\u0442\u044c \u043b\u0438\u0441\u0442\u044b...", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.textEditSelectedFilePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
        self.textEditResultPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432...", None))
        self.btnOpenFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.btnSelectResultPath.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.labelYear.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.labelFileType.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0444\u0430\u0439\u043b\u0430:", None))
        self.radioBtnFullFile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.radioBtnULFile.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.labelError.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043d\u0430\u0447\u0430\u043b\u0430 \u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f...", None))
        self.btnDoFormatToCSV.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

