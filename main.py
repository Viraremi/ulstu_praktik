import sys
import json
import sheet_settings as sttgs
import sheet_formating as frmt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.ui_main import Ui_MainWindow
from datetime import datetime

class CsvFormatter(QMainWindow):
    def __init__(self):
        super(CsvFormatter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioBtnFullFile.setChecked(True)
        self.ui.spinBoxFileYear.setValue(datetime.now().year)

        self.ui.btnDoFormatToCSV.clicked.connect(self.format)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnSelectResultPath.clicked.connect(self.select_result_path)

    def get_mode(self):
        if self.ui.radioBtnFullFile.isChecked(): return True
        elif self.ui.radioBtnULFile.isChecked(): return False

    def format(self):
        self.ui.btnDoFormatToCSV.setDisabled(True)
        self.ui.labelError.setText("Обработка...")

        sttgs.generate()
        with open("all_settings.json", "r", encoding="utf-8") as file:
            sheet_settings = json.load(file)
            print("Настройки форматирования получены!")

        frmt.start_format(
            sheet_settings,
            self.get_mode(),
            self.ui.textEditSelectedFilePath.toPlainText(),
            self.ui.spinBoxFileYear.value(),
            self.ui.textEditResultPath.toPlainText()
        )

        self.show_msg_done()

    def show_msg_done(self):
        self.ui.btnDoFormatToCSV.setDisabled(False)
        self.ui.labelError.setText("Готово!")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Файл (*.xlsx)")
        if file_path: self.ui.textEditSelectedFilePath.setText(file_path)

    def select_result_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder_path: self.ui.textEditResultPath.setText(folder_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CsvFormatter()
    window.show()

    sys.exit(app.exec())