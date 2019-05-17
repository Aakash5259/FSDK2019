# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:16:22 2019

@author: aks
"""

str1=input("Enter the word.")
str2=str1[1:]
str2=str2.replace("R","$")
print(str1[0]+str2)