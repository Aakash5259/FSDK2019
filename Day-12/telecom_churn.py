# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:22:45 2019

@author: aks
"""


"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :

File Name : Telecom_Churn.py
problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""

    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Telecom_churn.csv")
df[(df['international plan']=='yes')&(df['voice mail plan']=='yes')&(df['churn']==True)].count()
churn_true=df['total intl charge'][(df['churn']==True)&(df['international plan']=='yes')].sum()
churn_false=df['total intl charge'][(df['churn']==False)&(df['international plan']=='yes')].sum()

labels = 'Nchurnd', 'Churnd'
sizes = [15, 30,]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)

df1=df[df['churn']==True]
churn_true1=df1['total night minutes'].max()
state=df[df['total night minutes']==354.9]

df2=df['international plan'][(df['churn']==True)&(df['international plan']=='yes')].count()
df3=df['voice mail plan'][(df['churn']==True)&(df['voice mail plan']=='yes')].count()
plt.bar(['intl plan','voice mail'],[df2,df3])

df4=df[df['churn']==True]
min1=df4['total day charge'].min()
min2=df4['total eve charge'].min()
min3=df4['total night charge'].min()
min4=df4['total intl charge'].min()
plt.bar(['day','eve','night','int'],[min1,min2,min3,min4])

df['account length'].max()
df5=df[df['account length']==243]


df6=df[df['churn']==True]
count1=df6['customer service calls'].count()
count=df6['customer service calls'][df6['customer service calls']>0].count()
count1=count1-count
plt.bar(['requested','no requested'],[count,count1])

df7=df[df['international plan']=='yes']
df7.groupby('state').min()





