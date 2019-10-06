from src.app.database import DataBase


class DbHandler:

    def __init__(self):
        self.db = DataBase()
        pass

    def db_init(self):
        self.db.connectiontodb('postgres')
        self.db.createdatabase()
        self.db.closconnectiontodb()
        self.db.connectiontodb('reuters')
        self.db.createtable()
        self.db.closconnectiontodb()

    def add_data(self, newsdata):
        self.db.connectiontodb('reuters')
        for data in newsdata:
            self.db.create(data['title'], data['description'], data['newslink'], data['pubdate'])
        self.db.closconnectiontodb()

    def show_all_data(self):
        self.db.connectiontodb('reuters')
        self.db.readall()
        self.db.closconnectiontodb()
