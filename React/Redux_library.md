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

```
