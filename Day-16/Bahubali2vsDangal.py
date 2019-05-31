# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:58:52 2019

@author: aks
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
plt.boxplot(dataset.values)


features1 = dataset.iloc[:,:1].values  
labels1 = dataset.iloc[:,1:2].values


features2 = dataset.iloc[:,:1].values  
labels2 = dataset.iloc[:,2:3].values

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features2, labels2, test_size=0.2, random_state=0)  


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
list1=[10]
x=np.array(list1)
x=x.reshape(1,1)
Dangle = regressor.predict(x)
#print(regressor.intercept_)  
#print (regressor.coef_)









