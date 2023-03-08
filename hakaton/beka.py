# import json
# import requests

# from bs4 import BeautifulSoup as BS


# BASE_URL = 'https://mashina.kg'


# def get_soup(url:str) -> BS:
#     response = requests.get(url)
#     soup = BS(response.text, 'lxml')
#     return soup


# def get_product_info(product: BS) -> dict:
#     title = product.find('a', {'class':'table-view-list'}).text.strip()
#     price = product.find('div', {'class':'mm-item-card-price'}).text.strip().split('/n')[0]
#     image = product.find('img', {'class':'mm-item-card-img'}).find('img').get['src']
#     description = product.find('div', {'class':'mm-item-card-desc'}).text.strip()
#     return {'title':title, 'price':price, 'image':image, 'description':description}


# def get_all_products_from_page(url:str) ->list:
#     res = []
#     soup = get_soup(url)
#     products = soup.find_all('div', {'class':'mm-item-card'})
#     for product in products:
#         product_info = get_product_info(product)
#         res.append(product_info)
#     return res


# def write_to_json(data:dict):
#     with open('db.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False)


# def get_last_page(url:str) -> int:
#     soup = get_soup(url)
#     last = soup.find('li', {'class':'page-link'})
#     return int(last.text)


# def main():
#     category = '/moto'
#     data = {}
#     last_page = get_last_page(BASE_URL + category)
#     for page in range(1, last_page+1):
#         url = BASE_URL + category + '?page=' + str(page)
#         print(url)
#         one_page_data = get_all_products_from_page(url)
#         data[page] = one_page_data
#     write_to_json(data)



# main()



import requests
from bs4 import BeautifulSoup as BS
import csv

BASE_URL = 'https://www.mashina.kg'


def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup


def description_info(product:BS):
    engine=product.find('p',{'class':'body-type'}).text.strip()
    specifications=product.find('p',{'class':'volume'}).text.strip()
    age = product.find('p',{'class':'year-miles'}).text.strip()
    city =product.find('p',{'class':'city'}).text.strip().split("\n")[0]
    return f'Двигатель: {engine} Спецификации: {specifications} Год {age} Город: {city}'



def get_product_info(product:BS) -> dict:
    title = product.find('h2').text.strip()
    let =product.find('p').text.strip().split('\n')
    price = let[0]+'/'+let[-1].lstrip()
    image = product.find('img').get('data-src')
    description = description_info(product)
    list_data=[title,price, description, image]
    csv_beka(list_data)
    return list_data


def get_last_page(url)->int:
    soup = get_soup(url)
    pages = soup.find_all('li', {'class' : "page-item"})[-1].find('a').get('data-page')

    return int(pages)


def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div',{'class':'table-view-list'})
    products = box.find_all('div',{'class':'list-item'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)

    return res


def csv_beka(data):
    filename = 'car_data.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for i in data:
            writer.writerow([i])

def main():
    category = '/motosearch/all/'
    data = []
    last_page = get_last_page(BASE_URL+category)
    for page in range(1,last_page+1):
        url = (BASE_URL+category+'?page='+str(page))
        print(url)
        one_page_data=get_all_products_from_page(url)
        data.append(one_page_data)


main()