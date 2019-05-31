# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:42:01 2019

@author: aks
"""
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables)
 Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By
 How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By
 How Many Inches For Each One-Inch Increase In Father’s Height.
"""






import pandas as pd
import numpy as np

dataset=pd.read_csv("Female_Stats.csv")

features=dataset.iloc[:,1:]
labels=dataset.iloc[:,0]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((214,1)).astype(int),values=features,axis=1)

features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(labels,features_opt).fit()
regressor_OLS.summary()



print("When Mother's Height is Held Constant",regressor_OLS.params[2])

print("When Father's Height is Held Constant",regressor_OLS.params[1])






