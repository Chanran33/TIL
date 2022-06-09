# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 01:38:30 2022

@author: User
"""

import pandas as pd
data1 = pd.read_csv("201403.csv", encoding='cp949')
data2 = pd.read_csv("202103.csv", encoding='cp949')

total2014 = []
total2021 = []
bar = []

print((data1.iloc[0][0]).split('(')[0])

for i in range(18):
    total2014.append(int(data1.iloc[i][1].replace(',','')))
    bar.append((data1.iloc[i][0]).split('(')[0])
    
for i in range(18):
    total2021.append(int(data2.iloc[i][1].replace(',','')))



import numpy as np
re2014 = np.array(total2014)
re2021 = np.array(total2021)
result = re2021-re2014

print(bar)

import matplotlib.pyplot as plt
plt.bar(bar, result)
plt.xticks(rotation=90)

for i in range(18):
    plt.text(i,result[i],result[i]//10000)
    
plt.show()