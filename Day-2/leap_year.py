# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:40:50 2019

@author: aks
"""

# Make a function to find whether a year is a leap year or no, return True or False 

year=int(input("enter the year number:"))
if((year%400==0)or((year%4==0)and(year%100!=0))):
    print("%d True"%year)
else:
    print("%d False"%year)







