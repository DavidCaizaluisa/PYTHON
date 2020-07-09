# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:14:25 2020

@author: DAVID CAIZALUISA
"""

def isYearLeap(year):
    if year % 4 == 0:
            return False
    elif year % 100!= 0 :
            return True
    elif year % 400!= 0:
        return False
    else:
         return True
y=isYearLeap(1987)
print(y)

def daysInMonth(year,month):

     if year < 1900 or month < 1 or month > 12:
         return 
     
        
     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     res  = days[month - 1]
     if month == 2 and isYearLeap(year):
	     res = 29
     return res
print(daysInMonth(2019,2))

def dayofyear(year , month, day):
    days=0
    for m in range(1,month):
        md = daysInMonth(year, m)
        if md == None:
            return None
        
        days += md
        
    md = daysInMonth(year , month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None   
print(dayofyear(2020,2,3)) 
