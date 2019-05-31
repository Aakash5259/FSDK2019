# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:57:12 2019

@author: aks
"""
"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()
print (series.index[0:11])
print (series.values[0:11])

explode = (0.3,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal') 

plt.show() 

