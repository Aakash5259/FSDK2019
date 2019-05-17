# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:12:33 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""


##########################################

list1=[12,24,35,24,88,120,155,88,120,155]

dup_items=set()

uniq_items=[]

for x in list1:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
        
print(dup_items)


