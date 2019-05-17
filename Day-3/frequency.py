# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:54:51 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

test_str=  "www.google.com"

all_freq = {}

for i in test_str:
    
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1

print("count of all characters in  www.google.com is :\n"+str(all_freq))










