# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:53:07 2020

@author: DAVID CAIZALUISA
"""


dato=int(input("Ingrese el numero de veces a contar: "))

contador=1
acumulador=0
while contador <=dato:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
print("\n"*2)
print("La suma de los numeros es: ",acumulador)
print("el promedio total es: ",acumulador+contador)