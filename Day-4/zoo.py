# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:38:00 2019

@author: aks
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
##########################################
import csv

with open('zoo.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    for i in csv_read:
        print(i)

#{"elephant":[[1001,1002,1003],[500,600,550]],"tiger":[[],[]]}

animal_data = {}
with open('zoo.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)
    for row in csv_read:
        if row[0] not in animal_data:
            animal_data[row[0]] = [[int(row[1])],[int(row[2])]]
        else:
            animal_data[row[0]][0].append(int(row[1]))
            animal_data[row[0]][1].append(int(row[2]))

print(animal_data)
   
l = list()
a=sum(animal_data["elephant"][1])
b=sum(animal_data["tiger"][1])
c=sum(animal_data["zebra"][1])
d=sum(animal_data["kangaroo"][1])



for i in (a,b,c,d):
    l.append(i)
print(sum(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    