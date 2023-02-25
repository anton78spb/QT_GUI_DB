import sys


class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # clients = self.model.get_clients()
        clients = self.model.clients_table_model
        self.view.clients_update(clients)
        self.view.main_window.tab_clients.buttons_group.button_add.clicked.connect(self.add_client_clicked)

    def add_client_clicked(self):
        print('Presenter add_client_clicked')
        print(self.model.clients_table_model.rowCount())

    def run(self):
        sys.exit(self.view.exec())
