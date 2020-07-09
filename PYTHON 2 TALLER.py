# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:30:24 2020

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

def daysInMonth(year,month):

     if year < 1900 or month < 1 or month > 12:
         return 
     
        
     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     res  = days[month - 1]
     if month == 2 and isYearLeap(year):
	     res = 29
     return res
print(daysInMonth(2019,2))

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")