# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:16:12 2019

@author: aks
"""
"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

a = [6,9,2,3,5,8,1,5,4]
print (type(a))
print (a)  # it always prints the values WITH comma, that's list
import numpy as np

x = np.array( a ) 
print (type(x))

print (x)
x = x.reshape(3,3)
print (x)













