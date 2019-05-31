# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:02:01 2019

@author: aks
"""
"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his 
or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70
    inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting
    intelligence Height, Weight or brain size.
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

dataset = pd.read_csv('iq_size.csv')
labels = dataset.iloc[:,0].values
features = dataset.iloc[:,1:4].values
#plt.scatter(features, labels)

import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:, [0, 1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
listA=[1,90,70,150]
nd=np.array(listA)
nd=nd.reshape(1,4)
regressor_OLS.predict(nd)








