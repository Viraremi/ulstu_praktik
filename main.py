import sys
import json
import sheet_settings as sttgs
import sheet_formating as frmt
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
from datetime import datetime

class CsvFormatter(QMainWindow):
    def __init__(self):
        super(CsvFormatter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioBtnFullFile.setChecked(True)
        self.ui.spinBoxFileYear.setValue(datetime.now().year)

        self.ui.btnDoFormatToCSV.clicked.connect(self.test)

    def testui(self):
        if self.ui.radioBtnFullFile.isChecked(): return "full"
        elif self.ui.radioBtnULFile.isChecked(): return "ul"

    def test(self):
        self.ui.labelSelectedFile.setText(self.testui() + str(self.ui.spinBoxFileYear.value()))

    def format(self):
        # Читаем настройки форматирования из файла
        sttgs.get_settings()
        with open("all_settings.json", "r", encoding="utf-8") as file:
            sheet_settings = json.load(file)
            print("Настройки форматирования получены!")

        frmt.start_format(sheet_settings, True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CsvFormatter()
    window.show()

    sys.exit(app.exec())