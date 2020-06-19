# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:10:44 2020

@author: David Caizaluisa
"""

ipadd={"R1":"10.1.1.1" , "R2":"10.2.2.1","R3":"10.3.3.1","S1":"10.1.0.1","S2":"10.1.0.2"}
print(type(ipadd))

dict1={"usuario1":"1754872554","valor":5000,"edad":39,"soltero":True,"RATE en %":52.2}

print(ipadd["R2"])
ipadd["S4"]="10.1.0.4"
print("S1" in ipadd)
print("edad" in dict1)