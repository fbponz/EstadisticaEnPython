#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:09:01 2020

@author: franciscodeborjaponz
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')


#loop 1
for i in range(0,11,1):
    print("i:", i)
    
#loop 2
for i in [1,2,3,4]:
    print("i:", i)   
    
#loop 3
for i in ["Yellow","Red","Green"]:
    print(i)  

#Basic loop 
for i in range(10,101, 1):
    x=wbr['cnt']
    plt.hist(x, bins=i, edgecolor='black')
    plt.show()
    print(i)
    
for i in range(20,0, -2):
    x=wbr['cnt']
    plt.hist(x, bins=i, edgecolor='black')
    plt.show()
    print(i)
    
# Ejercicio dibujar en un plot
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

c1=plt.Circle((5, 5), 1, color='r') #Define  circle
ax.add_artist(c1)  #Draw circle

#Lienzo de fondo
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))  
c1=plt.Circle((i, i), 0.5,alpha=0.7, color='r')  
for i in range(0,10,1): 
    c0=plt.Circle((i-1, i-1), 0.5,alpha=0.7, color='w')
    c1=plt.Circle((i, i), 0.5,alpha=0.7, color='r') #Define  circle
    ax.add_artist(c0)  #Draw circle
    ax.add_artist(c1)  #Draw circle
    
### Pintar en azul
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))  
c1=plt.Circle((i, i), 0.5,alpha=0.7, color='r')  
for i in range(0,11,1): 
    c0=plt.Circle((10-i, i), 0.5,alpha=0.7, color='b')
    c1=plt.Circle((i, i), 0.5,alpha=0.7, color='r') #Define  circle
    c2=plt.Circle((i, 5), 0.5,alpha=0.7, color='y')
    c3=plt.Circle((5, i), 0.5,alpha=0.7, color='g') #Define  circle
    ax.add_artist(c0)  #Draw circle
    ax.add_artist(c1)  #Draw circle
    ax.add_artist(c2)  #Draw circle
    ax.add_artist(c3)  #Draw circle


####Dibujar con diferentes  tamaños
### Pintar en azul
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))  
c1=plt.Circle((i, i), 0.5,alpha=0.7, color='r')  
for i in range(0,11,1): 
    c0=plt.Circle((10-i, i), i*0.05,alpha=0.7, color='b')
    c1=plt.Circle((i, i), i*0.05,alpha=0.7, color='r') #Define  circle
    c2=plt.Circle((i, 5), i*0.05,alpha=0.7, color='y')
    c3=plt.Circle((5, i), i*0.05,alpha=0.7, color='g') #Define  circle
    ax.add_artist(c0)  #Draw circle
    ax.add_artist(c1)  #Draw circle
    ax.add_artist(c2)  #Draw circle
    ax.add_artist(c3)  #Draw circle

### Cambiar el color
####Dibujar con diferentes  tamaños
### Pintar en azul
colors=['b','g','r','c','m','y','orange','maroon', 'darkgreen', 'aquamarine', 'k']
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))  
c1=plt.Circle((i, i), 0.5,alpha=0.7, color=colors[0])  
for i in range(0,11,1): 
    c0=plt.Circle((10-i, i), i*0.05,alpha=i*0.1, color=colors[i])
    c1=plt.Circle((i, i), i*0.05,alpha=i*0.1, color=colors[i]) #Define  circle
    c2=plt.Circle((i, 5), i*0.05,alpha=i*0.1, color=colors[i])
    c3=plt.Circle((5, i), i*0.05,alpha=i*0.1, color=colors[i]) #Define  circle
    ax.add_artist(c0)  #Draw circle
    ax.add_artist(c1)  #Draw circle
    ax.add_artist(c2)  #Draw circle
    ax.add_artist(c3)  #Draw circle

count=1
while(count<4):
    print(count,"Calidad")
    count=count+1
    
test_covid = "Negativo"
if test_covid == "Negativo":
    print("Puede usted salir de casa")
else:
    print("Debe quedarse en casa")
    
for i in range(0, 11, 1):
    if i >8:
        print("nota:",i, "Excelente")
    elif i >6:
        print("nota:",i, "Notable")
    elif i>5:
        print("nota:",i, "Bien")
    elif i>4:
        print("nota:",i, "Aprobado")
    else:
        print("nota:",i, "Suspendido")

""" Comentario de la función"""
def plus(a,b):
    print("Sumamos estos argumentos")
    return a + b   

plus(4,5)

""" Comentario de la función"""
def dividir(a,b):
    print("Sumamos estos argumentos")
    return a / b   

dividir(4,5)
dividir(b=5,a=4)

def dividir_parametros_pred(a, b=2):
    print("Sumamos estos argumentos")
    return a / b   

dividir_parametros_pred(6)

### Tarea de python
### Encapsular histogramas y grafico de barras
### Dibujar una animación en python