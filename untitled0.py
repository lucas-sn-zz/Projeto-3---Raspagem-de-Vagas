#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:22:26 2018

@author: lucassn
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv('dados3.csv', sep = ',', encoding = 'ISO-8859-1')

sns.heatmap(y = 'peso', x ='codigo_origem',  data = tabela)
sns.clustermap(tabela)