# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:24:12 2022

@author: taeyoung

9주차 과제 연습문제2)

다중선형회귀분석 모델을 만드는 프로그램을 수행해보기.


"""

from sklearn import linear_model
from sklearn import datasets
from sklearn.metrics import mean_squared_error
import pandas as pd
diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data)
y = diabetes_data.target
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X = pd.DataFrame(X), y = y)
prediction = linear_regression.predict(X = pd.DataFrame(X))
print('a value = ', linear_regression.intercept_)
print('b balue =', linear_regression.coef_)
residuals = y-prediction
SSE = (residuals**2).sum(); 
SST = ((y-y.mean())**2).sum()
R_squared = 1- (SSE/SST)
print('R_squared = ', R_squared)
print('score = ', linear_regression.score(X = pd.DataFrame(X), y = y))
print('Mean_Squared_Error = ', mean_squared_error(prediction, y))
print('RMSE = ', mean_squared_error(prediction, y)**0.5)

from sklearn import linear_model
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data)
y = diabetes_data.target

#split 하기
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#모델 생성
linear_regression = linear_model.LinearRegression()
#모델 훈련
linear_regression.fit(X = pd.DataFrame(X_train), y = Y_train)
#예측결과 구하기
prediction = linear_regression.predict(X = pd.DataFrame(X_test))
print('a value = ', linear_regression.intercept_)
print('b balue =', linear_regression.coef_)

# 실제 y값과 예측한 y값을 비교하여 잔차(residuals)를 구한다.
residuals = Y_test-prediction
# 잔차를 제곱하여 전체를 합침. 결과값을 SSE라는 변수에 할당
SSE = (residuals**2).sum(); 
SST = ((y-y.mean())**2).sum()
R_squared = 1- (SSE/SST)
print('R_squared = ', R_squared)
print('score = ', linear_regression.score(X = pd.DataFrame(X), y = y))
print('Mean_Squared_Error = ', mean_squared_error(prediction, Y_test))
# Mean squared error의 제곱근 값을 구함
print('RMSE = ', mean_squared_error(prediction, Y_test)**0.5)