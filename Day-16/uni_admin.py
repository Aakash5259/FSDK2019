# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:44:14 2019

@author: aks
"""

"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""

import pandas as pd  
import numpy as np  
#import matplotlib.pyplot as plt
  
dataset = pd.read_csv('University_data.csv')
temp = dataset.values
features= dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1:].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
x=['Alaska Methodist University',295,2,2,7.2,0]
x=np.array(x)
x=x.reshape(1,-1)
x[:, 0] = labelencoder.transform(x[:, 0])
x = onehotencoder.transform(x).toarray()
x=x[:,1:]
print(regressor.predict(x))




