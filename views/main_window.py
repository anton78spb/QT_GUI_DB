# from __future__ import annotations

from PyQt6.QtWidgets import (QWidget, QTabWidget, QHBoxLayout, QPushButton, QVBoxLayout, QListWidget, QTableView,
                             QAbstractItemView, QDialog, QDialogButtonBox, QLabel, QLineEdit, QFormLayout, QInputDialog)
# from main import presenter


class AddClientDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.name_label = QLabel("Имя")
        self.name_edit = QLineEdit()

        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.name_label, self.name_edit)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self._layout = QVBoxLayout(self)
        self._layout.addLayout(self.form_layout)
        self._layout.addWidget(self.button_box)

    def accept(self) -> None:
        super().accept()
        print('ACCEPT.')

    def exec(self):
        # self.name_edit.setText('111')
        return super().exec(), self.name_edit.text()


class TableView(QTableView):
    def __init__(self):
        super().__init__()
        self.verticalHeader().hide()
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


class ClientsTabButtons(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.button_add = QPushButton("Add Client")
        self.button_edit = QPushButton("Edit Client")
        self.button_delete = QPushButton("Delete Client")
        self.button_fake = QPushButton("Fake Client")

        self.addWidget(self.button_add)
        self.addWidget(self.button_edit)
        self.addWidget(self.button_delete)
        self.addStretch()
        self.addWidget(self.button_fake)

        # self.button_add.clicked.connect(self.add_clicked)
        print(self.parent())
        print(self.parentWidget())

    def add_clicked(self):
        add_dialog = AddClientDialog()
        status, name = add_dialog.exec()
        if status and name.strip():
            pass
        print(status, name)
        print(add_dialog.name_edit.text())


class Clients(QWidget):
    def __init__(self):
        super().__init__()
        # self.clients_list = QTableWidget()

        self.clients_list = TableView()
        # self.clients_list = QTableView()
        # self.clients_list.verticalHeader().hide()
        # self.clients_list.horizontalHeader().setHighlightSections(False)
        # self.clients_list.horizontalHeader().setStretchLastSection(True)
        # self.clients_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # self.clients_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        # self.clients_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.buttons_group = ClientsTabButtons()

        self._layout = QHBoxLayout(self)
        self._layout.addWidget(self.clients_list)
        self._layout.addLayout(self.buttons_group)
        # self.setLayout(self._layout)

    # def add_clicked(self):
    #     add_dialog = AddClientDialog()
    #     status, name = add_dialog.exec()
    #     if status:
    #         pass
    #     print(status, name)
    #     print(add_dialog.name_edit.text())


class ProductsTabButtons(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.button_add = QPushButton("Add Product")
        self.button_edit = QPushButton("Edit Product")
        self.button_delete = QPushButton("Delete Product")
        self.button_fake = QPushButton("Fake Product")

        self.addWidget(self.button_add)
        self.addWidget(self.button_edit)
        self.addWidget(self.button_delete)
        self.addStretch()
        self.addWidget(self.button_fake)


class Products(QWidget):
    def __init__(self):
        super().__init__()
        self.products_list = QListWidget()
        self.buttons_group = ProductsTabButtons()

        self._layout = QHBoxLayout(self)
        self._layout.addWidget(self.products_list)
        self._layout.addLayout(self.buttons_group)
        # self.setLayout(self._layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI DB TEST")

        self.tabs = QTabWidget()
        self.tab_clients = Clients()
        self.tab_products = Products()
        self.tabs.addTab(self.tab_clients, "Clients")
        self.tabs.addTab(self.tab_products, "Products")

        self._layout = QHBoxLayout(self)
        self._layout.addWidget(self.tabs)
