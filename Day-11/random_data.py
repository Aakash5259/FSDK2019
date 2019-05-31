# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:27:45 2019

@author: aks
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import numpy as np
x=np.random.randint(5, 15,40)
print("array:")
print(x)
print("most frequent value in the array:")
print(np.bincount(x).argmax())