#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:17:36 2020

@author: franciscodeborjaponz
"""
#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 

#importamos la libreria para correlación
from scipy.stats.stats import pearsonr

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK
#La hipotesis nula es que no hay relacion entre las variables (r=0)


x= wbr.temp_celsius
y=wbr.cnt
r1, p_val2 = pearsonr(x, y) #primero coeficiente correlacion, segundo p_value del calculo.
res = wbr.temp_celsius.describe()
count = res[0]


plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none',edgecolors='C0')
plt.yticks(np.arange(0, 10000, step=1000))
plt.title('Figure 9. Daily bicycle rentals, by temperature.')
plt.ylabel('#Daily Rentals')
plt.xlabel('Temperature')
#añadirle un 
plt.show()


x = wbr.windspeed_kh
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none',edgecolors='C0')
plt.yticks(np.arange(0, 10000, step=1000))
plt.title('Figure 9. Daily bicycle rentals, by windspeed.')
plt.ylabel('#Daily Rentals')
plt.xlabel('Windspeed_kh')
plt.show()

"""
Cuando hay dos esquinas con menos puntos de lo normal ayuda para entender
directamente que seguramente hay una relación, describimos la variable.
"""
x = wbr.temp_celsius
res = pearsonr(x, y)
r1, p_val2 = pearsonr(x, y) #primero coeficiente correlacion, segundo p_value del calculo.

print(r1, p_val2)


#x = wbr.windspeed_kh
#res = pearsonr(x, y)
#r1, p_val2 = pearsonr(x, y)
#print(r1, p_val2)

#Extra topic by year
# en este caso la demanada es elastica la temperatura afecta claramente a la demanda.
plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c="yr")

#Season no aporta valor al analisis con la temperatura.
plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c="season")

#Extra topic by year
#S= 20 es el grosor del marcador.
#marker es un tipo de marcador.
plt.figure(figsize=(5,5))
plt.scatter(wbr.temp_celsius[wbr.yr==0],wbr.cnt[wbr.yr==0], s=20, marker="^", facecolors='none', edgecolors='C0',label="2011")
plt.scatter(wbr.temp_celsius[wbr.yr==1],wbr.cnt[wbr.yr==1], s=20, marker="^", facecolors='none', edgecolors='C1',label="2012")

plt.legend(loc="upper right")
box_string = '$\mathrm{r}=%.1f$\n$\mathrm{P.Val}=%.3f$'%(r1, p_val2)
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text (3, 7500, box_string, bbox=props)
plt.savefig('deflines.svg')
plt.show()
#cuidado con las relaciones no lineales, si son curvilineas mucho cuidado.
