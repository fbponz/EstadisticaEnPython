#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:31:50 2020

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

utmb_2017_results = pd.read_csv('Data/csv/utmb_2017.csv', sep=',', decimal='.')


df_percent_country = utmb_2017_results.nationality
plt.hist(df_percent_country)

"""
Forma de calcular el porcentaje por pais
"""
temporal_data = utmb_2017_results.nationality
counts = temporal_data.value_counts()
percent = temporal_data.value_counts(normalize=True)
percent100 = temporal_data.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
percent_country = pd.DataFrame({'counts': counts, 'percentage': percent, 'percentage100': percent100})

