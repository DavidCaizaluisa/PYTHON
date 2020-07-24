# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:11:43 2020

@author: DAVID CAIZALUISA
"""


import numpy as np
from random import randint
print("Ingrese la cantidad de filas que desea: ")
fis=int(input())    
print("Ingrese la cantidad de  columnas  que desea: ")
colu=int(input())
print("\n"*0)
matrix=np.zeros([fis,colu])
m=fis
b=fis
fy=-1
clu=-1
for q in range(0,fis):
    for n in range(0,colu):
        matrix[q][n]=int(randint(0,99))
print(" La matriz ejecutada es de",fis,"x",colu,)
print("\n"*0)
print(matrix)
print("\n"*0)
print('El valor de la diagonal principal de la matriz es: ')
print("\n"*0)
for r in range(0,fis):
    if fy<fis:
        fy+=1
        m-=1
    print(' | 0 |'*fy,"|",int(matrix[r][fy])," |",'| 0 | '*m)
    
print('El valor de la diagonal secundaria de la matriz es: ')
print("\n"*0)
for t in range(0,fis):
    if clu<fis:
        clu+=1
        b-=1
    print(' | 0 |'*b,"|",int(matrix[t][b]),"|",'| 0 | '*clu)