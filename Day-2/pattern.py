# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:13:12 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
for i in range(0,5):
    print(" *"*i)
for i in range(5,0,-1):
    print(" *"*i)


def pattern(n):
    for i in range(0,n):
        print('\r')
        for j in range(0,i+1):
            print("*",end=" ")
        if i == n-1:
            for i in range(n-1,0):
                for j in range(0,i+1):
                    print("*",end=' ')
            
            




