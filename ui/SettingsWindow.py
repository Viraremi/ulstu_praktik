import json

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QMessageBox

from sheet_format.model_settings import Setting
from sheet_format.sheet_settings import update_or_reset_settings, get_settings
from ui.qt_designer.py_ui_files.ui_settings import Ui_SettingsWindow
from ui.qt_designer.py_ui_files.ui_settings_add import Ui_Dialog as UIDialogAdd
from ui.qt_designer.py_ui_files.ui_settings_del import Ui_Dialog as UIDialogDel
from ui.JsonWindow import JsonViewer


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.ui.btnSettingsAdd.clicked.connect(self.btn_add)
        self.ui.btnSettingsDelete.clicked.connect(self.btn_delete)
        self.ui.btnSettingsShow.clicked.connect(self.btn_show)

        self.settings_list = get_settings()
        self.json_window = None

    def btn_add(self):
        self.add_window = QtWidgets.QDialog()
        self.add_window_ui = UIDialogAdd()
        self.add_window_ui.setupUi(self.add_window)
        self.add_window.show()
        self.add_window.setWindowTitle("Новый лист")
        self.add_window_ui.btnSave.clicked.connect(self.new_sheet_save)

    def btn_delete(self):
        self.del_window = QtWidgets.QDialog()
        self.del_window_ui = UIDialogDel()
        self.del_window_ui.setupUi(self.del_window)
        self.del_window.show()
        self.del_window.setWindowTitle("Удалить лист")
        self.del_window_ui.btnDeleteSelectedList.clicked.connect(self.delete_selected_sheet)

        self.del_window_ui.comboBoxSelectList.clear()
        self.del_window_ui.comboBoxSelectList.addItems(self.settings_list)

    def btn_show(self):
        try:
            with open("all_settings.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.json_window = JsonViewer(data)
            self.json_window.show()
        except FileNotFoundError as e:
            QMessageBox.information(self, "Настроек нет", "Нет заданных настроек")


    def new_sheet_save(self):
        new_sheet = Setting(
            sheet=self.add_window_ui.lineEditSheet.text(),
            iloc_rows=[int(item) for item in self.add_window_ui.textEditIlocRows.toPlainText().split('\n')],
            iloc_columns=[int(item) for item in self.add_window_ui.textEditIlocColumns.toPlainText().split('\n')],
            drop_column=[int(item) for item in self.add_window_ui.textEditDropColumns.toPlainText().split('\n')],
            m_id_lists=[_.split('\n') for _ in self.add_window_ui.textEditMIdLists.toPlainText().split('\n\n')],
            m_id_names=[_ for _ in self.add_window_ui.textEditMIdNames.toPlainText().split('\n')],
            csv_path=self.add_window_ui.lineEditCSVPath.text()
        )
        self.settings_list[new_sheet.sheet] = new_sheet
        update_or_reset_settings(self.settings_list)
        QMessageBox.information(self, "Готово!", f"Лист \"{new_sheet.sheet}\" создан")
        self.add_window.close()

    def delete_selected_sheet(self):
        selected_sheet = self.del_window_ui.comboBoxSelectList.currentText()
        self.settings_list.pop(selected_sheet)
        update_or_reset_settings(self.settings_list)
        QMessageBox.information(self, "Готово!", f"Лист \"{selected_sheet}\" удален")
        self.del_window.close()
