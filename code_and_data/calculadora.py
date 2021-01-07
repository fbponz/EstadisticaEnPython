#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:17:56 2021
Entrega final python
@author: franciscodeborjaponz
"""


class calculadora:
    operando_a = 0.0
    operando_b = 0.0
    
    def __init__(self, a, b):
        self.operando_a = a
        self.operando_b = b
    
    def sumar(self):
        return (self.operando_a + self.operando_b)
    
    def restar(self):
        return (self.operando_a - self.operando_b)
    
    def dividir(self):
        return (self.operando_a / self.operando_b)
    
    def multiplicar(self):
        return (self.operando_a * self.operando_b)
  
print("Ejemplo de calculadora EDEM-Python:")
operacion=input("¿Que operación quieres hacer (Sumar/Restar/Multiplicar/Dividir)?")
numero_a=float(input("¿Primer digito operación?"))
numero_b=float(input("¿Segundo digito operación?"))

obj_cal = operacionesbasicas(numero_a, numero_b)

if(operacion == 'Sumar'):
    print(obj_cal.sumar())
elif(operacion == 'Restar'):
    print(obj_cal.restar())
elif(operacion == 'Dividir'):
    print(obj_cal.dividir())
elif(operacion == 'Multiplicar'):
    print(obj_cal.multiplicar())
else:
    print("Operacion desconocida")
