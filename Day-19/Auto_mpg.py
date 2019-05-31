# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:23:05 2019

@author: aks
"""
"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per
 gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight",
    "acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more
    accurate in predicting the MPG value
    
Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders,
having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a
displacement of about 215. (Give the prediction from both the models)
"""
#import pandas as pd  
#import numpy as np  

#dataset = pd.read_csv("Auto_mpg.txt")  
#import os
#import pandas as pd
 #save_path = "F:\FSDK2019\Day-19"
 #in_filename = os.path.join(save_path,'Auto_mpg.txt')
#out_filename = os.path.join(save_path,'Auto_mpg.csv')
 #df = pd.read_csv(in_filename, sep=";")
#df.to_csv(out_filename, index=False)
##############################################

import pandas as pd
#import matplotlib.pyplot as plt 
#import numpy as np 
dataset = pd.read_csv("Auto_mpg.txt",delimiter="\s+",header=None) 
dataset.columns  =["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

name=dataset["car name"][dataset["mpg"]==dataset["mpg"].max()]
dataset["horsepower"]=dataset["horsepower"].replace('?',dataset["horsepower"].mode()[0]).astype('float64')

features = dataset.drop(['mpg','car name'] ,axis=1)  
labels = dataset['mpg'] 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
dataset=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
dataset  


######################################################################
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred2 = regressor.predict(features_test)

dataset=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
dataset    
