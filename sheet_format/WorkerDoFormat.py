from PySide6.QtCore import QThread, Signal

from sheet_format.model_settings import Setting
from sheet_format.sheet_formating import BaseFormater


class WorkerDoFormat(QThread):
    signal = Signal(str, bool)

    def __init__(self, sheet_settings: [str, Setting], mode: BaseFormater, file_path: str, file_year: int,
                 save_path: str, ignore_sheet: set, insert_to_db: bool):
        super().__init__()
        self.sheet_settings = sheet_settings
        self.mode = mode
        self.file_path = file_path
        self.file_year = file_year
        self.save_path = save_path
        self.ignore_sheet = ignore_sheet
        self.insert_to_db = insert_to_db

    def run(self):
        self.signal.emit("Обработка...", True)
        try:
            self.mode.start_format(self.sheet_settings, self.file_path, self.file_year,
                                   self.save_path, self.ignore_sheet, self.insert_to_db)
            self.signal.emit("Готово!", False)
        except Exception as e:
            self.signal.emit("Форматирование не удалось!", False)
            print(e)