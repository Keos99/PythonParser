from src.app.dbhandler import DbHandler
from src.app.mainview import MainView
from src.app.urlparser import UrlParser


class MainController:

    def __init__(self):
        self.dbhandler = DbHandler()
        self.parser = UrlParser()
        self.view = MainView()
        self.base_url = 'http://feeds.reuters.com/reuters/topNews'
        pass

    def start(self):
        while True:
            self.view.menu()
            userchoise = input()
            if (userchoise == '5'):
                break
            self.menu_options(userchoise)

    def menu_options(self, number: str):
        if (number == '1'):
            self.dbhandler.db_init()
        elif (number == '2'):
            page = self.parser.get_html(self.base_url)
            self.parser.get_news_data(page)
        elif (number == '3'):
            self.dbhandler.add_data(self.parser.get_reutersdata())
        elif (number == '4'):
            self.dbhandler.show_all_data()
        else:
            print('Повторите ввод')
