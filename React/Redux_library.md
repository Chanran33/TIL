# 1. 리덕스 개념 정리

**리덕스란?**

가장 많이 사용하는 리액트 상태 관리 라이브러리

- 리덕스를 사용해 컴포넌트의 상태 업데이트 관련 로직을 다른 파일로 분리시켜 더욱 효율적으로 관리할 수 있다.
- 컴포넌트끼리 똑같은 상태를 공유해야  할 때, 여러 컴포넌트를 거치지 않고 손쉽게 상태 값을 전달하거나 업데이트할 수 있다.

**리덕스는 언제 사용하나?**

단순히 전역 상태 관리만 한다면 Context API를 사용하는 것으로 충분하지만, 

리덕스를 사용하면 상태를 더욱 체계적으로 관리할 수 있어서, 프로젝트이 규모가 클 경우엔 리덕스를 사용하는 것이 좋다.

**리덕스 이용의 장점**

- 코드의 유지 보수성을 높여주어 작업 효율을 극대화한다.
- 편리한 개발자 도구를 지원한다.
- 미들웨어 기능을 제공하여, 비동기 작업을 훨씬 효율적으로 관리할 수 있게 한다.

## 1) 액션

**상태에 변화가 필요하면 액션(action)이 발생**

액션 객체의 형식)

```jsx
{
	type: 'TOGGLE_VALUE' //필수로 가지고 있어야 함. (액션의 이름)
}
```

- type 이외의 값들은 상태 업데이트 시 참고해야 할 값이며, 작성자 마음대로 넣을 수 있다.
    
    ex) 
    
    ```jsx
    {
    	type: 'ADD_TODO',
    	data: {
    		id: 1,
    		text: '리덕스 배우기'
    	}
    }
    
    {
    	type: 'CHAGE_INPUT',
    	text: '안녕하세요'
    }
    ```
    

## 2) 액션 생성 함수

**액션 객체를 만들어 주는 함수**

```jsx
function addTodo(data){
	return {
		type: 'ADD_TODO',
		data
	};
}

//화살표 함수로도 만들 수 있다.
const changeInput = text => ({
	type: 'CHANGE_INPUT',
	text
});
```

## 3) 리듀서

**변화를 일으키는 함수**

액션을 만들어 발생시키면 리듀서가 현재 상태와 전달받은 액션 객체를 파라미터로 받아 온다.

그리고 두 값을 참고하여 새로운 상태를 만들어 반환한다.

```jsx
const initialState = {
	counter: 1
};

function reducer(state = initialState, action){
	switch(action.type){
		case INCREMENT:
			return {
				counter: state.counter + 1
			};
		default:
			return state;
	}
}
```

## 4) 스토어

**프로젝트에 리덕스를 적용하기 위해 스토어(store)를 만든다.**

- 한 개의 프로젝트에는 하나의 스토어만 가질 수 있다.
- 스토어 안에는 현재 애플리케이션 상태와 리듀서가 들어가 있다.
- 이외에도 몇 가지 중요한 내장 함수를 지닌다.

## 5) 디스패치

**스토어의 내장함수 중 하나이다.**

- dispatch(action)과 같은 형태로 액션 객체를 파라미터로 넣어 호출한다.
- ‘액션을 발생시키는 것’이라고 생각하자
- 디스패치가 호출되면 스토어는 리듀서 함수를 실행시켜 새로운 상태를 만들어 준다.

## 6) 구독

**스토어의 내장함수 중 하나이다.**

- 구독 함수 안에 리스너 함수를 파라미터로 넣어 호출하면, 이 리스너 함수가 액션이 디스패치되어 상태가 업데이트될 때마다 호출된다.

```jsx
const listener = () => {
	console.log('상태가 업데이트됨');
}
const unsubscribe = store.subscribe(listener);

unsubscribe(); //추후 구독을 비활성화할 때 함수를 호출
```

# 2. 리액트 없이 쓰는 리덕스

**리덕스는 리액트에 종속되는 라이브러리가 아니다.**

