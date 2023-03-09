import requests
from bs4 import BeautifulSoup as BS


'============пагинация в mashina.kg=============='

BEKA_URL = 'https://www.mashina.kg/search/all/'

html = requests.get(BEKA_URL).text
soup = BS(html, 'lxml')

html = requests.get(BEKA_URL).text
soup = BS(html, 'lxml')
pagination = soup.find('ul', {'class':'pagination'})
last_li = pagination.find_all('li')[-1]
last_page = last_li.find('a').get('data-page')


'=========csv========'
import csv
data = [
    {'title':"hello", "price":32},
    {'title':"test", "price":34},
    {'title':"beko", "price":55},
    {'title':"blin", "price":22},
]

with open("test.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for product in data:
        writer.writerow(product.values())