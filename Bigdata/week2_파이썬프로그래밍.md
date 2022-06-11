# 2주차 파이썬 프로그래밍

### 딕셔너리 자료형 복습

```python
#딕셔너리 만들기
dic={'name':'Hong', 'phone':'01012345678','birth':'0814'}

#원소추가
dic[1] = 'a'
dic

dic['pet'] = 'dog'
dic

#원소 삭제
del dic[1]
dic

#원소의 value 구하기
dic['pet']
dic['name']

#key의 리스트 만들기
dic.keys()
list(dic.keys())

#value의 리스트 만들기
dic.values()
list(dic.values())

#key, value 쌍 구하기
dic.items()

#원소 삭제
dic.clear()
```

### 집합 자료형 복습

```python
s1={1,2,'a',5}
s2=set([1,2,3,4,5,6])
s3=set([4,5,6,7,8,9])

#교집합 연산
s2&s3
s2.intersection(s3)

#합집합 연산
s2|s3
s2.union(s3)

#차집합 연산
s2-s3
s2.difference(s3)

#원소 한개 추가
s2.add(7)
s2

#원소 여러개 추가
s2.update([6,7,8,9,10])
s2

#특정 원소 제거
s2.remove(7)
s2
```

### 내장 함수 복습

```python
#abs(x) : 숫자 x의 절대값을 반환
abs(-3.5)

#all(iterable_x) : 그룹 자료형의 변수 x의 모든 원소가 참(0이 아닌 값)이면 True 반환
all([1,2,3,4])
all([4,-2,0.0,4])

#any(iterable_x) : 그룹 자료형의 변수 x의 원소 중 하나라도 참이면 True 반환
any([1,2,3,4])
any([4,-2,0.0,4])

#chr(x) : 아스키코드 값 x에 대한 문자 출력
chr(97)
chr(48)

#dir(x) : 객체 x가 가진 멤버 변수와 멤버 함수 보여주기
dir([1,2,3])
dir({'1':'a'})
dir(1)

#divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플로 변환
divmod(7, 3)
divmod(1.3, 0.2)

#oct(x) : 정수값 x를 8진수로 변환하여 반환
oct(8)
oct(234)

#hex(x) : 정수값 x를 16진수로 변환하여 반환
hex(16)
hex(234)

#id(object) : object(객체)의 주소값을 반환
a=3
id(a)

#int(x) : x를 정수 형태로 반환
int('3')

#str(x) : x를 문자열 형태로 반환
str(3)

#list(x) : x를 리스트로 반환
list("Python")
list([1,2,3])

#tuple(x) : x를 튜플로 반환
tuple("Python")
tuple([1,2,3])

#lambda : 간단한 삽입형 함수 생성
sum = lambda a,b: a+b
sum
sum(3,5)

#max(iterable_x) : 반복 가능한 그룹 자료형 x를 입력받은 뒤 최대값을 반환
max([1,4,2,8,6])
max("Python")

#min(iterable_x) : 반복 가능한 그룹 자료형 x를 입력받은 뒤 최소값을 반환
min([1,4,2,8,6])
min("Python")

#pow(x,y) : x의 y제곱 결과값 반환
pow(2,4)

#input() : 사용자 입력으로 받은 값을 문자열로 반환
c=input()
c
c=input("정수를 입력하세요: ")
c

#range(x) : 입력받은 숫자에 해당되는 범위의 값을 반환
range(5)
list(range(5))
list(range(5,10))
list(range(5,10,2))

#len(s) : 입력값 s의 길이를 반환
len('Python')

#sorted(iterable_x) : 입력값을 정렬하여 리스트로 반환
sorted([3,0,2,1])
sorted('Python')
```

### 데이터 분석을 위한 주요 라이브러리(numpy, pandas, matplotlib)

**numpy**

```python
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
```

**pandas - Series**

```python
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
```

**pandas - DataFrame**

```python
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
```

( + 추가)

```python
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
```

( + 추가)

```python
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
```

**matplotlib**