- 다른 UI라이브러리/프레임워크와 함께 사용할 수도 있다.
    
    ex) angular-redux, ember redux, Vue(Vue는 주로 vuex를 사용)
    

**리덕스는 바닐라 자바스크립트와 함께 사용할 수도 있다.**

(바닐라 자바스크립트 : 라이브러리, 프레임워크 없이 사용하는 순수 자바스크립트 그 자체)

## 1) Parcel로 프로젝트 만들기

※ Parcel 도구를 사용해 빠르게 웹 애플리케이션 프로젝트를 만들 수 있다.

`$ yarn global add parcel-bundler`

`$ npm install -g parcel-bundler`

- index.html
    
    ```jsx
    <!DOCTYPE html>
    <html>
      <body>
        <div>바닐라 자바스크립트</div>
        <script src="./index.js"></script>
      </body>
    </html>
    ```
    
- index.js
    
    ```jsx
    console.log("hello parcel");
    ```
    

**개발용 서버 실행시키기)**

`$ parcel index.html`

<img src="https://user-images.githubusercontent.com/49816869/150358028-00acf4d6-460b-4ce0-af76-a388c50e30d2.png" />

**리덕스 모듈 설치하기)**

`$ yarn add redux`

## 2) 간단하게 UI 구성하기

- index.css
    
    ```css
    .toggle {
      border: 2px solid black;
      width: 64px;
      height: 64px;
      border-radius: 32px;
      box-sizing: border-box;
    }
    
    .toggle.active {
      background: yellow;
    }
    ```
    
- index.html
    
    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="index.css" />
      </head>
      <body>
        <div class="toggle"></div>
        <hr />
        <h1>0</h1>
        <button id="increase">+1</button>
        <button id="decrease">-1</button>
        <script src="./index.js"></script>
      </body>
    </html>
    ```
    

<img src="https://user-images.githubusercontent.com/49816869/150358295-b074ed01-b399-4ef8-8f29-f00e98f8b25e.png" />

## 3) DOM 레퍼런스 만들기

이 프로젝트에선 UI를 관리하는 별도의 라이브러리를 사용하지 않기 때문에 DOM을 직접 수정해주어야 한다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDecrease = document.querySelector("#decrease");
```

## 4) 액션 타입과 액션 생성 함수 정의

프로젝트의 상태에 변화를 일으키는 것 → 액션

**액션의 이름 정의하기)**

- 액션 이름은 문자열 형태여야 한다.
- 주로 대문자로 작성하며 액션 이름은 고유해야 한다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDecrease = document.querySelector("#decrease");

const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";
```

**액션 객체를 만드는 액션 생성 함수 작성하기)**

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDecrease = document.querySelector("#decrease");

//액션
const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

//액션 생성 함수(액션 객체를 만든다.)
const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });
```

- 액션 객체는 type 값을 반드시 갖고 있어야 한다.
- 그 외에 추후 상태를 업데이트할 때 참고하고 싶은 값은 마음대로 넣는다.

## 5) 초기값 설정

초깃값의 형태는 숫자, 문자열, 객체 등등 자유이다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDecrease = document.querySelector("#decrease");

//액션
const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

//액션 생성 함수(액션 객체를 만든다.)
const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });

//초기값 설정
const initialState = {
  togggle: false,
  counter: 0,
};
```

## 6) 리듀서 함수 정의

리듀서는 변화를 일으키는 함수이다.

함수의 파라미터로 state와 action 값을 받아 온다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDecrease = document.querySelector("#decrease");

//액션
const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

//액션 생성 함수(액션 객체를 만든다.)
const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });

//초기값 설정
const initialState = {
  togggle: false,
  counter: 0,
};

//리듀서 함수 정의
//state가 undefined일 때는 initialState를 기본값으로 사용
function reducer(state = initialState, action) {
  //action.type에 따라 다른 작업을 처리함
  switch (action.type) {
    case TOGGLE_SWITCH:
      return {
        ...state, //불변성 유지를 해 준다.
        toggle: !state.toggle,
      };
    case INCREASE:
      return {
        ...state,
        counter: state.counter + action.difference,
      };
    case DECREASE:
      return {
        ...state,
        counter: state.counter - 1,
      };
    default:
      return state;
  }
}
```

