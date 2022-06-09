# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:41:27 2022

@author: taeyoung

9주차 과제 연습문제1)
인구밀도와 절도발생률 간의 관계를 연구하면서 16개의 도시 자료 수집

X:{ 59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70}
Y:{ 209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204}

X는 해당 도시의 단위 면적당 "인구 밀도"
Y는 이전 년도의 10만명 당 절도 "범죄 발생횟수"


"""
from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

#2차원 배열을 만들어 'data' 변수에 할당
data = { 'X' : [59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70],
         'Y' : [209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204]}

#data 변수를 data frame 형태로 변환
data = pd.DataFrame(data)

#산점도 그리기
data.plot(kind="scatter", x="X", y='Y', figsize=(5,5), color="blue")

#linear_model 모듈이 포함하고 있는 Linearregression() 함수를 'linear_regression'이라고 하는 변수에 할당
linear_regression = linear_model.LinearRegression()
# Linearregression()의 fit()이라는 함수를 이용하여 선형회귀 모델 훈련 실행
linear_regression.fit(X=pd.DataFrame(data["X"]), y=data["Y"])

#선형 회귀식의 세로축 절편
print('a value = ', linear_regression.intercept_)

#선형 회귀식의 기울기
print('b balue =', linear_regression.coef_)

#선형 회귀 값 구하기
prediction = linear_regression.predict(X = pd.DataFrame(data["X"]))
print(prediction)

#실제 Y값과 예측한 Y값을 비교하여 잔차(residuals)구하기
residuals = data["Y"] - prediction
print(residuals)

residuals.describe()

SSE = (residuals**2).sum()
print("SSE = ", SSE)

SST = ((data["Y"]-data["Y"].mean())**2).sum()
print("SST = ", SST)

R_squared = 1 - (SSE/SST)
print('R_squared = ', R_squared)

data.plot(kind="scatter",x="X",y="Y",figsize=(5,5),color="red")
# Plot regression line
plt.plot(data["X"],prediction,color="blue")

from sklearn.metrics import mean_squared_error

print('score = ', linear_regression.score(X = pd.DataFrame(data["X"]), y = data["Y"]))

print('Mean_Squared_Error = ', mean_squared_error(prediction, data['Y']))

print('RMSE = ', mean_squared_error(prediction, data['Y'])**0.5)

#예측하기
mydata = {'X' : [58.0],
        'Y' : []}
prediction = linear_regression.predict(X = pd.DataFrame(mydata["X"]))
print("X값이 58일 때 Y값 예측=>", prediction)