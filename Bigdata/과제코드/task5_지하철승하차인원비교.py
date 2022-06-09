# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:07:46 2022

@author: USER
"""

import csv

#2020ver.
f = open('202003subwaytime.csv')
data = csv.reader(f)
next(data)#사용월, 호선명, 역 ID, 지하철역, 시간들
next(data)#승차, 하차
s_in2020 = [0]*24
s_out2020 = [0]*24

#comma가 포함된 데이터 int로 변환
row2020 = []
for row in data:
    r=[]
    for i in row[4:52]:
        r.append(int(i.replace(',', '')))
    row2020.append(r)    
        
print(row2020)

for row in row2020:
    for i in range(24):
        s_in2020[i] += row[i*2]
        s_out2020[i] += row[1+i*2]
print(s_in2020)
print(s_out2020)

#2021ver.
f1 = open('202103subwaytime.csv')
data1 = csv.reader(f1)
next(data1)#사용월, 호선명, 역 ID, 지하철역, 시간들
next(data1)#승차, 하차
s_in2021 = [0]*24
s_out2021 = [0]*24

#comma가 포함된 데이터 int로 변환
row2021 = []
for row in data1:
    r=[]
    for i in row[4:52]:
        r.append(int(i.replace(',', '')))
    row2021.append(r)    
        
print(row2021)

for row in row2021:
    for i in range(24):
        s_in2021[i] += row[i*2]
        s_out2021[i] += row[1+i*2]
print(s_in2021)
print(s_out2021)

#2022ver.
f2 = open('202203subwaytime.csv')
data2 = csv.reader(f2)
next(data2)#사용월, 호선명, 역 ID, 지하철역, 시간들
next(data2)#승차, 하차
s_in2022 = [0]*24
s_out2022 = [0]*24

#comma가 포함된 데이터 int로 변환
row2022 = []
for row in data1:
    r=[]
    for i in row[4:52]:
        r.append(int(i.replace(',', '')))
    row2022.append(r)    
        
print(row2022)

for row in row2022:
    for i in range(24):
        s_in2022[i] += row[i*2]
        s_out2022[i] += row[1+i*2]
print(s_in2022)
print(s_out2022)

    
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이(단위 1000만 명)')
plt.plot(s_in2020, label = '202003승차')
plt.plot(s_out2020, label = '202003하차')
plt.plot(s_in2021, label = '202103승차')
plt.plot(s_out2021, label = '202103하차')
plt.plot(s_in2021, label = '202203승차')
plt.plot(s_out2021, label = '202203하차')
plt.legend()
plt.xticks(range(24), range(4,28))
plt.show()
