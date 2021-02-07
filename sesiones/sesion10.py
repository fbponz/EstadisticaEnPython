#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:03:54 2020

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

#importamos para poder calcular el modelo.
from statsmodels.formula.api import ols

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')

"""
1)Siempre describir las variables en busqueda de valores anomalos,
2) Siempre explorar relaciones bivariadas Scatterplot/Pearson's
3) Ajustar el modelo de regresión  cuidadosamente.
    a) Escalor y intercept
    b) P.value
    c) Ajuste de modelo
"""
model1 = ols('cnt ~ temp_celsius', data=wbr).fit()
"""
Numero de observaciones, R-squared
al tener un p.value de 0.000  damos por buena y es suficientemente significativa.
En la muestra están asociadas.
R2 es la cantidad de variabilidad de mis ventas, que puedo asociar a la variabilidad
de la temperatura.
"""
model1.summary2() #visualizar el modelo.

"""
Siguiende modelo basado con el windspeed
"""
model2 = ols('cnt ~ windspeed_kh', data=wbr).fit()
model2.summary2() 

"""
Siguiente modelo basado en la temperatura y el windspeed_kh
Como podemos ver en el modelo, al incluir nuevas variables cambia la influencia de
las variables.
"""
model3 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()
model3.summary2()

wbr.hum.hist()
"""
Siguiende modelo basado con la variable humedad
"""
model4 = ols('cnt ~ hum', data=wbr).fit()
model4.summary2() 

"""
Siguiente modelo basado en la temperatura, el windspeed_kh y hum
"""
model5 = ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()
model5.summary2()

"""
stargazer ayuda a representar todos los modelos.
"""
#!pip install stargazer
from stargazer.stargazer import Stargazer

stargazer = Stargazer([model1, model2, model3, model4, model5])
stargazer.render_html()
