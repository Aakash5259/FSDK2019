# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:55:36 2019

@author: aks
"""



"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

######################################################3

num= input("enter the number:" ).split()

def pali(num):
    
    if num==num[::-1]:
              
        print('True')
    else:
        print('False')
    
    
final = list(filter(pali,num))

print(final)
    
#######################################################



list(map(lambda x: 'true' if x==x[::-1] else 'false',num))








