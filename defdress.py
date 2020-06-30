# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:40 2020

@author: David Caizaluisa
"""
def direccion(calle,sector,códigopostal,referencia,numcasa):
    print("Su dirección es; ","sector : ",sector,"Calle",calle)
    print("Sucasa es la #: ",numcasa,"con codigo postal #:",codigopostal) 
    print("Y esta cerca de: ",referencia)
  
print("Ingrese los datos que se solicitan de direccion")
c=input("Ingrese la calle:")
s=input("Ingrese secotr de residencia:")
cod=input("")
r=input("Ingrese una referencia de su domicilio:")
num=input("Ingrese el # de casa:")

direccion(c,s,cod,r,num)