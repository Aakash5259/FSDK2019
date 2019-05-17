# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:34:00 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
###############################################################


file = open("absentee.txt", "wt")
    



name=[]
for i in range(0,25):
    str1=input("Enter name>>")
    if not str1:
        break
    name.append(str1)
file.close()
    















