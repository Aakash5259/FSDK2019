# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:12:13 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

######################################

import ast

inp = input("Enter: ")
dict1= ast.literal_eval(inp)

sum1= 0

for i in dict1.values():
    if 13<=i<=19 and i!=15 and i!= 16:
        sum1=sum1
        
    else:
        sum1= i+sum1
print(sum1)
        
        
        
#############################################################        
        
        
        

      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
