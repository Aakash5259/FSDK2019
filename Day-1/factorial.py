# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:49:13 2019

@author: aks
"""
def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
num=int(input("enter a number"))
if num<0:
    print("factorial cannot be found")
else:
    print(factorial(num))