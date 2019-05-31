# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:31:40 2019

@author: aks
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv
Here, we are building a decision tree to check if a person is hired or not based on
 certain predictors.
Import PastHires.csv File.
scikit-learn needs everything to be numerical for decision trees to work.
So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.
 Build and perform Decision tree based on the predictors and see how accurate your
 prediction is for a being hired.
Now use a random forest of 10 decision trees to predict employment of specific
 candidate profiles:
 Predict employment of a currently employed 10-year veteran, previous employers 4, went to 
 top-tire school, having Bachelor's Degree without Internship.
 Predict employment of an unemployed 10-year veteran, ,previous employers 4,
 didn't went to any top-tire school, having Master's Degree with Internship.
"""

import pandas as pd
#import matplotlib.pyplot as plt 
#import numpy as np 
dataset = pd.read_csv("PastHires.csv")

from sklearn.preprocessing import LabelEncoder


features = dataset.drop(['Hired'] ,axis=1)  
labels = dataset['Hired']

listA=[]

for x in [1,3,4,5]:
    la=LabelEncoder()
    features[:,x]=la.fit_transform(features[:,x])
    listA.append(la)
    
la=LabelEncoder()
labels=la.fit_transform(labels)
listA.append(la)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test) 
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  
 



     
    
 