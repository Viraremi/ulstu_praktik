import json
import shutil
import sys
from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from SettingsWindow import SettingsWindow
from ui.py_ui_files.ui_main import Ui_MainWindow
from ui.py_ui_files.ui_settings_ignore import Ui_Dialog as ui_settings_ignore_dialog
from sheet_format import sheet_settings as format_settings, sheet_formating as format_do
SETTINGS_FILE = "all_settings.json"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioBtnFullFile.setChecked(True)
        self.ui.spinBoxFileYear.setValue(datetime.now().year)

        self.ui.btnDoFormatToCSV.clicked.connect(self.do_format)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnSelectResultPath.clicked.connect(self.select_result_path)
        self.ui.actionSettingsListIgnore.triggered.connect(self.open_window_settings_ignore)
        self.ui.actionOpenSheetSettingsWindow.triggered.connect(self.open_window_settings)
        self.ui.actionImport.triggered.connect(self.import_settings)
        self.ui.actionExport.triggered.connect(self.export_settings)

        self.window_settings = None
        self.ignore_list = []

    def get_mode(self):
        if self.ui.radioBtnFullFile.isChecked(): return True
        elif self.ui.radioBtnULFile.isChecked(): return False

    def do_format(self):
        self.ui.btnDoFormatToCSV.setDisabled(True)
        self.ui.labelError.setText("Обработка...")


        # try:
        # TODO(здесь нужна асинхронность)
        # except Exception as e:
        #     self.ui.btnDoFormatToCSV.setDisabled(False)
        #     self.ui.labelError.setText("Ошибка! Форматирование не удалось!")
        #     return

        format_do.start_format(
            format_settings.get_settings(),
            self.get_mode(),
            self.ui.textEditSelectedFilePath.toPlainText(),
            self.ui.spinBoxFileYear.value(),
            self.ui.textEditResultPath.toPlainText(),
            self.ignore_list
        )

        self.ui.btnDoFormatToCSV.setDisabled(False)
        self.ui.labelError.setText("Готово!")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Файл (*.xlsx)")
        if file_path: self.ui.textEditSelectedFilePath.setText(file_path)

    def select_result_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder_path: self.ui.textEditResultPath.setText(folder_path)

    def open_window_settings_ignore(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_settings = ui_settings_ignore_dialog()
        self.ui_settings.setupUi(self.new_window)
        self.new_window.show()
        self.ui_settings.btnSaveSelect.clicked.connect(self.save_ignore_list)

        self.ui_settings.listWidgetSheetsList.clear()
        self.ui_settings.listWidgetSheetsList.addItems(format_settings.get_settings())

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
                shutil.copy(file_path, SETTINGS_FILE)
                QMessageBox.information(self, "Успех", "Настройки успешно импортированы!")
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Ошибка", "Выбранный файл не является корректным JSON!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при импорте файла: {e}")

    def export_settings(self):
        file_path, _ = QFileDialog.getSaveFileName(self,  "Экспортировать", "", "JSON Files (*.json)")
        if file_path:
            shutil.copy(SETTINGS_FILE, file_path)
            QMessageBox.information(self, "Успех", "Файл настроек успешно экспортирован!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())