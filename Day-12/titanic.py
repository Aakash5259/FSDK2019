# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:56:55 2019

@author: aks
"""

import pandas as pd
#import numpy as np
df=pd.read_csv("training_titanic.csv")

print (df)
df.info() 
df.axes
df['Survived']
df['Survived'].value_counts()
df['Survived'].value_counts(normalize = True)


df['Sex'] 
df['Sex'].value_counts()
df['Sex'].value_counts(normalize = True)

df_male = df[df['Sex'] == 'male' ][['Survived']]

df_female = df[df['Sex'] == 'female' ][['Survived']]
df_male['Survived'].value_counts()
df_female['Survived'].value_counts()

df["Child"] = df["Age"].map(lambda x: 1 if x <18 else 0 )
df_Child = df[(df['Child'] == 1)]
df_Child['Survived'].value_counts()