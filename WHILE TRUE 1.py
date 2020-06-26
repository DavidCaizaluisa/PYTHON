# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:11:57 2020

@author: user
"""


while true:
    x=input("Enter a number to count to: ")
    
    if x == "q" and x == "quit":
        break 
    x=int(x) 
    y=1
   
   while true:
     print(y)  
     
     y= y + 1
     
     if y > x:
        break
    