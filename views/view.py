from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from views.main_window import MainWindow


class View(QApplication):
    def __init__(self):
        super().__init__([])
        self.setFont(QFont("system-ui", 16))
        self.main_window = MainWindow()
        self.main_window.show()

    def clients_update(self, model):
        self.main_window.tab_clients.clients_list.setModel(model)
        print(self.main_window.tab_clients.clients_list.model().rowCount())

        # self.main_window.tab_clients.clients_list.addItems(['111', '222'])
        # self.main_window.tab_clients.clients_list.setRowCount(5)
        # self.main_window.tab_clients.clients_list.setColumnCount(2)
        # self.main_window.tab_clients.clients_list.setHorizontalHeaderLabels(['id', 'Client'])
        # self.main_window.tab_clients.clients_list.verticalHeader().hide()
