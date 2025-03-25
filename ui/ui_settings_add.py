# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diplomUI_settings_add.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 640)
        Dialog.setMinimumSize(QSize(400, 640))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHeader = QLabel(Dialog)
        self.labelHeader.setObjectName(u"labelHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeader.sizePolicy().hasHeightForWidth())
        self.labelHeader.setSizePolicy(sizePolicy)
        self.labelHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelHeader)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.labelSheet = QLabel(Dialog)
        self.labelSheet.setObjectName(u"labelSheet")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelSheet)

        self.labelIlocRows = QLabel(Dialog)
        self.labelIlocRows.setObjectName(u"labelIlocRows")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelIlocRows)

        self.labelIlocColumns = QLabel(Dialog)
        self.labelIlocColumns.setObjectName(u"labelIlocColumns")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelIlocColumns)

        self.labelDropColumn = QLabel(Dialog)
        self.labelDropColumn.setObjectName(u"labelDropColumn")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelDropColumn)

        self.labelMIdLists = QLabel(Dialog)
        self.labelMIdLists.setObjectName(u"labelMIdLists")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelMIdLists)

        self.labelMIdNames = QLabel(Dialog)
        self.labelMIdNames.setObjectName(u"labelMIdNames")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelMIdNames)

        self.labelCsvPath = QLabel(Dialog)
        self.labelCsvPath.setObjectName(u"labelCsvPath")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelCsvPath)

        self.textEditIlocRows = QTextEdit(Dialog)
        self.textEditIlocRows.setObjectName(u"textEditIlocRows")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEditIlocRows)

        self.textEditIlocColumns = QTextEdit(Dialog)
        self.textEditIlocColumns.setObjectName(u"textEditIlocColumns")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textEditIlocColumns)

        self.textEditDropColumns = QTextEdit(Dialog)
        self.textEditDropColumns.setObjectName(u"textEditDropColumns")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEditDropColumns)

        self.textEditMIdLists = QTextEdit(Dialog)
        self.textEditMIdLists.setObjectName(u"textEditMIdLists")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.textEditMIdLists)

        self.textEditMIdNames = QTextEdit(Dialog)
        self.textEditMIdNames.setObjectName(u"textEditMIdNames")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEditMIdNames)

        self.lineEditSheet = QLineEdit(Dialog)
        self.lineEditSheet.setObjectName(u"lineEditSheet")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditSheet)

        self.lineEditCSVPath = QLineEdit(Dialog)
        self.lineEditCSVPath.setObjectName(u"lineEditCSVPath")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditCSVPath)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelHeader.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 \u043b\u0438\u0441\u0442", None))
        self.labelSheet.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 (Sheet)", None))
        self.labelIlocRows.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0430\u043d\u0438\u0446\u044b \u0441\u0442\u0440\u043e\u043a (iloc_rows)", None))
        self.labelIlocColumns.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0430\u043d\u0438\u0446\u044b \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 (iloc_columns)", None))
        self.labelDropColumn.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u0431\u0440\u0430\u0442\u044c \u0441\u0442\u043e\u043b\u0431\u0446\u044b... (drop_column)", None))
        self.labelMIdLists.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043a\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 (m_id_lists)", None))
        self.labelMIdNames.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043f\u0438\u0441\u043a\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 (m_id_nsmes)", None))
        self.labelCsvPath.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e csv \u0444\u0430\u0439\u043b\u0430 (csv_path)", None))
        self.textEditIlocRows.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u0442\u0440\u043e\u043a \u0447\u0435\u0440\u0435\u0437 Enter", None))
        self.textEditIlocColumns.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0447\u0435\u0440\u0435\u0437 Enter", None))
        self.textEditDropColumns.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0448\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0447\u0435\u0440\u0435\u0437 Enter", None))
        self.textEditMIdLists.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0440\u043e\u0432\u043d\u0438 \u043c\u0443\u043b\u044c\u0442\u0438\u0438\u043d\u0434\u0435\u043a\u0441\u0430, \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u044f \u043a\u0430\u0436\u0434\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u043d\u0430\u043a\u043e\u043c /, \u043a\u0430\u0436\u0434\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441 Enter", None))
        self.textEditMIdNames.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0441\u043f\u0438\u0441\u043a\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439. \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0439 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0443\u0440\u043e\u0432\u043d\u0435\u0439 \u043c\u0443\u043b\u044c\u0442\u0438\u0438\u043d\u0434\u0435\u043a\u0441\u0430 ", None))
        self.lineEditSheet.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 ex\u0441el \u0444\u0430\u0439\u043b\u0435", None))
        self.lineEditCSVPath.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 csv \u0444\u0430\u0439\u043b\u0430 \u0441 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u043c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

