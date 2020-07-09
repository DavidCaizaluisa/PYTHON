# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:24:33 2020

@author: DAVID CAIZALUISA
"""


def fib(n):
    n=int(input("INGRESE LA SUCESION QUE DESEA: "))
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        """ c=a+b
        a=b
        b=C"""
        a, b = b, a+b
    print()
fib(8)