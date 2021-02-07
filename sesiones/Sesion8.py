# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Percentage Comparison
MDA EDEM
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

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK


#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

pd.crosstab(wbr.cnt_cat, wbr.wd_cat, margins=True)

#Revisar si los porcentajes son correctos  para ello ver que la suma sea 100
my_ct = pd.crosstab(wbr.wd_cat, wbr.cnt_cat, normalize='columns', margins=True)*100

my_ct.round(1) #Objeto, metodo
#vamos ha hacer la comprobación de chi2
#el estadistico de chi2 se calcula sobre la tabla de contingencias con las
#frecuencias. solo dos variables con total y sin porcentajes.
ct=pd.crosstab(wbr.cnt_cat, wbr.wd_cat)

stats.chi2_contingency(ct)

"""
Salida el primero es el digito de control (Solo puede haber unos datos con un chi2 y un p_value).
p_Value tiene que ser menor de 0.05 sino no podemos rechazar la hipotesis nula.
"""
my_ct.plot(kind="bar") 

my_ct2=my_ct.transpose()
my_ct2.plot(kind="bar")

#hacer lo mismo con el weather conditions
#seaborn hacer grafico de barras.
wbr["weathersit_st"] = wbr.weathersit
wbr.weathersit_st = wbr.weathersit_st.replace(to_replace=1, value="Sunny")
wbr.weathersit_st = wbr.weathersit_st.replace(to_replace=2, value="Cloudy")
wbr.weathersit_st = wbr.weathersit_st.replace(to_replace=3, value="Rainy")

my_categories_weather=["Sunny", "Cloudy", "Rainy"]
my_weather_type = CategoricalDtype(categories=my_categories_weather, ordered=True)
wbr["weathersit_cat"] = wbr.weathersit_st.astype(my_weather_type)

# Barchat for Working day
mytable_wsc = pd.crosstab(index=wbr["weathersit_cat"], columns="count") # Crosstab
n=mytable_wsc.sum()
mytable2_wsc = (mytable_wsc/n)*100
print(mytable2_wsc)
plt.bar(mytable2_wsc.index, mytable2_wsc['count'])
plt.xlabel('Weather situation')
plt.title('Figure 6. Percentage of Weather Condition Days')

pd.crosstab(wbr.cnt_cat, wbr.weathersit_cat, margins=True)
my_wth_ct = pd.crosstab(wbr.weathersit_cat, wbr.cnt_cat, normalize='columns', margins=True)*100

my_wth_ct.round(1)

my_wth_ct=pd.crosstab(wbr.cnt_cat, wbr.weathersit_cat)
stats.chi2_contingency(my_wth_ct)

my_wth_ct2= my_wth_ct.transpose()
my_wth_ct2.plot(kind="bar")

"""
#guardar el workspace variables
!pip install dill
import dill
filename = '/Users/franciscodeborjaponz/Developer/mda-Workspace/EstadisticaEnPython/code_and_data/workvariables.pkl'
#Guardar variables
dill.dump_session(filename)

#cargar variables
dill.load_session(filename)
"""