# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:05:05 2019

@author: aks
"""

"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""
###################################################################
#import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'University.db' )
c = conn.cursor()


c.execute ("""CREATE TABLE University(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO University VALUES ('Rahul',14, 678, 'CSE')")
c.execute("INSERT INTO University VALUES ('Ajay',16, 890, 'ECE)')")
c.execute("INSERT INTO University VALUES ('Sumit',18, 456, 'ME')")
c.execute("INSERT INTO University VALUES ('Tushar',20, 234, 'CE')")
c.execute("INSERT INTO University VALUES ('Vipin',19, 123, 'CSE')")

c.execute("SELECT * FROM University")

print ( c.fetchone()) 

print ( c.fetchmany(2)) 

print ( c.fetchall() )

c.execute("SELECT * FROM University")

df = DataFrame(c.fetchall())
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]


conn.commit()

conn.close()

#####################################################################



























