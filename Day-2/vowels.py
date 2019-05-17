# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:15:43 2019

@author: aks
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""


string=[ 'Alabama','California','Oklahoma', 'Florida']
list2=[]
for item in string :
    list2.append(item.lower())
    
    
vowels=['a','e','i','o','u']
list1=[]
for item in list2:
    for char in item:
        if char in vowels:
            item=item.replace(char,"")
    list1.append(item)   
            
             
        








