# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:44:24 2020

@author: Borja
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
- Ultra Trail Mont Blanc. Clasificación desde 2003 hasta 2017.
https://www.kaggle.com/ceruleansea/ultratrail-du-montblanc-20032017?select=utmb_2017.csv

-Ultra Trail Mont Blanc, Clasificación desde 2017 hasta 2019.
https://www.kaggle.com/purpleyupi/utmb-results

Datos guardados en 'Data/csv/*.csv'
"""
utmb_2003 = pd.read_csv('Data/csv/utmb_2003.csv', sep=',', decimal='.')
utmb_2004 = pd.read_csv('Data/csv/utmb_2004.csv', sep=',', decimal='.')
utmb_2005 = pd.read_csv('Data/csv/utmb_2005.csv', sep=',', decimal='.')
utmb_2006 = pd.read_csv('Data/csv/utmb_2006.csv', sep=',', decimal='.')
utmb_2007 = pd.read_csv('Data/csv/utmb_2007.csv', sep=',', decimal='.')
utmb_2008 = pd.read_csv('Data/csv/utmb_2008.csv', sep=',', decimal='.')
utmb_2009 = pd.read_csv('Data/csv/utmb_2009.csv', sep=',', decimal='.')
utmb_2010 = pd.read_csv('Data/csv/utmb_2010.csv', sep=',', decimal='.')
utmb_2011 = pd.read_csv('Data/csv/utmb_2011.csv', sep=',', decimal='.')
utmb_2012 = pd.read_csv('Data/csv/utmb_2012.csv', sep=',', decimal='.')
utmb_2013 = pd.read_csv('Data/csv/utmb_2013.csv', sep=',', decimal='.')
utmb_2014 = pd.read_csv('Data/csv/utmb_2014.csv', sep=',', decimal='.')
utmb_2015 = pd.read_csv('Data/csv/utmb_2015.csv', sep=',', decimal='.')
utmb_2016 = pd.read_csv('Data/csv/utmb_2016.csv', sep=',', decimal='.')
utmb_2017 = pd.read_csv('Data/csv/utmb_2017.csv', sep=',', decimal='.')

"""
Los datos obtenidos de la segunda fuente contienen en una celda el nombre del
corredor y seguido por un espacio también el nombre del equipo que pertenecen.
"""
def clean_data(utmb_year):
    name_s2 = utmb_year["name"]
    nationality_s2 = utmb_year["nationality"]
    time_s2 = utmb_year["time"]
    data_cleaned_year = pd.DataFrame({"name": name_s2, "nationality": nationality_s2, "time": time_s2})
    del(name_s2)
    del(nationality_s2)
    del(time_s2)
    return data_cleaned_year

def rename_column(utmb_year, string_old, string_new):
    utmb_year = utmb_year.rename(columns={string_old:string_new})
    return utmb_year

def clean_and_rename_data(utmb_year, string_new):
    utmb_year_clean = clean_data(utmb_year)
    utmb_year_clean = rename_column(utmb_year_clean, 'time', string_new)
    return utmb_year_clean


utmb_clean_2003 = clean_and_rename_data(utmb_2003, 'time_2003')
utmb_clean_2004 = clean_and_rename_data(utmb_2004, 'time_2004')
utmb_clean_2005 = clean_and_rename_data(utmb_2005, 'time_2005')
utmb_clean_2006 = clean_and_rename_data(utmb_2006, 'time_2006')
utmb_clean_2007 = clean_and_rename_data(utmb_2007, 'time_2007')
utmb_clean_2008 = clean_and_rename_data(utmb_2008, 'time_2008')
utmb_clean_2009 = clean_and_rename_data(utmb_2009, 'time_2009')
utmb_clean_2010 = clean_and_rename_data(utmb_2010, 'time_2010')
utmb_clean_2011 = clean_and_rename_data(utmb_2011, 'time_2011')
utmb_clean_2012 = clean_and_rename_data(utmb_2012, 'time_2012')
utmb_clean_2013 = clean_and_rename_data(utmb_2013, 'time_2013')
utmb_clean_2014 = clean_and_rename_data(utmb_2014, 'time_2014')
utmb_clean_2015 = clean_and_rename_data(utmb_2015, 'time_2015')
utmb_clean_2016 = clean_and_rename_data(utmb_2016, 'time_2016')
utmb_clean_2017 = clean_and_rename_data(utmb_2017, 'time_2017')

"""
Merge all the data in a single data frame.
"""
utmb_clean_multiyear = pd.merge(utmb_clean_2003, utmb_clean_2004,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2005,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2006,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2007,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2008,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2009,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2010,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2011,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2012,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2013,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2014,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2015,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2016,how='outer',on=['name', 'nationality'], copy=True)
utmb_clean_multiyear = pd.merge(utmb_clean_multiyear, utmb_clean_2017,how='outer',on=['name', 'nationality'], copy=True)