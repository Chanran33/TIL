# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:43:22 2022

@author: User
"""
import pandas as pd

#[질의 3-1]emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

#[질의 3-2]SELECT * FROM Emp;
emp
#emp[:]
#emp[:][:]

#[질의 3-3]SELECT ename FROM Emp;
emp['ENAME']
#emp['ENAME'][:]
#emp.ENAME
#emp.loc[:,'ENAME']
#emp.loc[0:13,'ENAME']
#emp.iloc[:,1]
#emp.iloc[0:14,1]

#[질의 3-4]SELECT ename, sal FROM Emp;
emp[['ENAME','SAL']]
#emp.loc[:,['ename','sal']]
#emp.iloc[:,['ename','sal']]
#emp.iloc[:,[1,5]]

#[질의 3-5]SELECT DISTINCT job From Emp;
emp['JOB'].drop_duplicates()
#dir(emp['JOB'])

#[질의 3-6] SELECT * FROM EMP WHERE sal < 2000;
emp[emp['SAL'] < 2000]

#[질의 3-7] SELECT * FROM EMP WHERE sal BETWEEN 1000 AND 2000;
emp[emp['SAL'].between(1000,2000)]

#[질의3-8] SELECT * FROM Emp WHERE sal >= 1500 AND job= ‘SALESMAN’;
emp.loc[(emp.SAL >=1500) & (emp.JOB == 'SALESMAN')]

#[질의 3-9] SELECT * FROM EMP WHERE JOB IN ('MANAGER','CLERK');
emp.loc[emp.JOB.isin(['MANAGER', 'CLERK'])]

#[질의3-10] SELECT * FROM Emp WHERE job NOT IN ('MANAGER', 'CLERK');
emp.loc[~(emp.JOB.isin(['MANAGER', 'CLERK']))]

#[질의 3-11] SELECT ename, job FROM Emp WHERE enam LIKE 'BLAKE';
emp[['ENAME', 'JOB']][emp['ENAME']=='BLAKE']

#[질의 3-12] SELECT ename, job FROM EMP WHERE NAME LIKE '%AR%';
emp[['ENAME', 'JOB']][emp['ENAME'].str.contains('AR')]

#[질의3-13] SELECT * FROM Emp WHERE ename LIKE '%AR%' AND sal >= 2000;
emp[(emp['ENAME'].str.contains('AR'))&(emp['SAL']>=2000)]

#[질의3-14] SELECT * FROM Emp ORDER BY ename;
emp.sort_values('ENAME')

#[질의 3-15] SELECT SUM(sal) FROM emp;
emp['SAL'].sum()

#[질의 3-16] SELECT SUM(sal) FROM EMP WHERE JOB LIKE 'SALESMAN';
emp['SAL'][emp['JOB']=='SALESMAN'].sum()

#[질의3-17] SELECT SUM(sal), AVG(sal), MIN(sal), MAX(sal) FROM Emp;
emp.SAL.sum()
emp.SAL.mean()
emp.SAL.min()
emp.SAL.max()

#[질의3-18] SELECT COUNT(*) FROM Emp;
emp.count()

#[질의 3-19] SELECT COUNT(*), SUM(sal) FROM EMP GROUP BY job;
#문장2개
emp.groupby('JOB')['EMPNO'].count()
emp.groupby('JOB')["SAL"].sum()

#[질의 3-20] SELECT * FROM Emp WHERE comm IS NOT NULL;
emp[~emp['COMM'].isnull()]

#[질의 4-1] emp에 age 열을 만들어 다음을 입력하여라(14명)[30,40,50,30,40,50,30,40,50,30,40,50,30,40]
emp['age']=[30,40,50,30,40,50,30,40,50,30,40,50,30,40]

#[질의 4-2] INSERT INTO Emp(empno, name, job) Values (9999, ‘ALLEN’, ‘SALESMAN’)
emp=emp.append(pd.DataFrame(data=[[9999,'ALLEN','SALESMAN']], columns=['EMPNO', 'ENAME', 'JOB']))

#[질의 4-3] emp의 ename=‘ALLEN’ 행을 삭제하여라
#(DELETE FROM emp WHERE ename LIKE ‘ALLEN’;
emp=emp[~(emp['ENAME']=='ALLEN')]

#[질의 4-4] emp의 hiredate 열을 삭제하여라
#(ALTER TABLE emp DROP COLUMN hiredate;)
emp=emp.drop(columns='HIREDATE')

#[질의 4-5] emp의 ename=‘SCOTT’의 sal을 3000으로 변경하여라
#(UPDATE emp SET sal=3000 WHERE ename LIKE ‘SCOTT’;]
emp.loc[(emp['ENAME']=='SCOTT'),'SAL']=3000

#[질의 5-1] emp의 sal 컬럼을 oldsal 이름으로 변경하여라. 
#(ALTER TABLE emp RENAME sal TO oldsal;)
emp=emp.rename(columns={'SAL':"OLDSAL"})

#[질의 5-2] emp에 newsal 컬럼을 추가하여라, 값은 oldsal 컬럼값
#(ALTER TABLE emp ADD newsal …;)
emp['NEWSAL']=emp['OLDSAL']

#[질의 5-3] emp의 oldsal 컬럼을 삭제하여라
#(ALTER TABLE emp DROP COLUMN oldsal;)
emp=emp.drop('OLDSAL', axis=1)
