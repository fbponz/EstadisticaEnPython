#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:47:09 2020

@author: franciscodeborjaponz
"""

"""
Naturaleza de las variables 
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
#QC OK


"""
El metodo describe nos devuelve 
count -> numero de elementos
mean -> media
std -> desviación estandar
min -> el dia que menos hemos alquilado.
cuartiles 25%, 50% 75%
max -> dia que mas bicis hemos alquilado

wbr.cnt.mean()
wbr.cnt.min()
"""
res = wbr.cnt.describe()

def set_title_and_labels(title, xlabel, ylabel):
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)



def plot_hist(data_in, edgeColor, ticks, title, yLabel, xLabel, mean_activated, mean, mean_color, deviation_activated, deviation, deviation_color_a, deviation_color_b, text_pos_x, text_pos_y, text_box_string, props):
    plt.hist(data_in, edgecolor=edgeColor)
    plt.xticks(ticks)
    set_title_and_labels(title, xLabel, yLabel)
    if mean_activated == True:
        plt.axvline(x=mean, linewidth=1, linestyle = 'solid', color= mean_color, label='Mean')
    if deviation_activated == True:
        plt.axvline(x=mean-deviation, linewidth=1, linestyle = 'dashed', color= deviation_color_a, label='-sd')
        plt.axvline(x=mean+deviation, linewidth=1, linestyle = 'dashed', color= deviation_color_b, label='+sd')
    if mean_activated == True or deviation_activated == True:
        plt.legend()
    plt.text(text_pos_y, text_pos_x, text_box_string, bbox=props)    
    plt.show()
    
def plot_bar(data_in, data_list, edgeColor, title, yLabel, xLabel):
    plt.bar(data_list, data_in, edgeColor=edgeColor)
    set_title_and_labels(title, xLabel, yLabel)            
        
"""
Las variables cuantitavas se representan con histogramas. media y desviacion tipica
"""
x =wbr['cnt'] 
m = res[1]
sd = res[2]
n = res[0]
ticks=np.arange(0,10000,1000)
graph_title = 'Figure 1. Daily Bicycle rentals in Washington DC' '\n' 'by Capital bikeshare. 2011 - 2012'
y_label = 'Frequency'
x_label = 'Number of rented bicycles'
box_string = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
props = dict(boxstyle='round', facecolor='white', lw=0.5)

plot_hist(x, 'black', ticks, graph_title, y_label, x_label, True, m, "red", True, sd, "green", "brown", 6500, 110, box_string, props)

#textstr='Hola'
#plt.text('Rainy', 115, textstr)
#plt.show()


#textStr = 'Mean = 4504v\nS.D.=1937 \nn = 731'
#plt.text(6500, 110, textStr)
#plt.show()

### Añadir lineas para hacer lineas y la leyenda.

"""
Las variables nominales, porcentajes y grafico de barras. incluyendo el sampleo.
"""

mytable = wbr.groupby(['weathersit']).size()
mytable.sum()
mytable2 = (mytable/n)*100
bar_list = ['Sunny', 'Cloudy', 'Rainy']
title = 'Figure 1. Percentage of weather situations'
xLabel = 'Different weather situations'
yLabel = 'Percentage'

plot_bar(mytable2, bar_list, 'black', title, yLabel, xLabel)
