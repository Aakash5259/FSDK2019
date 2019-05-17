# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:16:38 2019

@author: aks
"""

"""
Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
import re


Email=input("ajeet@forsk.com kunal-23@forsk.com yogendra_54@forsk.com:" )

#result=re.findall(r'[0-9a-zA-Z_.-]+@[0-9a-zA-Z_.-]+\.[0-9a-zA-Z_.-]{2,4}', Email)

result= re.findall(r'\w+@\S+\w', Email)
print(result)






