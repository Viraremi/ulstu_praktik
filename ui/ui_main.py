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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QSize(400, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fileLoad = QHBoxLayout()
        self.fileLoad.setObjectName(u"fileLoad")
        self.btnOpenFile = QPushButton(self.centralwidget)
        self.btnOpenFile.setObjectName(u"btnOpenFile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenFile.sizePolicy().hasHeightForWidth())
        self.btnOpenFile.setSizePolicy(sizePolicy)

        self.fileLoad.addWidget(self.btnOpenFile)

        self.labelSelectedFile = QLabel(self.centralwidget)
        self.labelSelectedFile.setObjectName(u"labelSelectedFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelSelectedFile.sizePolicy().hasHeightForWidth())
        self.labelSelectedFile.setSizePolicy(sizePolicy1)
        self.labelSelectedFile.setFrameShape(QFrame.NoFrame)
        self.labelSelectedFile.setFrameShadow(QFrame.Plain)
        self.labelSelectedFile.setLineWidth(1)
        self.labelSelectedFile.setMidLineWidth(0)
        self.labelSelectedFile.setTextFormat(Qt.PlainText)
        self.labelSelectedFile.setAlignment(Qt.AlignCenter)

        self.fileLoad.addWidget(self.labelSelectedFile)


        self.verticalLayout_2.addLayout(self.fileLoad)

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

        self.verticalLayout.addWidget(self.radioBtnFullFile)

        self.radioBtnULFile = QRadioButton(self.centralwidget)
        self.radioBtnULFile.setObjectName(u"radioBtnULFile")

        self.verticalLayout.addWidget(self.radioBtnULFile)


        self.formLayoutSettings.setLayout(1, QFormLayout.FieldRole, self.verticalLayout)


        self.verticalLayout_2.addLayout(self.formLayoutSettings)

        self.mainBtns = QHBoxLayout()
        self.mainBtns.setSpacing(6)
        self.mainBtns.setObjectName(u"mainBtns")
        self.btnDoFormatToCSV = QPushButton(self.centralwidget)
        self.btnDoFormatToCSV.setObjectName(u"btnDoFormatToCSV")

        self.mainBtns.addWidget(self.btnDoFormatToCSV)

        self.btnIgnorList = QPushButton(self.centralwidget)
        self.btnIgnorList.setObjectName(u"btnIgnorList")

        self.mainBtns.addWidget(self.btnIgnorList)


        self.verticalLayout_2.addLayout(self.mainBtns)

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
        self.btnOpenFile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
        self.labelSelectedFile.setText(QCoreApplication.translate("MainWindow", u"[\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b]", None))
        self.labelYear.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.labelFileType.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0444\u0430\u0439\u043b\u0430:", None))
        self.radioBtnFullFile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.radioBtnULFile.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.btnDoFormatToCSV.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnIgnorList.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043b\u0438\u0441\u0442\u044b...", None))
    # retranslateUi

