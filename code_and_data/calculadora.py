#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:17:56 2021
Entrega final python
@author: franciscodeborjaponz
"""
import os

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
    
keep_running = True
resultado = 0
while keep_running:
    print("calculadora EDEM-PROGRAMACIÓN ESTADÍSTICA CON PYTHON:")
    operacion=input("¿Que operación quieres hacer (Sumar/Restar/Multiplicar/Dividir/Salir)?")
    operacion=operacion.lower()
    if(operacion=='salir'):
        keep_running = False
        print("Gracias por utilizar la calculadora")
    else:
        print("Si quieres gastar el valor en memoria escribe ANS+, el valor actual en memoria es: "+str(resultado))
        selecion_a=input("¿Primer digito operación? ")
        selecion_b=input("¿Segundo digito operación? ")
        
        if(str == type(selecion_a)):
            selecion_a = selecion_a.upper()
            
        if(str == type(selecion_b)):
            selecion_b = selecion_b.upper()
        
        
        if(selecion_a == 'ANS+'):
            numero_a=resultado
        else:
            numero_a = float(selecion_a)
            
        if(selecion_b == 'ANS+'):
            numero_b=resultado
        else:
            numero_b = float(selecion_b)
        
        obj_cal = calculadora(numero_a, numero_b)
        if ((operacion=='sumar')or(operacion=='restar')or(operacion == 'dividir')or(operacion == 'multiplicar')):
            if(operacion == 'sumar'):
                resultado=obj_cal.sumar()
            elif(operacion == 'restar'):
                resultado=obj_cal.restar()
            elif(operacion == 'dividir'):
                resultado=obj_cal.dividir()
            elif(operacion == 'multiplicar'):
                resultado=obj_cal.multiplicar()
        else:
            print("Operacion desconocida")
        
        ##Limpiar consola
        if os.name == "posix":
            os.system ("clear")
        elif (Sumar(os.name == "ce") or (os.name == "nt") or (os.name == "dos")):
            os.system ("cls")
        print("Resultado de " + operacion + ": Entre " + str(numero_a) + " con " + str(numero_b) + " resultado: " + str(resultado));
    
