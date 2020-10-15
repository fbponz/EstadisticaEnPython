#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:24:58 2020

@author: franciscodeborjaponz
"""
#%reset -f

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Con el siguiente comando cargamos el fichero .csv, debemos incluir que tipo de
separador tenemos y que tipo de separación decimal vamos a gastar.
CSV -> Europeo sep = ; con separador decimal ,
CSV -> Americano sep = , con separador decimal .

@attention cuando importamos ficheros puede venir problemas en la primera 
columna y en la ultima.
"""
rentals_2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')
#añadimos los datos meteorologicos.
weather_2011 = pd.read_csv('weather_washington_2011.csv', sep=';', decimal=',')

"""
Antes de hacer fusión de datos entre diferentes ficheros, debemos comprobar que
los diferentes datasets disponibles tienen almenos datos comunes que nos sirvan
para poder fusionarlos así como tambien que no están corruptos a inicio o final. 
"""
weather_2011.shape
weather_2011.tail()
weather_2011.head()
rentals_2011.tail()
rentals_2011.head()
#QC OK

"""
En el siguiente comando tenemos que seleccionar primero caul de los dos 
ficheros que queremos fusionar, en el parametro on es muy importante añadir
un UNQID.
"""
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on="day")

"""
Despues de hacer el merge cogemos y analizamos si tienen la calidad que esperamos.
"""
rentals_weather_2011.shape
rentals_weather_2011.head()

"""
Vamos a eliminar el parametro doble de dteday, que tenemos despues de hacer el 
merge.
"""
rentals_weather_2011 = rentals_weather_2011.drop(columns=['dteday_y'])
"""
Ahora vamos a renombrar la columna dteday_x al valor que queremos dteday
en este caso en los brackets tenemos dos nombre {'nombre_antiguo': 'nuevo_nombre'}
Los brackets -> nos sirven para buscar como diccionario.
"""
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x':'dteday'})

plt.scatter(rentals_weather_2011.temp_celsius, rentals_weather_2011.cnt)

rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep=';', decimal=',')

rentals_weather_2012.shape
rentals_weather_2012.head()

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)

rentals_weather_11_12.shape
rentals_weather_11_12.head()
rentals_weather_11_12.tail()

"""
Si quisieramos reordenar las columnas despues de hacer un append podemos ejecutar
el siguiente comando.
"""
rentals_weather_11_12 = rentals_weather_11_12[rentals_weather_2011.columns]

orden = rentals_weather_2011.columns

# QC OK 2020_10_15

#para guardar podemos hacerlo de la siguiente forma
rentals_weather_11_12.to_csv("rentals2011_2012.csv")
