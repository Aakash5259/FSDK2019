# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:03:38 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""


list1=[1,3,6,78,35,55]

list2= [12,6,24,35,24,88,120,155]

def intersection(list1,lis2):
   
    
    list3=[value for value in list1 if value in list2]
    return list3

print(intersection(list1,list2))
    