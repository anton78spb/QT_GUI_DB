from datetime import datetime
from pony.orm import Database, PrimaryKey, Required, Set, set_sql_debug, db_session, select
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtCore import Qt

db = Database()


class Client(db.Entity):
    _table_ = 'clients'
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    orders = Set('Order')


class Product(db.Entity):
    _table_ = 'products'
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    price = Required(int, unsigned=True)
    sub_orders = Set('SubOrder')


class Order(db.Entity):
    _table_ = 'orders'
    id = PrimaryKey(int, auto=True)
    creation_time = Required(datetime, default=lambda: datetime.now())
    client = Required(Client)
    sub_orders = Set('SubOrder')


class SubOrder(db.Entity):
    _table_ = 'sub_orders'
    id = PrimaryKey(int, auto=True)
    product = Required(Product)
    count = Required(int, default=0, unsigned=True)
    order = Required(Order)


class Model:
    def __init__(self):
        set_sql_debug(True)
        db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
        db.generate_mapping(create_tables=True)

    @db_session
    def get_clients(self):
        clients = select(client for client in Client)
        return clients


class ClientTableModel(QSqlTableModel):
    def __init__(self):
        super().__init__()
        self.setTable('clients')
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Имя")
        self.select()


class ModelQT:
    def __init__(self):
        connection = QSqlDatabase.addDatabase('QSQLITE')
        connection.setDatabaseName('database.sqlite')
        connection.open()

        self.clients_table_model = ClientTableModel()
        # self.clients_table_model = QSqlTableModel()
        # self.clients_table_model.setTable('clients')
        # self.clients_table_model.select()
        # self.clients_table_model.setHeaderData(1, Qt.Orientation.Horizontal, "Имя")

    def get_clients(self):
        return self.clients_table_model


if __name__ == '__main__':
    set_sql_debug(True)
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
