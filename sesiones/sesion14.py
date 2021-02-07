#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:04:08 2021

@author: franciscodeborjaponz
"""

print("Ejemplo de input:")
a=input("¿Que ejmplo quieres ponerme?")
print("Tu ejemplo es",a)
b=input("Ejemplo Numerico?")

class lista_mejorada:
    datos =[28,23,25,23,25]
    def media(self):
        print("La media es:")
        return sum(self.datos) /len(self.datos)
    
edad3 = lista_mejorada()
edad3.datos
edad3.media()