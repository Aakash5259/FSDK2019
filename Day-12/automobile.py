# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:59:02 2019

@author: aks
"""


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import numpy as np
import pandas as pd
df=pd.read_csv("Automobile.csv")
#df = df.fillna(round(df.mean(),0))
df['price'] = df['price'].fillna(df['price'].mean())
a=df['price']
data=np.array(df['price'])
a.max()
a.min()
a.mean()