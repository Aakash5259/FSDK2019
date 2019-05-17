# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:51:47 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '12')
"""


user_input = ("2, 4, 7, 8, 9, 12").split(",")
print(user_input)

final= tuple(user_input)

print(final)






