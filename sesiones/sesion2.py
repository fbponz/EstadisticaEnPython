#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:53:51 2020

@author: fbponz
"""
#%reset -f

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()

"""
Con el siguiente comando cargamos el fichero .csv, debemos incluir que tipo de
separador tenemos y que tipo de separación decimal vamos a gastar.
CSV -> Europeo sep = ; con separador decimal ,
CSV -> Americano sep = , con separador decimal .

@attention cuando importamos ficheros puede venir problemas en la primera 
columna y en la ultima.
"""
rentals_2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')

"""
El siguiente estudiante nos devuelve la dimensionalidad del objeto (numero 
                    total de elementos, y de caracteristicas de cada elemento).
"""
rentals_2011.shape
"""
El siguiente comando nos devuelve las primeras 5, si le pasamos sin parametro
mientras que si le especificamos  un numero en los brackets, nos devuelve X 
elementos del principio.
"""
rentals_2011.head()
"""
El siguiente comando nos devuelve los ultimos 5, si le pasamos sin parametro
mientras que si le especificamos  un numero en los brackets, nos devuelve X 
elementos del final.
"""
rentals_2011.tail()

#QC OK

"""
las variables que nos interesan del csv washington_bike_rentals_2011, los datos
que nos interesan son los campos: casual, registered, cnt.
"""

"""
Es una variable cuantitativa, nos representa que tipo de negoció que tenemos.
"""
#Alberto's Tips: es recomendable cuando hay elementos variables que cambian no incluirlo en la función de plot.
ds_cnt = rentals_2011.cnt
plt.hist(ds_cnt)

#plotea  los datos de casual.
ds_casual = rentals_2011.casual
plt.hist(ds_casual)

#plotea los datos de registered.
ds_registered = rentals_2011.registered
plt.hist(ds_registered)

"""
Incluimos algo de diseño en los graficos.
"""
plt.hist(ds_registered, edgecolor='black')
plt.xticks(np.arange(0, 7000, step=1000)) #añadir ejes a nuestro grafico.
plt.title('Figure 1. Registered rentals in Washington') #añadir titulo a nuestro grafico.
plt.show()

