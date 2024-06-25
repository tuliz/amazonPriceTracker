from bs4 import BeautifulSoup
import requests
URL = 'https://www.amazon.com/-/he/dp/B0CL61F39H/ref=sr_1_1?crid=3L6GM9V7VEPQQ&dib=eyJ2IjoiMSJ9.AHjTd7ZFe8s8RHzX7QExwDesCneAdSrHHQ5Jj2D66rvF-pjGi8aIBEUBd2Es1eHM3WTiK9PkEloVhyt-Gwo_VaVSD8HWlrHw6lknKp9XIn8oft0hEMiDGCX3gYhF_YgGtnWCzQsgpDxSi3BgTP6xW0HpaqLX4Dsw1vV25Gvj4FPC8qXXkz44FlsvvxvaSa6AFy5wkHuNWqZHqfeT36vbd69SHq-P4RBWnvE2RnyMGLI.ieKx5HshoxJ3fcASVB0-MiAfluQT7N2YJ562ko-1apU&dib_tag=se&keywords=playstation%2B5&qid=1719339837&sprefix=plays%2Caps%2C335&sr=8-1&th=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6'
}

response = requests.get(URL,headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, 'html.parser')
product_price = float(soup.find(name='span', class_='a-price').getText().split('$')[1].split('\u200e')[1])