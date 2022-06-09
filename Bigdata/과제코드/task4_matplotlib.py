# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:19:39 2022

@author: User
"""

import csv
f1=open('201403.csv')
f2=open('202103.csv')

data1 = csv.reader(f1)
next(data1)

data2 = csv.reader(f2)
next(data2)

result2014 = []
result2021 = []
bar = []

for row in data1:
    result2014.append(int(row[1].replace(',','')))
    bar.append((row[0].split('('))[0])

for row in data2:
    result2021.append(int(row[1].replace(',', '')))

import numpy as np
re2014 = np.array(result2014)
re2021 = np.array(result2021)
result = re2021-re2014

print(re2021-re2014)
print(bar)

import matplotlib.pyplot as plt
plt.bar(bar, result)
plt.xticks(rotation=90)

for i in range(18):
    plt.text(i,result[i],result[i]//10000)
    
plt.show()

