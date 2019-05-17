# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:37:14 2019

@author: aks
"""



"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

string = input("Enter the string:")

count1=0

count2=0
for i in string:
    if(i.isdigit()):
        count1=count1+1
        count2=count2+1
        print("The number of digit is:")
        print(count1)
        
        
        print("The number of Letters is:")
        print(count2)

###############################################################
        
s = input("Enter a string:")

d=l=0

for c in s:
   
    if c.isdigit():
        d=d+1
   
    if c.isalpha():
        l=l+1
   
    
    else:
        pass
print("Letter",l)

print("Digits",d)
        
       
        
        
        
        
        
        
        
        
        
        
