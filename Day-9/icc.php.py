# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:58:00 2019

@author: aks
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""
#########################
 
from bs4 import BeautifulSoup
import pandas as pd
import requests
import mysql.connector 
import sqlite3
conn = sqlite3.connect ( 'Cricket.db' ) 
conn = mysql.connector.connect(user='Aakash_Sharma', password='16evjcs001@',
                              host='db4free.net', database = 'Cricket')
c = conn.cursor()

c.execute ("""CREATE TABLE Cricket(
          Position INTEGER,
          Team  TEXT,
          Matches INTEGER,
          Points INTEGER,
          Rating INTEGER
          )""")

lnk = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
pg = requests.get(lnk).text
sp = BeautifulSoup(pg,"lxml")

my_tab = sp.find('table',class_="table")


A=[]
B=[]
C=[]
D=[]
E=[]

for bdy in my_tab.find_all("tbody"):
    for row in bdy.find_all("tr"):
        cel = row.find_all('td')
        A.append(cel[0].text.strip())
        B.append(cel[1].text.strip())
        C.append(cel[2].text.strip())
        D.append(cel[3].text.strip())
        E.append(cel[4].text.strip())

df = pd.DataFrame()
df["Position"]=A
df["Team"]=B
df["Matches"]=C
df["Points"]=D
df["Rating"]=E
  
df.to_csv("data/ODI_Ranking_2017.csv", index=False)


 for i in range (A):
    c.execute("INSERT INTO Cricket VALUES (('{}','{}','{}','{}','{}').format(A[i],B[i],C[i],D[i],E[i]))")

    
    
conn.commit()
 
conn.close()
    

















