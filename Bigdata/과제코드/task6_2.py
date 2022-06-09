# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:27:04 2022

@author: USER
"""

import csv
import matplotlib.pyplot as plt
f = open('중국_방한외래관광객_2017_202112.csv')
data = csv.reader(f)
next(data)

visitdays=[]
visitcount=[]
rows=[]

for row in data:
    visitdays.append(row[2])
    visitcount.append(int(row[3]))

print(visitdays)
print(visitcount)

plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('Visitors')
plt.bar(range(48),visitcount,color='g')
plt.xticks(range(48),visitdays, rotation = 90)
plt.show()
