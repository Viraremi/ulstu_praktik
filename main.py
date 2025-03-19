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

    def get_mode(self):
        if self.ui.radioBtnFullFile.isChecked(): return True
        elif self.ui.radioBtnULFile.isChecked(): return False

    def format(self):
        sttgs.get_settings()
        with open("all_settings.json", "r", encoding="utf-8") as file:
            sheet_settings = json.load(file)
            print("Настройки форматирования получены!")

        frmt.start_format(
            sheet_settings,
            self.get_mode(),
            self.ui.labelSelectedFile.text(),
            self.ui.spinBoxFileYear.value()
        )

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "Файл (*.xlsx)"
        )
        if file_path:
            self.ui.labelSelectedFile.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CsvFormatter()
    window.show()

    sys.exit(app.exec())