# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:17 2020

@author: DAVID CAIZALUISA
"""

def isYearLeap(year):
 año=int(input('Introduce un año: '))

 if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('TRUE')
        else:
            print('FALSE')
    else:
        print('TRUE')
 else:
    print('FALSE')
    
    
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
