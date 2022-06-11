# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:52:34 2022

@author: Taeyoung
"""

"""
numpy : 수치 데이터를 다루기 위한 라이브러리로 다차원 배열 자료 구조인 ndarray를 지원하며 
선형대수계산 등의 행렬 연산에 주로 사용된다.
"""
import numpy as np

#리스트를 이용하여 numpy 생성
ar1 = np.array([1,2,3,4,5])
type(ar1)
ar2 = np.array([[10,20,30],[40,50,60]])
ar2

#값의 범위를 지정하여 numpy 생성
ar3 = np.arange(1,11,2)
ar3

#구조를 지정하여 numpy 생성
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2)) #3행 2열 구조 생성
ar4

#초기값과 구조를 지정하여 numpy 생성
ar5 = np.zeros((2,3)) #0으로 초기화하고 2행 3열 구조를 생성
ar5

#numpy 슬라이싱
ar6 = ar2[0:2, 0:2]
ar6

ar7 = ar2[0,:]
ar7

#numpy 사칙연산
ar8 = ar1 + 10
ar8
ar1 + ar8
ar8 - ar1
ar1*2
ar1/2

#numpy 행렬곱 연산
ar9 = np.dot(ar2, ar4)
ar9

"""
pandas : 데이터 분석에서 자주 사용하는 테이블 형태로 다룰 수 있는 라이브러리
- 1차원 자료구조 : Series
- 2차원 자료구조 : DataFrame
- 3차원 자료구조 : Panel
"""

import pandas as pd
#Series생성
data1 = [10,20,30,40,50]
data1

data2=['1반','2반','3반','4반','5반']
data2

#리스트를 이용하여 Series 생성
sr1 = pd.Series(data1)
sr2 = pd.Series(data2)

#값을 이용하여 Series 생성
sr3 = pd.Series([101, 102, 103, 104, 105])
sr3

sr4 = pd.Series(['월', '화','수','목','금'])
sr4

#인덱스를 지정하여 Series 생성
sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
sr5

sr6 = pd.Series(data1, index=data2)
sr6

sr7 = pd.Series(data2, index=data1)
sr7

sr8 = pd.Series(data2, index=sr4)
sr8

#Series 인덱싱
sr8[2]

sr8['수']

sr8[-1]

#Series 슬라이싱
sr8[0:4]

#Series 인덱스 구하기
sr8.index

#Series 값 구하기
sr8.values

#Series 원소가 숫자면 덧셈 수행
sr1 + sr3

#Series 원소가 문자열이면 문자열 연결 수행
sr4 + sr2


"""
DataFrame
"""
data_dic = {
    'year' : [2018, 2019, 2020],
    'sales': [350, 480, 1099]
    }

#딕셔너리를 이용하여 DataFrame 생성
df1 = pd.DataFrame(data_dic)
df1

#리스트를 이용하여 DataFrame 생성
df2 = pd.DataFrame([
    [89.2, 92.5, 90.8],
    [92.8, 89.9, 95.2]
    ], index=['중간고사','기말고사'],columns = data2[0:3])
df2

#리스트를 이용하여 DataFrame 생성2
data_df = [['20201101', 'Hong', '90', '95'],['20201102', 'Kim', '93', '94'],
           ['20201103','Lee', '87', '97']]
df3 = pd.DataFrame(data_df)

#DataFrame 열 이름 설정
df3.columns = ['학번', '이름', '중간고사', '기말고사']
df3

#DataFrame 조회
df3.head(2) #위에서부터 2개 행 조회
df3.tail(2) #아래에서부터 2개 행 조회
df3['이름'] #'이름'컬럼 조회

#CSV 파일로 저장
path= 'D:\빅데이터 수업자료\기말고사대비정리\week02_파이썬프로그래밍\score.csv'
df3.to_csv(path,header='False')

#CSV 파일을 DataFrame으로 불러오기
df4 = pd.read_csv(path, encoding='utf-8', index_col=0, engine='python')
df4
"""
encoding='utf-8'(csv)
encoding='euc-kr'(excel)
"""

import pandas as pd
df = pd.DataFrame([[60,61,62], [70,71,72],[80,81,82],[90,91,92]],
                  index = ['1반','2반','3반','4반'], columns=['퀴즈1','퀴즈2','퀴즈3'])

#df - 열 단위 데이터 추출하기
df['퀴즈1']
df['퀴즈1'][2]

#df.loc - 인덱스를 기준으로 행 데이터 추출
df.loc['2반']
df.loc['2반', '퀴즈1']
df.loc['2반':'4반','퀴즈1']
type(df.loc['2반':'4반','퀴즈1'])
df.loc['2반':'4반','퀴즈1':'퀴즈2']
type(df.loc['2반':'4반','퀴즈1':'퀴즈2'])

#df.iloc - 행 번호를 기준으로 행 데이터 추출
df.iloc[2]
type(df.iloc[2])
df.iloc[2,1]
df.iloc[2:4, 0]
df.iloc[2:4, 0:2]

import pandas as pd
data2 = ['1반', '2반', '3반', '4반', '5반']

df = pd.DataFrame([[89.1,90.1,'B'], [89.2,90.2,'A'],[89.3,90.3,'A'],[89.4,90.4,'C'],[89.5,90.5,'B']],
                  index=data2, columns = ['중간고사','기말고사','성적'])

#df - 열 단위 데이터 추출하기
df['기말고사']
df.기말고사
df[['중간고사','기말고사']]
df['2반':'4반']
df['2반','4반'] #error
df['중간고사'][3]
df['중간고사']['1반':'2반']
df['1반':'2반']['중간고사']
df['중간고사'][0:2]
df[0:2]['중간고사']

#df.loc - 인덱스를 기준으로 행 데이터 추출
df.loc['5반']
df.loc['1반':'2반']
df.loc[:,'기말고사']

#df.iloc - 행 번호를 기준으로 행 데이터 추출
df.iloc[0:2]['중간고사']
df.iloc[4]

#뽑아내기
df[df['성적']=='B']
df[df.성적=='B']

df.loc[df.성적=='B']
df[df.성적.isin(['B','C'])]
df.loc[df.성적.isin(['B','C'])]
df[(df.성적 == 'A') & (df.중간고사 >= 89.3)]
df.loc[(df.성적 == 'A') & (df.중간고사 >= 90)]

#summary function and maps
df.describe()
df.중간고사.describe()
df.head(1)
df.중간고사.unique()
df_mean = df.중간고사.mean()
df.중간고사.value_counts()
df.중간고사.map(lambda p: p - df_mean)

#grouping and sorting
df.groupby('중간고사').중간고사.count()
df.groupby('중간고사').중간고사.min()
df.groupby(['중간고사']).중간고사.agg([len, min, max])
df.sort_values(by='중간고사')
df.sort_values(by='중간고사', ascending=False)
df.sort_index(ascending=False)

#data types and missing values
df.dtypes
df.중간고사.dtypes
df.loc['6반']=[10,10,np.nan]
df[pd.isnull(df.성적)]

#renaming and combining
df.rename(columns={'성적':'등급'})
df.rename_axis("반이름", axis='rows')

df1 = pd.DataFrame([
    [89.2, 92.5, 'B'],[90.8, 92.8,'A'],[89.9,95.2,'A'],[89.9, 85.2,'C'],[89.9,90.2,'B']
    ],
                   index=['1반','2반','3반','4반','5반'], columns=['중간고사','기말고사','성적'])

df0 = pd.concat([df,df1])
