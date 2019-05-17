# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:36:14 2019

@author: aks
"""


"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""

import re

file=open('simpsons_phone_book.txt','r') 
#    txt_read = txt.reader(txt_file)
#    for i in txt_read:
        
#        print(i)
content = file.read()
result=re.findall('J[a-zA-Z ]+ Neu',content)
print(result)

