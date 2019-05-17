# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:50:59 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

file1= open("file1","wt")

    ########################################################
    
with open ("new.txt", "rt") as rf :
  with open ("file1.txt", "wt") as wf :
    for line in rf :
      wf.write ( line)
    

    
    
    
    
    
    
    