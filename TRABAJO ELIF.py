# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:36:56 2020

@author: David Caizaluisa
"""

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
ubicacion=input("Ingrese su ubicacion: ")

edad=input("Ingrese su edad: ")
edad=int(edad)

if edad>=0 and edad<=10:
   print ("ES NIÑO") 
elif edad>=11 and edad<= 17 :
   print("es adolescente")   
elif edad>=18 and edad<=64 :
   print("es adulto")  
elif edad>=65 and edad<=99:
    print("es adulto mayor")
else:
    print("no es una edda considerada")