# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:17 2020

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

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
