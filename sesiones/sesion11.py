#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:06:10 2020

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


model1 = ols('cnt ~ temp_celsius', data=wbr).fit()

model1b = ols('cnt ~ windspeed_kh', data=wbr).fit()

model2 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()

model3 = ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()


model1d = ols('cnt ~ workingday', data=wbr).fit()

print(model1d.summary2())

model4 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday', data=wbr).fit()
print(model4.summary2())

"""
Cuando metamos variables dicotomicas en el modelo que el No -> 0 y la Yes -> 1,...
"""
model5 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr', data=wbr).fit()
print(model5.summary2())

"""
One hot encoding, variables dummy variables dummyes
"""
dummies = pd.get_dummies(wbr.weathersit)

colnames ={1:'sunny', 2:'cloudy', 3:'rainy'} #Esto es un diccionario.

dummies.rename(columns = colnames, inplace = True)
wbr_dummies=pd.concat([wbr,dummies],axis=1)

pd.crosstab(wbr_dummies.weathersit, wbr_dummies.sunny)
pd.crosstab(wbr_dummies.weathersit, wbr_dummies.cloudy)
pd.crosstab(wbr_dummies.weathersit, wbr_dummies.rainy)
#QC OK
wbr=pd.concat([wbr,dummies],axis=1)

model5 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + sunny', data=wbr).fit()

"""
Cuando hacemos un modelo de regresión y con variables que tienen mas de dos valores
dummy hay que dejar fuera una variable fuera. Por que sino en la predicción del
modelo no nos dara bien.
"""
model6 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + cloudy + rainy', data=wbr).fit()
print(model6.summary2())


dummies_season = pd.get_dummies(wbr.season)

colnames_season ={1:'winter', 2:'spring', 3:'summer', 4:'autumn'} #Esto es un diccionario.

dummies_season.rename(columns = colnames_season, inplace = True)
wbr_season_dummies=pd.concat([wbr,dummies_season],axis=1)

pd.crosstab(wbr_season_dummies.season, wbr_season_dummies.winter)
pd.crosstab(wbr_season_dummies.season, wbr_season_dummies.spring)
pd.crosstab(wbr_season_dummies.season, wbr_season_dummies.summer)
pd.crosstab(wbr_season_dummies.season, wbr_season_dummies.autumn)
#QC OK
wbr =pd.concat([wbr,dummies_season],axis=1)

model7 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + cloudy + rainy + spring + summer + autumn', data=wbr).fit()
print(model7.summary2())

"""
Creamos la variabla  nonlinear
"""

wbr['temp_2'] = wbr.temp_celsius*wbr.temp_celsius

model8 = ols('cnt ~ temp_celsius + temp_2 + windspeed_kh + hum + workingday + yr + cloudy + rainy + spring + summer + autumn', data=wbr).fit()
print(model8.summary2())




























