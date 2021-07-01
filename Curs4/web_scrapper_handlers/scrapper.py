import requests
from bs4 import BeautifulSoup


def get_page_html(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')
    return soup


def get_table_rows(page):
    table = page.find('table', {'id': 'serverlist'})
    table_rows = [row for row in table.findAll('tr') if row.get('class')]
    return table_rows
