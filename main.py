from bs4 import BeautifulSoup
import requests
import pandas
import smtplib
TARGET_PRICE = 450
USER = ''
PASSWORD = ''
EMAIL = ''

products_dataframe = pandas.read_csv('products.csv')
products_dict = products_dataframe.to_dict(orient='records')

headers = {
    'User-Agent': 'Mozilla/5.0 ',
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6'
}

for product in products_dict:

    response = requests.get(product['product_url'],headers=headers)
    response.raise_for_status()
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')
    product_title = soup.find(name='span', id='productTitle').getText()
    product_price = float(soup.find(name='span', class_='a-price').getText().split('$')[1].split('\u200e')[1])
    product_target_price = product['target_price']
    product_url = product['product_url']
    if product_price < product_target_price:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(USER,PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f'the product {product_title} is now at a price of ${product_target_price}\n{product_url}')
