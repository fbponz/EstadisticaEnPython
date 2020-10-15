#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:02:44 2020

@author: franciscodeborjaponz
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Tarea 0, apartado 2.

Descargar dos ficheros csv desde kaggle.com:
- Ultra Trail Mont Blanc. Clasificación desde 2003 hasta 2017.
https://www.kaggle.com/ceruleansea/ultratrail-du-montblanc-20032017?select=utmb_2017.csv

-Ultra Trail Mont Blanc, Clasificación desde 2017 hasta 2019.
https://www.kaggle.com/purpleyupi/utmb-results

Datos guardados en 'Data/csv/*.csv'
"""

"""
Tarea 0, apartado 3.

Importar los datos y replicar alguna estadística descriptiva sencilla de las que
aparecen en el explorador de datos de Kaggle.
"""
utmb_2003_results = pd.read_csv('Data/csv/utmb_2003.csv', sep=',', decimal='.')
utmb_2004_results = pd.read_csv('Data/csv/utmb_2004.csv', sep=',', decimal='.')
utmb_2005_results = pd.read_csv('Data/csv/utmb_2005.csv', sep=',', decimal='.')
utmb_2006_results = pd.read_csv('Data/csv/utmb_2006.csv', sep=',', decimal='.')
utmb_2007_results = pd.read_csv('Data/csv/utmb_2007.csv', sep=',', decimal='.')
utmb_2008_results = pd.read_csv('Data/csv/utmb_2008.csv', sep=',', decimal='.')
utmb_2009_results = pd.read_csv('Data/csv/utmb_2009.csv', sep=',', decimal='.')
utmb_2010_results = pd.read_csv('Data/csv/utmb_2010.csv', sep=',', decimal='.')
utmb_2011_results = pd.read_csv('Data/csv/utmb_2011.csv', sep=',', decimal='.')
utmb_2012_results = pd.read_csv('Data/csv/utmb_2012.csv', sep=',', decimal='.')
utmb_2013_results = pd.read_csv('Data/csv/utmb_2013.csv', sep=',', decimal='.')
utmb_2014_results = pd.read_csv('Data/csv/utmb_2014.csv', sep=',', decimal='.')
utmb_2015_results = pd.read_csv('Data/csv/utmb_2015.csv', sep=',', decimal='.')
utmb_2016_results = pd.read_csv('Data/csv/utmb_2016.csv', sep=',', decimal='.')
utmb_2017_results = pd.read_csv('Data/csv/utmb_2017.csv', sep=',', decimal='.')
utmb_2017b_results = pd.read_csv('Data/csv/utmb_2017_s2.csv', sep=',', decimal='.')
utmb_2018b_results = pd.read_csv('Data/csv/utmb_2018_s2.csv', sep=',', decimal='.')
utmb_2019b_results = pd.read_csv('Data/csv/utmb_2019_s2.csv', sep=',', decimal='.')

utmb_2003_results = utmb_2003_results.filter(['name','nationality','time'])
utmb_2004_results = utmb_2004_results.filter(['name','nationality','time'])
utmb_2005_results = utmb_2005_results.filter(['name','nationality','time'])
utmb_2006_results = utmb_2006_results.filter(['name','nationality','time'])
utmb_2007_results = utmb_2007_results.filter(['name','nationality','time'])
utmb_2008_results = utmb_2008_results.filter(['name','nationality','time'])
utmb_2009_results = utmb_2009_results.filter(['name','nationality','time'])
utmb_2010_results = utmb_2010_results.filter(['name','nationality','time'])
utmb_2011_results = utmb_2011_results.filter(['name','nationality','time'])
utmb_2012_results = utmb_2012_results.filter(['name','nationality','time'])
utmb_2013_results = utmb_2013_results.filter(['name','nationality','time'])
utmb_2014_results = utmb_2014_results.filter(['name','nationality','time'])
utmb_2015_results = utmb_2015_results.filter(['name','nationality','time'])
utmb_2016_results = utmb_2016_results.filter(['name','nationality','time'])
utmb_2017_results = utmb_2017_results.filter(['name','nationality','time'])
utmb_2017b_results = utmb_2017b_results.filter(['Surname First name Club / Team','Nationality','Time'])
utmb_2018b_results = utmb_2018b_results.filter(['Surname First name Club / Team','Nationality','Time'])
utmb_2019b_results = utmb_2019b_results.filter(['Surname First name Club / Team','Nationality','Time'])