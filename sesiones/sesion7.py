# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Mean Comparison
MDA EDEM
"""
#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

#load basiclibraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# New libraries
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference 
import seaborn as sns  # For hi level, Pandas oriented, graphics

# Get working directory
os.getcwd()

# Change working directory
os.chdir('the path to your working directory here')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#QC OK

# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

#frequencies
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#Sesión 7, Mean comparison(2 groups).
# sobre la muestra esta clara, pero en washington en general no sé sabe
# la varianza de cada muestra nos cambia entre datasets.
wbr.groupby('wd_cat').cnt.mean()
#la prueba de te
cnt_wd = wbr.loc[wbr.wd_cat=='Yes', "cnt"]
#CI meanplot as sns

cnt_nwd = wbr.loc[wbr.wd_cat=='No', "cnt"]
#prueba de T
#nos devuelves dos valores el primero no es muy importante, pero el segundo
#si que es pi values. contra menos mejor. 95% es igual a 0.05! un valor
# 
res = stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
print(res)

#graficos con intervalos de confianza.
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000,7000, step=500))
plt.ylim(2800, 6200)
plt.axhline(y=wbr.cnt.mean(), linewidth = 1, linestyle = 'dashed', color ="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.85, 5400, 'Mean 4504.3''\n''')
plt.xlabel('working days')
plt.legend()

# primero le ponemos el calitativo y despues el cuantitativo.
#join = 0 -> para evitar que ponga una linea 
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
#añadir el valor de t y el pvalue en la leyenda. el valor de t es un digito de control.
# con este valor de p_Value no nos tenemos datos para contra decir la primera hipotesis.

#acabar en casa.
wbr.groupby('yr').cnt.mean()

cnt_2011 = wbr.loc[wbr.yr==0, "cnt"]
cnt_2012 = wbr.loc[wbr.yr==1, "cnt"]
res = stats.ttest_ind(cnt_2011, cnt_2012, equal_var = False)
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
# La prueba de T solo es valido para dos grupos

#Para comunicar resultados es recomendable que se gasten los mismos ejes.
#En caso de anova, se reporta estadistico, f y pvalue
res = stats.ttest_ind(cnt_2011, cnt_2012, equal_var = False)

wbr.groupby('ws_cat').cnt.mean()
cnt_sunny = wbr.loc[wbr.yr=='Sunny', "cnt"]
cnt_cloudy = wbr.loc[wbr.yr=='Cloudy', "cnt"]
cnt_rainy = wbr.loc[wbr.yr=='Rainy', "cnt"]