# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:52:58 2019

@author: aks
"""


"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
#################################################################

import re


Email=input("enter email: ")

#result=re.findall(r'[0-9a-zA-Z_.-]+@[0-9a-zA-Z_.-]+\.[0-9a-zA-Z_.-]{2,4}', Email)

result= re.findall(r'[a-zA-Z0-9_-]+@\S+\w', Email)
print(result)
















