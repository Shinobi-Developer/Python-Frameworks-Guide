from bs4 import BeautifulSoup
from flask import Flask
from selenium import webdriver
import pandas as pd

app = Flask(__name__)
driver = webdriver.Chrome()
driver.get('https://www.bestofelectricals.com/consumables')

@app.route('/')
def scrapping():
    
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    unit = soup.find('div', class_='item-grid')
    items = unit.find_all(class_='item-box')
    
    names = []
    descriptions = []
    old_prices = []
    current_prices = []
    
    for item in items:
        description = item.find('div', class_='description')
        old_price = item.find('span', class_='price old-price')
        current_price = item.find('span', class_='price actual-price')
        names.append(item.h2.text)
        descriptions.append(description.text if description != None else '')
        old_prices.append(old_price.text if old_price != None else '')
        current_prices.append(current_price.text)
        
    name_series = pd.Series(names, name='Name')
    description_series = pd.Series(descriptions, name='Description')
    old_price_series = pd.Series(old_prices, name='Old Price')
    current_price_series = pd.Series(current_prices, name='Current Price')
    
    dataframe = pd.DataFrame({ 'Names': name_series, 'Descriptions': description_series, 'Old Prices': old_price_series, 'Current Prices': current_price_series })
    dataframe.to_excel('products.xlsx', index=False)
    
    return 'Success'