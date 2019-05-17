# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:19:46 2019

@author: aks
"""
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
##############################################

from  selenium import webdriver
import pandas as pd

url= "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:/Users/aks/Downloads/chromedriver_win32/chromedriver.exe")
bid_l=[]
item=[]
Qr=[]
driver.get(url)
for i in range(1,11):
    bid = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a')
    bid_l.append(bid.text)
    item_nm = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span')
    item.append(item_nm.text)
    qr=








