# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:25:12 2020

@author: David Caizaluisa
"""

acl=input("ingrese el numero de ACL¡¡")
acl=int(acl)
print("/n"*2)
 if acl>= 1 and acl<= 99:
      print ("es ACL STANDARD")
 elif acl>=100 and acl<=199:
      print ("es ACL EXTENDIAD")
 else:
     print ("No es ACL")    
 