# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:21:32 2019

@author: aks
"""

# Create a list of number from 1 to 20 using range function. 
list1=[]

list(range(1,21))
print(list1)
list1=[]
for a in range(1,20):
    print(a)
    
    list1.append(a)
print(list1)
