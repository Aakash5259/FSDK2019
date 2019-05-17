# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:32:10 2019

@author: aks
"""
"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
###########################################################
from bs4 import BeautifulSoup as BS
import requests
url=   "https://www.icc-cricket.com/rankings/mens/team-rankings/odi" 
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")
ranking_table=soup.find('table', class_='table')
print(ranking_table)
pos=[]
team=[]
matchs=[]
points=[]
rating=[]
for row in ranking_table.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) ==5:
            pos.append(cells[0].text.strip())
            team.append(cells[1].text.strip())
            matchs.append(cells[2].text.strip())
            points.append(cells[3].text.strip())
            rating.append(cells[4].text.strip())
      
import pandas as pd
from collections import OrderedDict

col_name = ["pos","team","matchs","points","rating"]
col_data = OrderedDict(zip(col_name,[pos,team,matchs,points,rating]))
df = pd.DataFrame(col_data) 