- 리듀서에서는 상태의 불변성을 유지하면서 데이터에 변화를 일으켜 주어야 한다.
    - 이 때 spread 연산자를 사용하면 편하다.
    - 단, 객체의 구조가 복잡해지면( 예: object.something.inside.value) spread 연산자로 불변성을 관리하며 업데이트하는 것이 굉장히 번거로울 수 있고 코드의 가독성도 나빠지기 때문에 리덕스의 상태는 최대한 깊지 않은 구조로 진행하는 것이 좋다.
    - 객체의 구조가 복잡해지거나 배열도 함께 다루는 경우 immer 라이브러리를 사용하면 좀 더 쉽게 리듀서를 작성할 수 있다.

## 7) 스토어 만들기

- 스토어는 createStore 함수를 사용한다.

```jsx
import { createStore } from "redux";

(...)

const store = createStore(reducer);
```

## 8) render 함수 만들기

- render함수는 상태가 업데이트될 때마다 호출되며, 리액트의 reender함수와는 다르게 이미 html을 사용하여 만들어진 UI의 속성을 상태에 따라 변경해준다.

```jsx
(...)

const render = () => {
  const state = store.getState(); //현재 상태를 불러온다.
  //토글처리
  if (state.toggle) {
    divToggle.classList.add("active");
  } else {
    divToggle.classList.remove("active");
  }
  //카운터 처리
  counter.innerText = state.counter;
};

render();
```

## 9) 구독하기

스토어의 상태가 바뀔 대마다 render함수가 호출되도록 할 것이다.

이 작업은 스토어의내장 함수 subscribe를 사용하여 수행할 수 있다.

**subscribe 함수 사용 예시)**

```jsx
const listener = () => {
	console.log('상태가 업데이트됨');
}
const unsubscribe = store.subscribe(listener);

unsubscribe(); //추후 구독을 비활성화할 때 함수를 호출
```

> ✅ 이번 프로젝트에서는 subscribe 함수를 직접 사용하지만, 추후 리액트 프로젝트에서는 리덕스를 사용할 때 이 함수를 직접 사용하지 않는다!
→ react-redux라는 라이브러리가 이 작업을 대신해주기 때문!

</aside>

```jsx
(...)

//구독하기
store.subscribe(render);
```

## 10) 액션 발생시키기

액션 발생 시키는 것 → 디스패치

- 스토어의 내장 함수 dispatch를 사용

```jsx
//액션 발생시키기
divToggle.onclick = () => {
  store.dispatch(toggleSwitch());
};
btnIncrease.onclick = () => {
  store.dispatch(increase(1));
};
btnDecrease.onclick = () => {
  store.dispatch(decrease());
};
```

**결과)**

<img src="https://user-images.githubusercontent.com/49816869/150383562-69822044-1ded-4ab1-bc71-8024f21ab0ff.png" />

# 3. 리덕스의 세 가지 규칙

## 1) 단일 스토어

- 하나의 애플리케이션 안에는 하나의 스토어가 들어 있다.

## 2) 읽기 전용 상태

- 리덕스 상태는 읽기 전용이다.
- 상태를 업데이트할 때 기존의 객체는 건드리지 않고 새로운 객체를 생성해 주어야 한다.

## 3) 리듀서는 순수한 함수

**순수한 함수란?**

- 리듀서 함수는 이전 상태와 액션 객체를 파라미터로 받는다.
- 파라미터 외의 값에는 의존하면 안된다.
- 이전 상태는 절대로 건드리지 않고, 변화를 준 새로운 상태 객체를 만들어서 반환한다.
- 똑같은 파라미터로 호출된 리듀서 함수는 언제나 똑같은 결과 값을 반환해야 한다.

<결론>

어렵당
