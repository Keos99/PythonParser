import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DataBase:

    def __init__(self):
        self.con = None
        self.cur = None
        pass

    def connectiontodb(self, dbname: str):
        try:
            self.con = psycopg2.connect(dbname=str(dbname), user='postgres', host='localhost', port='5433', password='superuser')
            self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cur = self.con.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def closconnectiontodb(self):
        self.cur.close()
        self.con.close()

    def createdatabase(self):
        try:
            self.cur.execute('''CREATE DATABASE reuters WITH 
                                OWNER = postgres
                                ENCODING = 'UTF8'
                                TABLESPACE = pg_default
                                CONNECTION LIMIT = -1;''')
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error creating database.')
            print(error)

    def createtable(self):
        try:
            self.cur.execute('''CREATE TABLE public.news
                                (
                                    id SERIAL,
                                    title text,
                                    description text,
                                    newslink text,
                                    pubdate text,
                                    PRIMARY KEY (id)
                                );''')
            self.con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error creating table.')
            print(error)

    def create(self, title: str, description: str, newslink: str, pubdate: str):
        try:
            sql = '''INSERT INTO public.news (
                    title, description, newslink, pubdate) VALUES (
                    %s::text, %s::text, %s::text, %s::text)
                     returning id;'''

            self.cur.execute(sql, (title, description, newslink, pubdate))
        except (Exception, psycopg2.DatabaseError) as error:
            print('Еrror adding data.')
            print(error)

    def readall(self):
        try:
            self.cur.execute("SELECT * FROM public.news")
            row = self.cur.fetchone()

            while row is not None:
                print(row)
                row = self.cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Еrror reading data.')
            print(error)

    def update(self, title: str, description: str, newslink: str, pubdate: str, id: int):
        try:
            sql = '''UPDATE public.news SET
                        title = %s::text, description = %s::text, 
                        newslink = %s::text, pubdate = %s::text 
                        WHERE
                        id = %s;'''

            self.cur.execute(sql, (title, description, newslink, pubdate, id))
        except (Exception, psycopg2.DatabaseError) as error:
            print('Еrror reading data.')
            print(error)

    def delete(self, rowid: int):
        try:
            self.cur.execute("DELETE FROM public.news WHERE id = %s", (rowid,))
        except (Exception, psycopg2.DatabaseError) as error:
            print('Еrror deleting data.')
            print(error)