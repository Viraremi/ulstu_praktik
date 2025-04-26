import json
import shutil
import sys
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from config_project import Const
from database.connection import DBConnection
from SettingsWindow import SettingsWindow
from sheet_format.model_settings import Setting
from sheet_format.sheet_formating import UlskFormater, FullFormater, BaseFormater
from sheet_format.sheet_settings import get_settings
from ui.py_ui_files.ui_main import Ui_MainWindow
from ui.py_ui_files.ui_settings_ignore import Ui_Dialog


class WorkerDoFormat(QThread):
    signal = Signal(str, bool)

    def __init__(self, sheet_settings: [str, Setting], mode: BaseFormater, file_path: str, file_year: int,
                 save_path: str, ignore_sheet: set):
        super().__init__()
        self.sheet_settings = sheet_settings
        self.mode = mode
        self.file_path = file_path
        self.file_year = file_year
        self.save_path = save_path
        self.ignore_sheet = ignore_sheet

    def run(self):
        self.signal.emit("Обработка...", True)
        try:
            self.mode.start_format(self.sheet_settings, self.file_path, self.file_year,
                                   self.save_path, self.ignore_sheet)
            self.signal.emit("Готово!", False)
        except Exception as e:
            self.signal.emit("Форматирование не удалось!", False)
            print(e)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db_conn = DBConnection()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioBtnFullFile.setChecked(True)
        self.ui.spinBoxFileYear.setValue(datetime.now().year)

        self.ui.btnDoFormatToCSV.clicked.connect(self.start_format_async)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnSelectResultPath.clicked.connect(self.select_result_path)
        self.ui.actionSettingsListIgnore.triggered.connect(self.open_window_settings_ignore)
        self.ui.actionOpenSheetSettingsWindow.triggered.connect(self.open_window_settings)
        self.ui.actionImport.triggered.connect(self.import_settings)
        self.ui.actionExport.triggered.connect(self.export_settings)
        self.ui.actionGetSQL.triggered.connect(self.get_sql_script)

        self.window_settings = None
        self.ignore_list = set()

    def get_mode(self) -> BaseFormater:
        if self.ui.radioBtnFullFile.isChecked():
            return FullFormater()
        elif self.ui.radioBtnULFile.isChecked():
            return UlskFormater()
        raise ValueError('Ни один чек бокс не выбран')

    def start_format_async(self):
        self.worker = WorkerDoFormat(
            get_settings(),
            self.get_mode(),
            self.ui.textEditSelectedFilePath.toPlainText(),
            self.ui.spinBoxFileYear.value(),
            self.ui.textEditResultPath.toPlainText(),
            self.ignore_list)
        self.worker.signal.connect(self.update_status_label)
        self.worker.start()

    def update_status_label(self, text, btn_disabled):
        self.ui.btnDoFormatToCSV.setDisabled(btn_disabled)
        self.ui.labelStatus.setText(text)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Файл (*.xlsx)")
        self.ui.textEditSelectedFilePath.setText(file_path) if file_path else None

    def select_result_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.textEditResultPath.setText(folder_path) if folder_path else None

    def open_window_settings_ignore(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_settings = Ui_Dialog()
        self.ui_settings.setupUi(self.new_window)
        self.new_window.setWindowTitle("Игнорируемые листы")
        self.new_window.show()
        self.ui_settings.btnSaveSelect.clicked.connect(self.save_ignore_list)

        self.ui_settings.listWidgetSheetsList.clear()
        self.ui_settings.listWidgetSheetsList.addItems(get_settings())

    def save_ignore_list(self):
        selected_items = self.ui_settings.listWidgetSheetsList.selectedItems()
        self.ignore_list = {item.text() for item in selected_items}
        QMessageBox.information(self, "Готово!", "Игнорирование задано")
        self.new_window.close()

    def open_window_settings(self):
        if self.window_settings is None or not self.window_settings.isVisible():
            self.window_settings = SettingsWindow()
            self.window_settings.show()

    def import_settings(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    json.load(f)
                shutil.copy(file_path, Const.SETTINGS_FILE)
                QMessageBox.information(self, "Успех", "Настройки успешно импортированы!")
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Ошибка", "Выбранный файл не является корректным JSON!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при импорте файла: {e}")

    def export_settings(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Экспортировать", "", "JSON Files (*.json)")
        if file_path:
            shutil.copy(Const.SETTINGS_FILE, file_path)
            QMessageBox.information(self, "Успех", "Файл настроек успешно экспортирован!")

    def get_sql_script(self):
        self.db_conn.test()
        # TODO(get_sql_script)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
