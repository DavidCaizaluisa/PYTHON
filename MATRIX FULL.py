# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:37:26 2020

@author: DAVID CAIZALUISA
"""



import numpy as np

matrix=np.array([[1,2,3,4,5],[5,6,8,9,10]],dtype=np.int64)
print(matrix)
print("\n"*2)
unos=np.ones((4,4))
print(unos)
print("\n"*2)
ceros=np.zeros((5,5))
print(ceros)
print("\n"*2)
ran=np.random.random((4,4))
print(ran)
print("\n"*2)
ept=np.empty((5,5))
print(ept)
print("\n"*2)
full=np.full((5,5),5)
print(full)
print("\n"*2)
