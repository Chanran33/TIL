# 들어가기전

## Context API란?

**리액트 프로젝트에서 전역적으로 사용할 데이터가 있을 때 유용한 기능**

ex) 사용자 로그인 정보, 애플리케이션 환경 설정, 테마

**Context API를 기반으로 구현된 것들**

→ 리덕스, 리액트 라우터, styled-components

# 1. Context API를 사용한 전역 상태 관리 흐름 이해하기

**일반적인 전역 상태 관리 흐름)**

<img src="https://user-images.githubusercontent.com/49816869/148258787-cfcd9a42-eb81-4949-a39c-83f2e8151ad3.png" width="300px">
                                                                                                                         
ex) App이 지닌 state값을 F, J, G로 전달

**F** : App → A → B → F

**J** : App → H → J

**G** : App → A→ B → E → G.

를 거쳐야 한다.

**Context API를 사용한 전역 상태 관리 흐름)**

<img src="https://user-images.githubusercontent.com/49816869/148259284-190a25e5-285d-450d-adfa-fe2c569b520a.png" width="300px">

Context를 생성해 한 번에 어느 컴포넌트든 한 번에 원하는 값을 받아 와서 사용할 수 있다.

# 2. Context API 사용법 익히기

# 3. 동적 Context 사용하기

# 4. Consumer 대신 Hook 또는 static contextType 사용하기
