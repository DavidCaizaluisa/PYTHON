# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:35:59 2020

@author: user
"""

from random import randint
from time import sleep 
auxiliar=int()
vector=[int() for ind0 in range(100)]
print("Ingrese tamaño vector")
tamañovector=int(input())
for i in range(1,tamañovector+1):
    vector[i+1]=randint(0,99)
    print("El valor en la posicion",i,"es",vector[i+1])
    sleep(1)
sleep(1)
for j in range(1,tamañovector-1):
    for l in range(1,tamañovector):
        if vector[l+1]<vector[1]:
            auxiliar=vector[l+1]
            vector[l+1]=vector[1]
            vector[1]=auxiliar
for k in range(1,tamañovector-1):
    print("El vector ordenado en la posicion",k,"es",vector[k+1])
    sleep(1)