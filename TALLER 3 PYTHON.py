# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:33:37 2020

@author: DAVID CAIZALUISA
"""
d=int(input("Ingrese la primera calificacion: "))
e=int(input("Ingrese la segunda calificacion: "))
f=int(input("Ingrese la tercera calificacion: "))

if d>=f and e>=f :
    t=d+e
else:
    t=d+f
print("Su promedio es: ",t)