import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
name = soup.find_all('a', class_='title')
description = soup.find_all('p', class_='description')
price = soup.find_all('h4', class_='pull-right price')
reviews = soup.find_all('p', class_='pull-right')
price1 = soup.find('h4', class_='pull-right price')
# print(name, description, price, reviews)
# print(price1.text)
if len(name) == len(description) == len(price) == len(reviews):
    product_name_list = []
    product_price_list = []
    product_revies_list = []
    product_description_list = []
    for i in range(len(name)):
        name_prod = name[i].text
        price_prod = price[i].text
        description_prod = description[i].text
        review_prod = reviews[i].text
        product_name_list.append(name_prod)
        product_price_list.append(price_prod)
        product_description_list.append(description_prod)
        product_revies_list.append(review_prod)
    # print(product_name_list, product_price_list, product_description_list)
else:
    print('not OK')


dtframe = pd.DataFrame({'Product Name':product_name_list,
 'Price': product_price_list,
 'Reviews': product_revies_list,
 'Description': product_description_list})
print(dtframe)