# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 00:25:50 2022

@author: USER
"""

#1.데이터 읽어오기
import pandas as pd
data = pd.read_csv("age.csv", encoding='cp949')

#2.궁금한 지역의 이름 입력받기
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성

#3. 궁금한 지역의 인구 구조를 저장한다.
for i in range(len(data)):
    if name in data.iloc[i][0]:
        areaname=data.iloc[i][0]
        for j in data.iloc[i][3:]:
            home.append(int(j))
        hometotal = int(data.iloc[i][2])
print(hometotal) 
for k in range(len(home)):
    home[k]=(home[k]/hometotal)        
    
#4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
result_list=[]
for row in range(len(data)):
    away=[]
    for i in data.iloc[row][3:]:
        away.append(int(i))
    awaytotal=int(data.iloc[row][2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    s=0
    for j in range(len(away)):
        s += ((home[j]-away[j])**2)
    result_list.append([data.iloc[row][0],away,s])
result_list.sort(key=lambda s: s[2])
print(result_list[0][0])

#5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)            
plt.rc('font', family ='Malgun Gothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(result_list[1][1], label = result_list[1][0])
plt.plot(result_list[2][1], label = result_list[2][0])
plt.plot(result_list[3][1], label = result_list[3][0])
plt.plot(result_list[3][1], label = result_list[4][0])
plt.plot(result_list[3][1], label = result_list[5][0])
plt.legend()
plt.show()
