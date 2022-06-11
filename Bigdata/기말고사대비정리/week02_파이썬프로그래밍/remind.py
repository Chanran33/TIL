# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:23:06 2022

@author: Taeyoung

딕셔너리 자료형 복습
"""

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

"""
집합 자료형 복습
"""
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

"""
내장함수 복습
"""
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