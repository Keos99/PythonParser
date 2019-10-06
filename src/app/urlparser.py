import requests
import re
import csv
from bs4 import BeautifulSoup


class UrlParser:

    def __init__(self):
        self.reutersdata = []
        pass

    def get_reutersdata(self):
        return self.reutersdata

    def get_html(self, url: str):
        r = requests.get(url)
        return r.text

    def write_csv(self, data):
        with open('reuters.csv', 'a') as t:
            writer = csv.writer(t)

            writer.writerow((
                data['title'],
                data['description'],
                data['newslink'],
                data['pubdate']))

    def get_news_data(self, html: str):
        soup = BeautifulSoup(html, features="html.parser")
        items = soup.find_all('item')
        for item in items:
            try:
                title = item.find('title').text
            except:
                title = 'none'

            try:
                temp_description = item.find('description')
                description = str(re.findall(r'<description>(.*?)&lt;div', str(temp_description))).strip('[').strip(']')
            except:
                description = 'none'

            try:
                newslink = str(re.findall(r'<link\/>(.*?)\s*<guid', str(item))).strip('[').strip(']')
            except:
                newslink = 'none'

            try:
                pubdate = item.find('pubdate').text
            except:
                pubdate = 'none'

            data = {
                'title': title,
                'description': description,
                'newslink': newslink,
                'pubdate': pubdate}

            self.reutersdata.append(data)
            self.write_csv(data)
