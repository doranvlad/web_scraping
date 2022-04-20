import requests
from bs4 import BeautifulSoup as Bs
import lxml
import csv
import re


r = requests.get('https://www.aks.ua/catalog/displei-ekrany/page/1')
html = Bs(r.content, 'lxml')
last_page = int(html.find('li', class_='next').find_previous().text)
print(last_page)

with open('eggs.csv', 'w', encoding='utf-8'):
    pass
g
for i in range(last_page + 1):
    r = requests.get(f'https://www.aks.ua/catalog/displei-ekrany/page/{i}')
    html = Bs(r.content, 'lxml')
    tovar = html.find_all('div', class_='catalog-item-box')
    for t in tovar:
        name = t.find('div', class_='catalog-name').text.strip()
        if t.find('div', class_='catalog-item-id catalog-bottom active old-price') is None:
            code = t.find('div', class_='catalog-item-id catalog-bottom active').text.strip()
            code = re.findall(r'\d+', code)[0]
        else:
            code = t.find('div', class_='catalog-item-id catalog-bottom active old-price').text.strip()
            code = re.findall(r'\d+', code)[0]

        href = 'https://www.aks.ua' + t.find('a').get('href').strip()
        price = t.find('div', class_='catalog-price-new').text.strip()
        price = re.findall(r'\d+', price)[0]

        with open('eggs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([name, code, price, href])
