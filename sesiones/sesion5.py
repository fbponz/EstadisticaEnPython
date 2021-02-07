#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:08:05 2020

@author: franciscodeborjaponz
"""

#%reset -f

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Cargamos el fichero WBR.
"""
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape
print(wbr.tail())
#QC OK

plt.hist(wbr.cnt)

"""
Vamos a crear un subset desde un pandas dataset
"""

mytable = wbr.groupby(['yr']).size()
print(mytable)

n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

"""
Con la siguiente instrucción creamos un subset que con las lineas que cumplan
year igual a 0
"""
wbr_2011 = wbr[wbr.yr == 0]
plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()
plt.show()

wbr_2012 = wbr[wbr.yr == 1]

"""
Operadores logicos y operadores aritmeticos.
"""
plt.hist(wbr_2012.cnt)
wbr_2012.cnt.describe()
plt.show()


wbr_2012_winter_1 = wbr[(wbr.yr == 1) & (wbr.season == 1)]

"""
Se puede  anidar crear subsets desde otros subsets.
"""
wbr_2012_winter_2 = wbr_2012[wbr_2012.season == 1]

plt.hist(wbr_2012_winter_1.cnt)
plt.title("Rentals in winter 2012")
plt.show()

plt.hist(wbr_2012_winter_2.cnt)
plt.title("Rentals in winter 2012")
plt.show()

"""
Creamos un subset con casos de otoño y invierno.
"""
wbr_winter_fall = wbr[(wbr.season == 1)|(wbr.season == 4)]
res = wbr_winter_fall.season.unique()
plt.hist(wbr_winter_fall.cnt)
plt.title("Rentals in winter y fall")
plt.show()

###########
mytable_qc = wbr_winter_fall.groupby(['season']).size()
print(mytable_qc)
#QC OK

wbr_ue = pd.read_csv('wbr_ue.csv', sep=';', decimal=',')
wbr_ue.head()

my_var=['temp_celsius','cnt']
wbr_eu_minimal = wbr_eu=[my_var]
plt.hist(wbr_ue.temp_celsius)
result = wbr_ue.temp_celsius.describe()


wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan)
wbr_ue.temp_celsius_c.describe()[1]

wbr_ue.temp_celsius_c.dropna()

plt.hist(wbr_ue.temp_celsius_c.dropna(), edgecolor = "black")

wbr_ue2 = wbr_ue.dropna()

"""
Aplicado sobre un dataframe, quitamos tantas lineas como hacen falta.
"""
print(wbr_ue.shape)
print(wbr_ue2.shape)

#devuelve true o false en funcion de si es un caso duplicado o no.
wbr_ue.drop_duplicates()
res = pd.concat([wbr_ue,wbr_ue.drop_duplicates()]).drop_duplicates(keep=False) 

#otra forma de eliminar los duplicados.
wbr_ue.drop_duplicates('instant', keep='last')   
