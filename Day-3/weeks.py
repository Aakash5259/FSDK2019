# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:06:26 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

a = ('Monday', 'Wednesday', 'Thursday', 'Saturday')

b = ('Tuesday',  'Friday', 'Sunday')

c=(a[0],)+(b[0],)+a[1:3]+(b[1],)+(a[-1],)+(b[-1],)

print(c)








