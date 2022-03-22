# Intro

리액트 프로젝트를 사용자에게 제공할 때는 빌드 작업을 거쳐서 배포해야 한다.

빌드 작업에선

- 불필요한 주석, 경고 메시지, 공백 등을 제거해 파일 크기 최소화
- JSX문법이나 최신 자바스크립트 문법이 원활하게 실행되도록 코드의 트랜스파일 작업 진행
- 이미지와 같은 정적 파일의 경로 설정

과 같은 일을 한다.

빌드 작업은 **웹팩** 이라는 도구가 담당한다.

- 프로젝트의 모든 자바스크립트 파일 하나로 합치기
- 프로젝트의 모든 CSS 파일 하나로 합치기

스플리팅이란?

파일을 분리하는 작업

CRA를 통해 React 프로젝트를 만들 경우 기본으로 탑재되어있는 SplitChunks 기능을 통해 스플리팅이 되지만, 단순한 캐싱 효과만 있을 뿐이다.

애플리케이션의 규모가 커질 경우에 기본적인 스플리팅 기능만 이용하면 로딩이 오래 걸리고 사용자 경험도 안좋아지고 트래픽도 나오게 된다.

이를 해결하는 방법은 **코드 비동기 로딩**!

# 1. 자바스크립트 함수 비동기 로딩

**일반 자바스크립트 함수 스플리팅 하기)**

```jsx
export default function notify() {
  alert("안녕하세요!");
}
```

**App.js 수정)**

```jsx
import React from "react";
import logo from "./logo.svg";
import "./App.css";
import notify from "./notify";

function App() {
  const onClick = () => {
    notify();
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p onClick={onClick}>Hello React!</p>
      </header>
    </div>
  );
}

export default App;
```

→ 빌드 시 notify 코드가 main 파일에 들어감

**App.js 수정)**

```jsx
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const onClick = () => {
    import("./notify").then((result) => result.default());
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p onClick={onClick}>Hello React!</p>
      </header>
    </div>
  );
}

export default App;
```

→ Hello React!를 클릭하는 시점에서 notify 불러옴

→ 빌드시 새로 시작하는 숫자 파일 안에 notify 관련 코드가 들어가게 됨(스플리팅!)

# 2. React.lazy와 Suspense를 통한 컴포넌트 스플리팅

**React.lazy** → 컴포넌트를 렌더링하는 시점에서 비동기적으로 로딩할 수 있게 해주는 유틸 함수

**Suspense** → 리액트 내장 컴포넌트로서, 코드 스플리팅된 컴포넌트를 로딩하도록 발동시킬 수 있다. 로딩이 끝나지 않았을 때 보여 줄 UI를 설정할 수 있다.

## 1) state를 사용한 코드 스플리팅

**React.lazy를 사용하지 않고 코드 스플리팅 하기)**

```jsx
import React from "react";

const SplitMe = () => {
  return <div>SplitMe</div>;
};

export default SplitMe;
```

```jsx
import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

class App extends Component {
  state = {
    SplitMe: null,
  };
  handleClick = async () => {
    const loadedModule = await import("./SplitMe");
    this.setState({
      SplitMe: loadedModule.default,
    });
  };
  render() {
    const { SplitMe } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p onClick={this.handleClick}>Hello React!</p>
          {SplitMe && <SplitMe />}
        </header>
      </div>
    );
  }
}

export default App;
```

## 2) React.lazy와 Suspense 사용하기

React.lazy와 Suspense를 사용하면 코드 스플리팅을 위한 state를 따로 선언하지 않아도 된다.

**React.lazy 컴포넌트 사용법)**

```jsx
const SplitMe = React.lazy(() => import('./SplitMe'));
```

**Suspense 사용법)**

```jsx
import React, { Suspense } from 'react';

(...)
<Suspense fallback={<div>loading...</div>}>
  <SplitMe />
</Suspense>
```

**적용하기)**

```jsx
import React, { useState, Suspense } from 'react';
import logo from './logo.svg';
import './App.css';
const SplitMe = React.lazy(() => import('./SplitMe'));

function App() {
  const [visible, setVisible] = useState(false);
  const onClick = () => {
    setVisible(true);
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p onClick={onClick}>Hello React!</p>
        <Suspense fallback={<div>loading…</div>}>
          {visible && <SplitMe />}
        </Suspense>
      </header>
    </div>
  );
}

export default App;
```

## 3) Loadable Components를 통한 코드 스플리팅

Loadable Components → 코드 스플리팅을 편하게 하도록 도와주는 서드파티 라이브러리

※ React.lazy와 Suspense는 서버 사이드 렌더링을 지원하지 않지만, Loadable Components 은 서버 사이드 렌더링을 지원한다.

> ✅ **서버 사이드 렌더링**이란?
웹 서비스의 초기 로딩 속도 개선, 캐싱 및 검색 엔진 최적화를 가능하게 해주는 기술
서버 사이드 렌더링을 사용하면 웹 서비스의 초기 렌더링을 사용자 브라우저가 아닌 서버에서 처리함.


**라이브러리 설치)**

`$ yarn add @loadable/component`

**적용하기)**

```jsx
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import loadable from '@loadable/component';

const SplitMe = loadable(() => import('./SplitMe'));

function App() {
  const [visible, setVisible] = useState(false);
  const onClick = () => {
    setVisible(true);
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p onClick={onClick}>Hello React!</p>
        {visible && <SplitMe />}
      </header>
    </div>
  );
}

export default App;
```

만약, 로딩 중 다른 UI를 보여 주고 싶다면, loadable를 사용하는 부분을 아래와 같이 수정한다.

```jsx
const SplitMe = loadable(() => import('./SplitMe'), {
  fallback: <div>loading…</div>
});
```

**preload 하기)**

preload → 컴포넌트를 미리 불러오기

```jsx
import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import loadable from "@loadable/component";
const SplitMe = loadable(() => import("./SplitMe"));

function App() {
  const [visible, setVisible] = useState(false);
  const onClick = () => {
    setVisible(true);
  };
  const onMouseOver = () => {
    SplitMe.preload();
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p onClick={onClick} onMouseOver={onMouseOver}>
          Hello React!
        </p>
        {visible && <SplitMe />}
      </header>
    </div>
  );
}

export default App;
```

**더 다양한 loadable-components 알아보기)**

[Delay - Loadable Components](https://loadable-components.com/docs/delay/)

# 퀴즈

Q1) 컴포넌트를 렌더링하는 시점에서 비동기적으로 로딩할 수 있게 해 주는 유틸함수는?

- 정답
    
    React.lazy
    

Q2) 리액트 내장 컴포넌트로써 코드 스플리팅된 컴포넌트를 로딩하도록 발동시킬 수 있는 함수는?

- 정답
    
    Suspense
