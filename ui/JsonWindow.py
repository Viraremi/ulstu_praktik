from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QTreeView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem


class JsonViewer(QMainWindow):
    def __init__(self, json_data):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.resize(400, 300)
        self.setMinimumSize(QSize(400, 300))

        # Основной виджет и layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Дерево и модель
        self.tree_view = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Key', 'Value'])

        self.tree_view.setModel(self.model)
        layout.addWidget(self.tree_view)

        self.setCentralWidget(central_widget)

        # Заполнение модели JSON-данными
        self.load_json(json_data)

    def load_json(self, data, parent=None):
        if parent is None:
            parent = self.model.invisibleRootItem()

        if isinstance(data, dict):
            for key, value in data.items():
                key_item = QStandardItem(str(key))
                if isinstance(value, (dict, list)):
                    value_item = QStandardItem('')
                    self.load_json(value, key_item)
                else:
                    value_item = QStandardItem(str(value))
                parent.appendRow([key_item, value_item])
        elif isinstance(data, list):
            for index, item in enumerate(data):
                key_item = QStandardItem(f"[{index}]")
                if isinstance(item, (dict, list)):
                    value_item = QStandardItem('')
                    self.load_json(item, key_item)
                else:
                    value_item = QStandardItem(str(item))
                parent.appendRow([key_item, value_item])
