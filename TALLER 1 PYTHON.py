# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:20:22 2020

@author: DAVID CAIZALUISA
"""
#llantasdescuento
#PRIMERO DEFINIMOS CADA UNO DE LOS ITEMS 
n=int(input("Cantidad de llantas: "))
p=int(input("Precio unitario: "))
#TIENE QUE SER MAYOR A 4 LLANTAS PARA EL DESCUENTO
if n>4:
     p=0.9*p
t=n*p
print("Valor a pagar: ",t)