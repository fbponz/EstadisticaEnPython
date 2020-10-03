# -*- coding: utf-8 -*-
"""
Esto es un comentario
@author: fbponz
This is a script used during the first leason.
"""
#%% Bloque variables.
"""
variable
"""
a = 3
b = 2

"""
Operaciones con variables
"""
c = a + b
"""
En caso de concatenar estas invocaciones, solo muestra el ultimo.
"""
a
b
c
#%% Bloque de variables string.
"""
En caso de concatenar estos print, muestra todos los valores
"""
print (a)
print (b)
print (c)

"Utilización de strings"
a = "Hello"
b = 'World!'
c = " "
d = a + c + b  # Comentario de una linea.
print (d)

#%% Bloque limpieza
del (a,b,c,d) #Si alguna de las variables ya está borrada nos devolvera un error.
#%reset -f #es una CLI de spyder que sirve para resetear por completo el entorno.

#%% Importación de librerias
#Cargar las librerias basicas para está asignatura
"""
Importamos una libreria con un nickname
Import $liberia as $nickname.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Listas
name = ['Yaling','Sofia','Maria','Pablo', 'Inés'] #En python lista, en pandas series.
age = [28,23,25,23, 25] 
gender=['Female','Female','Female','Male','Female']

#Los casos por filas
#Las caracteristicas por columnas

"""
#Pandas Dataframe
#pd.DataFrame es una función
#donde le pasamos un diccionario { }
#Debemos evitar gastar nombres no descriptivos o incluir guiones/espacios en 
                                                                   los nombres.
#Si hacemos doble click en la variable clase 2020 podemos observar los datos 
                                                                como una tabla.
"""
clase2020 = pd.DataFrame({'name' : name, 'age' : age, 'gender' : gender})
"""
#ahora que ya tenemos la información metida en un Dataframe debemos limpiar 
                                                  variables de nuestro entorno.
"""
del(age,gender,name)

#Podemos acceder a las variables de un Dataframe de la manera siguiente.
age = clase2020.age
"""
El siguiente estudiante nos devuelve la dimensionalidad del objeto (numero 
                    total de elementos, y de caracteristicas de cada elemento).

"""
clase2020.shape
"""
El siguiente comando nos devuelve las primeras 5, si le pasamos sin parametro
mientras que si le especificamos  un numero en los brackets, nos devuelve X 
elementos del principio.
"""
clase2020.head()
"""
El siguiente comando nos devuelve los ultimos 5, si le pasamos sin parametro
mientras que si le especificamos  un numero en los brackets, nos devuelve X 
elementos del final.
"""
clase2020.tail()
#Alberto's Tips: escribe un comentario para estár seguro
#QC OK (Control de calidad OK).

#obtener el directorio de trabajo.
cwd = os.getcwd()
os.chdir(cwd)
os.getcwd()

#guardar el Dataframe a excel / csv(Formato estandar).
#clase2020.to_excel("clases2020.xlsx")
clase2020.to_csv("clase2020.csv") #Durante esta asignatura vamos a gastar CSV's

