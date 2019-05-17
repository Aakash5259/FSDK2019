# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:00:32 2019

@author: aks
"""

"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""
#####################################################


#from pymongo import MongoClient

import pymongo

client = pymongo.MongoClient("mongodb://Aakash_Sharma:16evjcs001%40@cluster0-shard-00-00-gqo0i.mongodb.net:27017,cluster0-shard-00-01-gqo0i.mongodb.net:27017,cluster0-shard-00-02-gqo0i.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.Student
def add_University(Name,Age,Roll_no,Branch):
    mydb.University.insert_one(
            {
            "Student_Name" : Name,
            "Student_Age" : Age,
            "Student_Roll_no" : Roll_no,
            "Student_Branch" : Branch
            })
    return "University added successfully"


def fetch_all_University():
    user = mydb.University.find()
    for i in user:
        print (i)
        
        add_University ('Ajay',16, 890, 'ECE')
        add_University ('Sumit',18, 456, 'ME')
        add_University('Tushar',20, 234, 'CE')
        add_University ('Vipin',19, 123, 'CSE')
        fetch_all_University()


