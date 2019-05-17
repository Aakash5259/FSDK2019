# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:48:10 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""



from collections import OrderedDict
dict1 = OrderedDict()

inp = input("Enter: ")


dict1["BANANA FRIES"] = 12
dict1["POTATO CHIPS"] = 30
dict1["APPLE JUICE"] = 10
dict1["CANDY"] = 5


item ="BANANA FRIES" 
price = 12
item = "POTATO CHIPS"
price = 30
item = "APPLE JUICE"
price = 10
item = "CANDY"
price = 5

if item in dict1:
    dict1[item] = dict1[item] + price
else:
    dict1[item] = price

#############################################

from collections import OrderedDict
total_billing = OrderedDict()

while True:
    user_input=input("enter value >")
    if not user_input:
        break
    item = user_input.split()
    product = " ".join(item[:-1])
    price = int(item[-1])
    
    if product in total_billing:
        total_billing[product] = total_billing[product] + price
    else:
        total_billing[product] = price
    
for k,v in total_billing.items():
    print(k,v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

