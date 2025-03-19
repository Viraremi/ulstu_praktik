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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QSize(400, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnOpenFile = QPushButton(self.centralwidget)
        self.btnOpenFile.setObjectName(u"btnOpenFile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenFile.sizePolicy().hasHeightForWidth())
        self.btnOpenFile.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btnOpenFile)

        self.labelFilePath = QLabel(self.centralwidget)
        self.labelFilePath.setObjectName(u"labelFilePath")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelFilePath.sizePolicy().hasHeightForWidth())
        self.labelFilePath.setSizePolicy(sizePolicy1)
        self.labelFilePath.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.labelFilePath)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)

        self.textEditSelectedFilePath = QTextEdit(self.centralwidget)
        self.textEditSelectedFilePath.setObjectName(u"textEditSelectedFilePath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEditSelectedFilePath.sizePolicy().hasHeightForWidth())
        self.textEditSelectedFilePath.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textEditSelectedFilePath)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnSelectResultPath = QPushButton(self.centralwidget)
        self.btnSelectResultPath.setObjectName(u"btnSelectResultPath")
        sizePolicy.setHeightForWidth(self.btnSelectResultPath.sizePolicy().hasHeightForWidth())
        self.btnSelectResultPath.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.btnSelectResultPath)

        self.labelSaveTo = QLabel(self.centralwidget)
        self.labelSaveTo.setObjectName(u"labelSaveTo")
        sizePolicy2.setHeightForWidth(self.labelSaveTo.sizePolicy().hasHeightForWidth())
        self.labelSaveTo.setSizePolicy(sizePolicy2)
        self.labelSaveTo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.labelSaveTo)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.verticalLayout_7)

        self.textEditResultPath = QTextEdit(self.centralwidget)
        self.textEditResultPath.setObjectName(u"textEditResultPath")
        sizePolicy2.setHeightForWidth(self.textEditResultPath.sizePolicy().hasHeightForWidth())
        self.textEditResultPath.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEditResultPath)


        self.verticalLayout_8.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayoutSettings = QFormLayout()
        self.formLayoutSettings.setObjectName(u"formLayoutSettings")
        self.labelYear = QLabel(self.centralwidget)
        self.labelYear.setObjectName(u"labelYear")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelYear.sizePolicy().hasHeightForWidth())
        self.labelYear.setSizePolicy(sizePolicy3)

        self.formLayoutSettings.setWidget(0, QFormLayout.LabelRole, self.labelYear)

        self.spinBoxFileYear = QSpinBox(self.centralwidget)
        self.spinBoxFileYear.setObjectName(u"spinBoxFileYear")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spinBoxFileYear.sizePolicy().hasHeightForWidth())
        self.spinBoxFileYear.setSizePolicy(sizePolicy4)
        self.spinBoxFileYear.setMinimum(2000)
        self.spinBoxFileYear.setMaximum(3000)
        self.spinBoxFileYear.setValue(2025)

        self.formLayoutSettings.setWidget(0, QFormLayout.FieldRole, self.spinBoxFileYear)

        self.labelFileType = QLabel(self.centralwidget)
        self.labelFileType.setObjectName(u"labelFileType")
        sizePolicy3.setHeightForWidth(self.labelFileType.sizePolicy().hasHeightForWidth())
        self.labelFileType.setSizePolicy(sizePolicy3)

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
        sizePolicy2.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy2)
        self.labelError.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.labelError)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.mainBtns = QHBoxLayout()
        self.mainBtns.setSpacing(6)
        self.mainBtns.setObjectName(u"mainBtns")
        self.btnDoFormatToCSV = QPushButton(self.centralwidget)
        self.btnDoFormatToCSV.setObjectName(u"btnDoFormatToCSV")

        self.mainBtns.addWidget(self.btnDoFormatToCSV)

        self.btnIgnorList = QPushButton(self.centralwidget)
        self.btnIgnorList.setObjectName(u"btnIgnorList")

        self.mainBtns.addWidget(self.btnIgnorList)


        self.verticalLayout_8.addLayout(self.mainBtns)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.spinBoxFileYear, self.radioBtnFullFile)
        QWidget.setTabOrder(self.radioBtnFullFile, self.radioBtnULFile)
        QWidget.setTabOrder(self.radioBtnULFile, self.btnDoFormatToCSV)
        QWidget.setTabOrder(self.btnDoFormatToCSV, self.btnIgnorList)
        QWidget.setTabOrder(self.btnIgnorList, self.btnOpenFile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnOpenFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443...", None))
        self.btnSelectResultPath.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.labelSaveTo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432...", None))
        self.labelYear.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.labelFileType.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0444\u0430\u0439\u043b\u0430:", None))
        self.radioBtnFullFile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.radioBtnULFile.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.labelError.setText("")
        self.btnDoFormatToCSV.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnIgnorList.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043b\u0438\u0441\u0442\u044b...", None))
    # retranslateUi

