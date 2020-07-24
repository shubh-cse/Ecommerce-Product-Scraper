# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:55:18 2020

@author: Shubh Gupta
"""

#importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
from prettytable import PrettyTable

#flipkart product page
prod1 = 'https://www.flipkart.com/apple-iphone-11-green-64-gb/p/itmfdb5266c6e904?pid=MOBFKCTSKZQCYCWE&lid=LSTMOBFKCTSKZQCYCWEMDZQMV&marketplace=FLIPKART&srno=s_1_18&otracker=search&otracker1=search&fm=SEARCH&iid=231e4b94-2eae-45de-ae80-8c7b86edef94.MOBFKCTSKZQCYCWE.SEARCH&ppt=sp&ppn=sp&ssid=1ddvge1s400000001595599700484&qH=24e991083bcf4f55'
prod2 = 'https://www.flipkart.com/samsung-galaxy-a80-phantom-black-128-gb/p/itmfghz3gneezbyh?pid=MOBFGHZ2CHC2SYSA&marketplace=FLIPKART'
prod3 = 'https://www.flipkart.com/apple-iphone-se-red-128-gb/p/itm55d4e3652bd92?pid=MOBFRFXHNB5ED82D&lid=LSTMOBFRFXHNB5ED82DP6ZOLW&marketplace=FLIPKART&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&fm=SEARCH&iid=3c5bd4e4-d3ca-404c-b301-516b1982df79.MOBFRFXHNB5ED82D.SEARCH&ppt=sp&ppn=sp&ssid=x9whi0a5fk0000001595599048545&qH=0b3f45b266a97d70'
prod4 = 'https://www.flipkart.com/samsung-galaxy-s10-lite-prism-blue-128-gb/p/itm10bfdc05a4bda?pid=MOBFZ8HTYDB5RDZF&lid=LSTMOBFZ8HTYDB5RDZFQGSJLO&marketplace=FLIPKART&srno=s_1_8&otracker=search&otracker1=search&fm=SEARCH&iid=4070b039-3966-4272-9df2-13f957e43014.MOBFZ8HTYDB5RDZF.SEARCH&ppt=sp&ppn=sp&ssid=99wq3b4rcg0000001595599093187&qH=8fbbd6d263c5426c'
prod5 = 'https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART&srno=s_1_9&otracker=search&otracker1=search&fm=SEARCH&iid=231e4b94-2eae-45de-ae80-8c7b86edef94.MOBFKCTSVZAXUHGR.SEARCH&ppt=sp&ppn=sp&ssid=1ddvge1s400000001595599700484&qH=24e991083bcf4f55'

#creating a web driver for chrome
wait_time = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
driver = webdriver.Chrome(r'chromedriver.exe',options=CO)

#product1
driver.get(prod1)
driver.implicitly_wait(wait_time)
prod_price = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]')
prod_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]")
prod_rating = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]")
name1 = prod_name.text
price1 = prod_price.text
rating1 = prod_rating.text

#product2
driver.get(prod2)
driver.implicitly_wait(wait_time)
prod_price = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
prod_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]")
prod_rating = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]")
name2 = prod_name.text
price2 = prod_price.text
rating2 = prod_rating.text

#product3
driver.get(prod3)
driver.implicitly_wait(wait_time)
prod_price = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
prod_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]")
prod_rating = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]")
name3 = prod_name.text
price3 = prod_price.text
rating3 = prod_rating.text

#product4
driver.get(prod4)
driver.implicitly_wait(wait_time)
prod_price = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
prod_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]")
prod_rating = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]")
name4 = prod_name.text
price4 = prod_price.text
rating4 = prod_rating.text

#product5
driver.get(prod5)
driver.implicitly_wait(wait_time)
prod_price = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]")
prod_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]")
prod_rating = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]")
name5 = prod_name.text
price5 = prod_price.text
rating5 = prod_rating.text

#putting all the result in a table using prettytable
table = PrettyTable()
table.field_names = ["S.No.", "Product Name", "Product Price", "Product Rating"]
table.add_row([1, name1, price1, rating1])
table.add_row([2, name2, price2, rating2])
table.add_row([3, name3, price3, rating3])
table.add_row([4, name4, price4, rating4])
table.add_row([5, name5, price5, rating5])
print(table)












