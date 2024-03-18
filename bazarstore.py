from selenium import webdriver
from csv import writer
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\Leman\Documents\scraping\chromedriver")
driver.get('https://bazarstore.az/search?controller=search&s=berqa')

with open('bazarstore.csv','w',encoding='utf-8') as bazarstore_csv:
    berqa = writer(bazarstore_csv)
    berqa.writerow(['Name','Price'])
    mehsullar = driver.find_elements(By.CLASS_NAME, 'bs-product-row')
    for mehsul in mehsullar:
        name = mehsul.find_element(By.CLASS_NAME, 'product-title').text.split(' ')
        price = mehsul.find_element(By.CLASS_NAME, 'pp_price_with_text').text.split(' ')
        berqa.writerow([name,price])


        


