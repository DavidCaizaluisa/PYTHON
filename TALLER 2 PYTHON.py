# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:27:33 2020

@author: DAVID CAIZALUISA
"""
c=int(input("Ingrese las horas trabajadas: "))
t=int(input("Ingrese la tarifa por horas:"))
d=int(input("Descuento: "))
if c<=40:
    p=c*t-d
else: 
  p=40*t + 1.5*t*(c-40)-d

print("El valor a pagar es: ",p)
    


