# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:01:39 2019

@author: aks
"""

# Make a function days_in_month to return the number of days in a specific month of a year

days_30 = ["apr","jun","sept","nov"]

def year_func(month,year):
    if month == 'feb':
        year = int(year)
        if((year%400==0)or((year%4==0)and(year%100!=0))):
            return month + " 29"
        else:
            return month + " 28"
    else:
        if month in days_30:
            return month + " 30"
        else:
            return month + " 31"


mon, yr = input("Enter Month and Year: ").split()

print(year_func(mon,yr))
