#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:03:34 2020

@author: franciscodeborjaponz
"""
#Transformación de datos.

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
#QC OK
#Crear una nueva columna desde el resultado de una columna
wbr['cs_ratio']=(wbr.casual)/(wbr.registered)

wbr.cs_ratio.describe()
plt.hist(wbr.cs_ratio, edgeColor='black')
#en el grafico se puede discrimnar que hay dos tipos de dias, para ello vamos a utilizar los working days para sacarlo.

#asi segmentamos nuestro archivo y nos sirve para aplicar a las diferentes opcines de la variable 'workingday'
wbr.groupby(['workingday']).cs_ratio.describe()

wbr.cs_ratio.describe()

#recodificar una variable(cambiarle el valor de uno a otro)
mytable = wbr.groupby(['season']).size()


#como borrar una columna
#wbr=wbr.drop(columns="season_cat")

#wbr.loc[(filas) , columnas] = valor asignado en la nueva columna
wbr.loc[(wbr['season']==1), "season_cat"] = "Winter"
wbr.loc[(wbr['season']==2), "season_cat"] = "Spring"
wbr.loc[(wbr['season']==3), "season_cat"] = "Summer"
wbr.loc[(wbr['season']==4), "season_cat"] = "Autum"

#despues de realizar la codificación vamos a crear una tabla cruzada, así hacemos un control de calidad.
pd.crosstab(wbr.season, wbr.season_cat)
#QC OK

res = wbr['cnt'].describe()

mean = res[1]
std = res[2]
count = res[0]


mean_substract_std = mean - std
mean_add_std = mean + std

wbr.loc[(wbr['cnt']<mean_substract_std), "cnt_cat2"] = "1: Low rentals"
wbr.loc[((wbr['cnt']>=mean_substract_std)&(wbr['cnt']<mean_add_std)), "cnt_cat2"] = "2: Average rentals"
wbr.loc[(wbr['cnt']>=mean_add_std), "cnt_cat2"] = "3: High rentals"

plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)
plt.axvline(x=mean-std, linewidth=1, linestyle = 'dotted', color= 'Blue', label='-sd')
plt.axvline(x=mean+std, linewidth=1, linestyle = 'dotted', color= 'Blue', label='+sd')
#QC OK 

wbr.dtypes
wbr.info()

mytable = pd.crosstab(index=wbr["cnt_cat2"], columns="count")
print(mytable)

wbr["cnt_cat4"] = wbr.cnt_cat2.astype("category")
wbr.info()
wbr = wbr.drop('cnt_cat4', axis=1)

my_order=["Low rentals", "Average rentals", "High rentals"]
#wbr["cnt_cat4"]= wbr.cnt_cat2.astype("category", ordered=-True, categories=my_order)

from pandas.api.types import CategoricalDtype

my_rentals_type = CategoricalDtype(categories=my_order, ordered=True)

wbr["cnt_cat5"] = wbr.cnt_cat2.astype(my_rentals_type)

#Tarea grupo:
# Elegir un dataset en Kaggle.
# Cargar el dataset en un google colab.
# Describir 6 o 7 variables de ese dataset.    