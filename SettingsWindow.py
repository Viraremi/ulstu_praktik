from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from ui.py_ui_files.ui_settings import Ui_SettingsWindow
from ui.py_ui_files.ui_settings_add import Ui_Dialog as ui_settings_add_dialog
from ui.py_ui_files.ui_settings_del import Ui_Dialog as ui_settings_del_dialog
from ui.py_ui_files.ui_settings_show import Ui_Dialog as ui_settings_show_dialog

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.ui.btnSettingsAdd.clicked.connect(self.btn_add)
        self.ui.btnSettingsDelete.clicked.connect(self.btn_delete)
        self.ui.btnSettingsShow.clicked.connect(self.btn_show)

    def btn_add(self):
        self.new_window = QtWidgets.QDialog()
        self.new_window_ui = ui_settings_add_dialog()
        self.new_window_ui.setupUi(self.new_window)
        self.new_window_ui.btnSave.clicked.connect(self.new_settings_save)
        self.new_window.show()

    def btn_delete(self):
        self.new_window = QtWidgets.QDialog()
        self.new_window_ui = ui_settings_del_dialog()
        self.new_window_ui.setupUi(self.new_window)
        self.new_window_ui.btnDeleteSelectedList.clicked.connect(self.delete_selected_sheed)
        self.new_window.show()

    def btn_show(self):
        self.new_window = QtWidgets.QDialog()
        self.new_window_ui = ui_settings_show_dialog()
        self.new_window_ui.setupUi(self.new_window)
        #TODO (self.new_window_ui.textEditShowSettings.setText())
        self.new_window.show()

    def new_settings_save(self):
        #TODO
        self.new_window.close()
        return

    def delete_selected_sheed(self):
        # TODO
        self.new_window.close()
        return