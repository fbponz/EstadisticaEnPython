#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 11:55:19 2020

@author: franciscodeborjaponz
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Tarea 0, apartado 4. Importar desde un fichero Excel a un pandas data frame.

"""
economics_data = pd.read_excel('Data/xlsx/Exchange_rate.xlsx', index_col=0)
