# 1. 작업 환경 준비

**프로젝트 생성)**

`$ yarn create react-app learn-redux-middleware`

**라이브러리 설치)**

`$ yarn add redux react-redux redux-actions`

**counter 리덕스 모듈 작성)**

>✅ **복습!** <br>
모듈이란 Ducks 패턴을 사용해 액션 타입, 액션 생성 함수, 리듀서를 작성한 코드를 말한다!

```jsx
import { createAction, handleActions } from "redux-actions";

//액션타입 정의
const INCREASE = "counter/INCREASE";
const DECREASE = "counter/DECREASE";

//액션 생성 함수
export const increase = createAction(INCREASE);
export const decrease = createAction(DECREASE);

//초기화
const initialState = 0; //상태는 꼭 객체일 필요가 없다. 숫자도 작동한다.

//리듀서 생성
//리듀서는 변화를 일으키는 함수
const counter = handleActions(
  {
    [INCREASE]: (state) => state + 1,
    [DECREASE]: (state) => state - 1,
  },
  initialState
);

export default counter;
```

**루트 리듀서 생성)**

> ✅ **복습!** <br>
루트 리듀서는 여러 개의 리듀서를 하나로 합친 것

```jsx
import { combineReducers } from "redux";
import counter from "./counter";

const rootReducer = combineReducers({
  counter,
});

export default rootReducer;
```

**Provider 컴포넌트를 사용해 프로젝트에 리덕스 적용하기)**

> ✅ 복습!<br>
Provider는 리액트 컴포넌트에서 **스토어를 사용할 수 있도록 해주는 컴포넌트**이다.<br>
App 컴포넌트를 Provider 컴포넌트로 감싸면 된다.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { createStore } from "redux";
import { Provider } from "react-redux";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import rootReducer from "./modules";

//스토어 생성
const store = createStore(rootReducer);

ReactDOM.render(
  //리덕스 적용
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

reportWebVitals();
```

**카운터 컴포넌트 생성→프레젠테이셔널 컴포넌트)**

```jsx
import React from "react";

const Counter = ({ onIncrease, onDecrease, number }) => {
  return (
    <div>
      <h1>{number}</h1>
      <button onClick={onIncrease}>+1</button>
      <button onClick={onDecrease}>-1</button>
    </div>
  );
};

export default Counter;
```

**카운터 컨테이너 컴포넌트 생성→컨테이너 컴포넌트)**

> ✅ **복습!** <br>
connect 함수는 container 컴포넌트를 리덕스와 연동시키기 위해 사용하는 함수이다. <br>
`const makeContainer = connect(mapStateToProps, mapDispatchToProps)
makeContainer(타깃 컴포넌트)`

```jsx
import React from "react";
import { connect } from "react-redux";
import { increase, decrease } from "../modules/counter";
import Counter from "../components/Counter";

const CounterContainer = ({ number, increase, decrease }) => {
  return (
    <Counter number={number} onIncrease={increase} onDecrease={decrease} />
  );
};

//컨테이너 컴포넌트 리덕스와 연동시키기!
export default connect(
  (state) => ({
    number: state.counter,
  }),
  {
    increase,
    decrease,
  }
)(CounterContainer);
```

**App에 적용)**

```jsx
import React from "react";
import CounterContainer from "./containers/CounterContainer";

const App = () => {
  return (
    <div>
      <CounterContainer />
    </div>
  );
};

export default App;
```

# 2. 미들웨어란?

- 액션과 리듀서 사이의 중간자
- 액션을 디스패치(액션 발생)했을 때 리듀서에서 이를  처리하기에 앞서 지정된 작업들을 실행해 주는 것

ex) 전달받은 액션 콘솔에 기록, 전달받은 액션 정보를 기반으로 액션 취소, 다른 종류의 액션을 추가로 디스패치

> ✅ 실제 프로젝트 작업시 미들웨어는 직접 만들어 사용하기보단, 다른 개발자가 만들어 놓은 미들웨어를 사용하는 경우가 많다.

## 1) 미들웨어 만들기

액션이 디스패치 될 때마다 액션의 정보와 액션이 디스패치되기 전후의 상태를 콘솔에 보여 주는 로깅 미들웨어 만들기

```jsx
const loggerMiddleware = (store) => (next) => (action) => {
  //미들웨어 기본 구조
};

export default loggerMiddleware;
```

- store : 리덕스 스토어 인스턴스
- action : 디스패치된 액션
- next
    - 함수 형태의 파라미터 값
    - **store.dispatch**와 비슷한 역할
    - next(action)을 호출하면 그 다음 처리해야 할 미들웨어에게 액션을 넘겨주고, 다음 미들웨어가 없을 때 리듀서에게 액션을 넘겨 줌.
    - 미들웨어 내부에서 store.dispatch를 사용하면 첫 번째 미들웨어 부터 다시 처리한다.
    만약 미들웨어에서 next를 사용하지 않으면 액션이 리듀서에 전달되지 않는다.
        
        <img src="https://user-images.githubusercontent.com/49816869/150680364-47b6451f-3075-4c31-8947-5adf8b7a57bd.png" width="500px" />
        

**1 이전 상태, 2 액션정보, 3 새로워진 상태 를 순차적으로 콘솔에 보여주는 미들웨어)**

```jsx
const loggerMiddleware = (store) => (next) => (action) => {
  console.group(action && action.type); //액션 타입으로 log를 그룹화함.
  console.log("이전 상태", store.getState());
  console.log("액션", action);
  next(action); //다음 미들웨어 혹은 리듀서에게 전달
  console.log("다음 상태", store.getState());
  console.groupEnd(); //그룹 끝
};

export default loggerMiddleware;
```

**제작한 리덕스 미들웨어를 스토어에 적용하기)**

미들웨어는 스토어를 생성하는 과정에서 적용한다.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import rootReducer from "./modules";
import loggerMiddleware from "./lib/loggerMiddleware";

//스토어 생성
const store = createStore(rootReducer, applyMiddleware(loggerMiddleware));

ReactDOM.render(
  //리덕스 적용
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

<img src="https://user-images.githubusercontent.com/49816869/150680699-c57e1b7c-c22e-430f-8268-317e6bc3ea91.png" width="500px" />

## 2) redux-logger 사용하기

이미 오픈 소스 커뮤니티에 올라와 있는 redux-logger 미들웨어를 설치하고 사용해보자.

**redux-logger 설치)**

`$ yarn add redux-logger`

**index.js 수정)**

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import rootReducer from "./modules";
// import loggerMiddleware from "./lib/loggerMiddleware";
import { createLogger } from "redux-logger";

//스토어 생성
const logger = createLogger();
const store = createStore(rootReducer, applyMiddleware(logger));

ReactDOM.render(
  //리덕스 적용
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

**결과)**

<img src="https://user-images.githubusercontent.com/49816869/150680737-ebfd9148-4c91-440c-b6cf-c9e96b2b24cb.png" width="500" />

# 3. 비동기 작업을 처리하는 미들웨어 사용

오픈 소스 커뮤니티에 공개된 미들웨어를 사용해 리덕스를 사용하고 있는 프로젝트에서 비동기 작업을 더욱 효율적으로 관리해보자.

- **redux-thunk** : 비동기 작업을 처리할 때 가장 많이 사용하는 미들웨어. 함수 형태의 액션을 디스패치할 수 있게 해 준다.
- **redux-saga** : redux-thunk 다음으로 많이 사용되는 비동기 작업 관련 미들웨어 라이브러리. 특정 액션이 디스패치 되었을 때 정해진 로직에 따라 다른 액션을 디스패치 시키는 규칙을 작성하여 비동기 작업을 처리할 수 있게 해준다.

## 1) redux-thunk

### (1) Thunk란?

- Thunk 뜻
    
    썽크(**Thunk**)는 "고려하다"라는 영어 단어인 "Think"의 은어 격 과거분사인 "**Thunk**"에서 파생된 단어인데, 연산이 철저하게 "고려된 후", 즉 실행이 된 후에야 썽크의 값이 가용해지는 데서 유래된 것이라고 볼 수 있다.
    

특정 작업을 나중에 할 수 있도록 미루기 위해 함수 형태로 감싼 것을 의미

> ✅ redux-thunk 라이브러리를 사용하면 thunk 함수를 만들어 디스패치 할 수 있다. 그러면 리덕스 미들웨어가 그 함수를 전달받아 store의 dispatch와 getState를 파라미터로 넣어서 호출해준다.

```jsx
const sampleThunk = () => (dispatch, getState) => {
	//현재 상태를 참조할 수 있고,
  //새 액션을 디스패치할 수도 있다.
}
```

### (2) 미들웨어 적용하기

**라이브러리 설치)**

`$ yarn add redux-thunk`

**스토어를 만들 때 redux-thunk 적용)**

```jsx
(...)
import ReduxThunk from "redux-thunk";

//스토어 생성
const logger = createLogger();
const store = createStore(rootReducer, applyMiddleware(logger, ReduxThunk));

(...)
```

### (3) Thunk 생성 함수 만들기

- redux-thunk는 액션 생성 함수에서 일반 액션 객체를 반환하는 대신 함수를 반환한다.

**increaseAsync와 decreaseAsync 함수를 만들어 카운터 값을 비동기적으로 변경시키기)**

```jsx
//1초 뒤에 increase 혹은 decrease 함수를 디스패치함
export const increaseAsync = () => (dispatch) => {
  setTimeout(() => {
    dispatch(increase());
  }, 1000);
};

export const decreaseAsync = () => (dispatch) => {
  setTimeout(() => {
    dispatch(decrease());
  }, 1000);
};
```

**CounterContainer 에서 호출하던 액션 생성 함수도 변경해주기)**

```jsx
import React from "react";
import { connect } from "react-redux";
import { increaseAsync, decreaseAsync } from "../modules/counter";
import Counter from "../components/Counter";

const CounterContainer = ({ number, increaseAsync, decreaseAsync }) => {
  return (
    <Counter
      number={number}
      onIncrease={increaseAsync}
      onDecrease={decreaseAsync}
    />
  );
};

//컨테이너 컴포넌트 리덕스와 연동시키기!
export default connect(
  (state) => ({
    number: state.counter,
  }),
  {
    increaseAsync,
    decreaseAsync,
  }
)(CounterContainer);
```

**숫자가 1초 뒤에 변경되는지 확인하기)**

<img src="https://user-images.githubusercontent.com/49816869/150682273-207ddf95-46c8-4883-bcdc-456a6215ab54.png" width="500" />


처음 디스패치되는 액션은 함수 형태, 두번 째는 객체 형태

### (4) 웹 요청 비동기 작업 처리하기

**사용할 API 함수화하기)**

```jsx
import axios from "axios";

//포스트 읽기
export const getPost = (id) =>
  axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`);

//모든 사용자 불러오기
export const getUsers = (id) =>
  axios.get(`https://jsonplaceholder.typicode.com/users`);
```

**리듀서 작성하기)**

```jsx
import { handleActions } from "redux-actions";
import * as api from "../lib/api";

// 액션 타입을 선언합니다.
// 한 요청당 세 개를 만들어야 합니다.

const GET_POST = "sample/GET_POST";
const GET_POST_SUCCESS = "sample/GET_POST_SUCCESS";
const GET_POST_FAILURE = "sample/GET_POST_FAILURE";

const GET_USERS = "sample/GET_USERS";
const GET_USERS_SUCCESS = "sample/GET_USERS_SUCCESS";
const GET_USERS_FAILURE = "sample/GET_USERS_FAILURE";

// thunk 함수를 생성합니다.
// thunk 함수 내부에서는 시작할 때, 성공했을 때, 실패했을 때 다른 액션을 디스패치합니다.

export const getPost = (id) => async (dispatch) => {
  dispatch({ type: GET_POST }); // 요청을 시작한 것을 알림
  try {
    const response = await api.getPost(id);
    dispatch({
      type: GET_POST_SUCCESS,
      payload: response.data,
    }); // 요청 성공
  } catch (e) {
    dispatch({
      type: GET_POST_FAILURE,
      payload: e,
      error: true,
    }); // 에러 발생
    throw e; // 나중에 컴포넌트단에서 에러를 조회할 수 있게 해 줌
  }
};

export const getUsers = () => async (dispatch) => {
  dispatch({ type: GET_USERS }); // 요청을 시작한 것을 알림
  try {
    const response = await api.getUsers();
    dispatch({
      type: GET_USERS_SUCCESS,
      payload: response.data,
    }); // 요청 성공
  } catch (e) {
    dispatch({
      type: GET_USERS_FAILURE,
      payload: e,
      error: true,
    }); // 에러 발생
    throw e; // 나중에 컴포넌트단에서 에러를 조회할 수 있게 해 줌
  }
};

// 초기 상태를 선언합니다.
// 요청의 로딩 중 상태는 loading이라는 객체에서 관리합니다.

const initialState = {
  loading: {
    GET_POST: false,
    GET_USERS: false,
  },
  post: null,
  users: null,
};

const sample = handleActions(
  {
    [GET_POST]: (state) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_POST: true, // 요청 시작
      },
    }),
    [GET_POST_SUCCESS]: (state, action) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_POST: false, // 요청 완료
      },
      post: action.payload,
    }),
    [GET_POST_FAILURE]: (state, action) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_POST: false, // 요청 완료
      },
    }),
    [GET_USERS]: (state) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_USERS: true, // 요청 시작
      },
    }),
    [GET_USERS_SUCCESS]: (state, action) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_USERS: false, // 요청 완료
      },
      users: action.payload,
    }),
    [GET_USERS_FAILURE]: (state, action) => ({
      ...state,
      loading: {
        ...state.loading,
        GET_USERS: false, // 요청 완료
      },
    }),
  },
  initialState
);

export default sample;
```

**루트 리듀서 작성하기)**

```jsx
import { combineReducers } from "redux";
import counter from "./counter";
import sample from "./sample";

const rootReducer = combineReducers({
  counter,
  sample,
});

export default rootReducer;
```

**데이터를 렌더링할 Sample 컴포넌트 작성→프레젠테이셔널 컴포넌트)**

```jsx
import React from "react";

const Sample = ({ loadingPost, loadingUsers, post, users }) => {
  return (
    <div>
      <section>
        <h1>포스트</h1>
        {loadingPost && "로딩 중..."}
        {!loadingPost && post && (//이렇게 해주는 이유 (유효성 검사) - post 데이터가 없을 때 조회하면 에러 뜨기 때문!
          <div>
            <h3>{post.title}</h3>
            <h3>{post.body}</h3>
          </div>
        )}
      </section>
      <hr />
      <section>
        <h1>사용자 목록</h1>
        {loadingUsers && "로딩 중..."}
        {!loadingUsers && users && (
          <ul>
            {users.map((user) => (
              <li key={user.id}>
                {user.username}({user.email})
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
};

export default Sample;
```

**컨테이너 컴포넌트 작성)**

```jsx
import React from "react";
import { connect } from "react-redux";
import Sample from "../components/Sample";
import { getPost, getUsers } from "../modules/sample";

const { useEffect } = React;
const SampleContainer = ({
  getPost,
  getUsers,
  post,
  users,
  loadingPost,
  loadingUsers,
}) => {
  //클래스 형태 컴포넌트였다면 componentDidMount
  useEffect(() => {
    getPost(1);
    getUsers(1);
  }, [getPost, getUsers]);
  return (
    <Sample
      post={post}
      users={users}
      loadingPost={loadingPost}
      loadingUsers={loadingUsers}
    />
  );
};

export default connect(
  ({ sample }) => ({
    post: sample.post,
    users: sample.users,
    loadingPost: sample.loading.GET_POST,
    loadingUsers: sample.loading.GET_USERS,
  }),
  {
    getPost,
    getUsers,
  }
)(SampleContainer);
```

App 컴포넌트에 적용)

```jsx
import React from "react";
import CounterContainer from "./containers/CounterContainer";
import SampleContainer from "./containers/SampleContainer";

const App = () => {
  return (
    <div>
      <SampleContainer />
    </div>
  );
};

export default App;
```

<img src="https://user-images.githubusercontent.com/49816869/150682323-a0ea68f4-0cc6-4ee7-b2a8-112271a6d968.png" width="500" />


### (5) 리팩토링

```jsx
export default function createRequestThunk(type, request) {
  // 성공 및 실패 액션 타입을 정의합니다.
  const SUCCESS = `${type}_SUCCESS`;
  const FAILURE = `${type}_FAILURE`;
  return (params) => async (dispatch) => {
    dispatch({ type }); // 시작됨
    try {
      const response = await request(params);
      dispatch({
        type: SUCCESS,
        payload: response.data,
      }); // 성공
    } catch (e) {
      dispatch({
        type: FAILURE,
        payload: e,
        error: true,
      }); // 에러 발생
      throw e;
    }
  };
}

// 사용법: createRequestThunk('GET_USERS', api.getUSERS);
```

**위에서 만든 유틸 함수로 API 요청을 해주는 thunk 함수 한 줄로 생성하기**

```jsx
import createRequestThunk from "../lib/createRequestThunk";

(...)

// export const getPost = (id) => async (dispatch) => {
//   dispatch({ type: GET_POST }); // 요청을 시작한 것을 알림
//   try {
//     const response = await api.getPost(id);
//     dispatch({
//       type: GET_POST_SUCCESS,
//       payload: response.data,
//     }); // 요청 성공
//   } catch (e) {
//     dispatch({
//       type: GET_POST_FAILURE,
//       payload: e,
//       error: true,
//     }); // 에러 발생
//     throw e; // 나중에 컴포넌트단에서 에러를 조회할 수 있게 해 줌
//   }
// };

// export const getUsers = () => async (dispatch) => {
//   dispatch({ type: GET_USERS }); // 요청을 시작한 것을 알림
//   try {
//     const response = await api.getUsers();
//     dispatch({
//       type: GET_USERS_SUCCESS,
//       payload: response.data,
//     }); // 요청 성공
//   } catch (e) {
//     dispatch({
//       type: GET_USERS_FAILURE,
//       payload: e,
//       error: true,
//     }); // 에러 발생
//     throw e; // 나중에 컴포넌트단에서 에러를 조회할 수 있게 해 줌
//   }
// };

export const getPost = createRequestThunk(GET_POST, api.getPost);
export const getUsers = createRequestThunk(GET_USERS, api.getUsers);

(...)
```

**로딩 상태만 관리하는 리덕스 모듈을 생성하여 처리하기)**

```jsx
import { createAction, handleActions } from "redux-actions";

const START_LOADING = "loading/START_LOADING";
const FINISH_LOADING = "loading/FINISH_LOADING";

// 요청을 위한 액션 타입을 payload로 설정합니다(예: "sample/GET_POST").

export const startLoading = createAction(
  START_LOADING,
  (requestType) => requestType
);

export const finishLoading = createAction(
  FINISH_LOADING,
  (requestType) => requestType
);

const initialState = {};

const loading = handleActions(
  {
    [START_LOADING]: (state, action) => ({
      ...state,
      [action.payload]: true,
    }),
    [FINISH_LOADING]: (state, action) => ({
      ...state,
      [action.payload]: false,
    }),
  },
  initialState
);

export default loading;
```

**요청이 시작될 때 디스패치할 액션)**

```jsx
{
	type: 'loading/START_LOADING',
	payload: 'sample/GET_POST'
}
```

→ sample/GET_POST의 loading 리듀서 값을 true로 변경

요청이 끝났을 때 디스패치할 액션)

```jsx
{
	type: 'loading/FINISH_LOADING',
	payload: 'sample/GET_POST'
}
```

→ sample/GET_POST의 loading 리듀서 값을 false로 변경

**생성한 리듀서 루트 리듀서에 포함)**

```jsx
import { combineReducers } from "redux";
import counter from "./counter";
import sample from "./sample";
import loading from "./loading";

const rootReducer = combineReducers({
  counter,
  sample,
  loading,
});

export default rootReducer;
```

**loading 리덕스 모듈 사용하기)**

```jsx
import { startLoading, finishLoading } from "../modules/loading";

export default function createRequestThunk(type, request) {
  // 성공 및 실패 액션 타입을 정의합니다.
  const SUCCESS = `${type}_SUCCESS`;
  const FAILURE = `${type}_FAILURE`;
  return (params) => async (dispatch) => {
    dispatch({ type }); // 시작됨
    dispatch(startLoading(type));
    try {
      const response = await request(params);
      dispatch({
        type: SUCCESS,
        payload: response.data,
      }); // 성공
      dispatch(finishLoading(type));
    } catch (e) {
      dispatch({
        type: FAILURE,
        payload: e,
        error: true,
      }); // 에러 발생
      dispatch(startLoading(type));
      throw e;
    }
  };
}

// 사용법: createRequestThunk('GET_USERS', api.getUSERS);
```

**로딩 상태 조회)**

```jsx
export default connect(
  ({ sample, loading }) => ({
    post: sample.post,
    users: sample.users,
    // loadingPost: sample.loading.GET_POST,
    // loadingUsers: sample.loading.GET_USERS,
    loadingPost: loading["sample/GET_POST"],
    loadingUsers: loading["sample/GET_USERS"],
  }),
  {
    getPost,
    getUsers,
  }
)(SampleContainer);
```

<img src="https://user-images.githubusercontent.com/49816869/150682350-6f6cf26c-6d52-48dc-b66a-0ec77ab0cc34.png" width="500" />


**sample 리듀서에서 불필요한 코드 지우기)**

```jsx
// const initialState = {
//   loading: {
//     GET_POST: false,
//     GET_USERS: false,
//   },
//   post: null,
//   users: null,
// };

const initialState = {
  post: null,
  users: null,
};

// const sample = handleActions(
//   {
//     [GET_POST]: (state) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_POST: true, // 요청 시작
//       },
//     }),
//     [GET_POST_SUCCESS]: (state, action) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_POST: false, // 요청 완료
//       },
//       post: action.payload,
//     }),
//     [GET_POST_FAILURE]: (state, action) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_POST: false, // 요청 완료
//       },
//     }),
//     [GET_USERS]: (state) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_USERS: true, // 요청 시작
//       },
//     }),
//     [GET_USERS_SUCCESS]: (state, action) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_USERS: false, // 요청 완료
//       },
//       users: action.payload,
//     }),
//     [GET_USERS_FAILURE]: (state, action) => ({
//       ...state,
//       loading: {
//         ...state.loading,
//         GET_USERS: false, // 요청 완료
//       },
//     }),
//   },
//   initialState
// );

const sample = handleActions(
  {
    [GET_POST_SUCCESS]: (state, action) => ({
      ...state,
      post: action.payload,
    }),
    [GET_USERS_SUCCESS]: (state, action) => ({
      ...state,
      users: action.payload,
    }),
  },
  initialState
);
```

- sample 리듀서에서 로딩 중에 대한 상태를 관리할 필요가 없다.
- 실패했을 때의 케이스를 관리하고 싶다면, _FAILURE가 붙은 액션을 리듀서에서 처리하거나, 컨테이너 컴포넌트에서 try/catch문을 사용해 에러 값을 조회할 수 있다.
    
    ```jsx
    useEffect(() => {
        // useEffect에 파라미터로 넣는 함수는 async로 할 수 없기 때문에
        // 그 내부에서 async 함수를 선언하고 호출해 줍니다.
        const fn = async () => {
          try {
            await getPost(1);
            await getUsers(1);
          } catch (e) {
            console.log(e); // 에러 조회
          }
        };
        fn();
      }, [getPost, getUsers]);
    ```
    

## 2) redux-saga

**redux-saga를 사용하는 것이 유리한 경우)**

- 기존 요청을 취소 처리해야 할 때(불필요한 중복 요청 방지)
- 특정 액션이 발생했을 때 다른 액션을 발생시키거나, API 요청 등 리덕스와 관계없는 코드를 실행할 때
- 웹소켓을 사용할 때
- API 요청 실패 시 재요청해야 할 때,

### (1) 재너레이터 함수 이해하기

- 하나의 함수에서 값을 여러 개 반환하는 것은 불가능하다.
- 하지만 제너레이터 함수를 사용하면 값을 순차적으로 여러 개 반환할 수 있다.
- 재너레이터 함수는 **function*** 키워드를 사용한다.

```jsx
function* generatorFunction(){
	console.log('안녕하세요');
	yield 1;
	console.log('재너레이터 함수');
	yield 2;
	console.log('function*');
	yield 3;
	return 4;
}

//재너레이터 생성
const generator = generatorFunction();
```

<img alt="결과" src="https://user-images.githubusercontent.com/49816869/150680089-c189a78a-3d02-4d41-8e4a-1bfc3a431fbc.png" width="500px" />

<결과>

- next() 호출 시 다음 yield가 있는 곳까지 호출 후 함수가 멈춘다.
- 추가적으로 next 함수에 파라미터를 넣으면 재너레이터 함수에서 yield를 사용해 해당 값을 조회할 수 있다.

>✅ redux-saga는 재너레이터 함수 문법을 기반으로 비동기 작업을 관리해 준다.

ex)

```jsx
function* watchGenerator() {
console.log('모니터링 중...');
let prevAction = null;
while(true) {
    const action = yield;
    console.log('이전 액션: ', prevAction);
    prevAction = action;
    if (action.type === 'HELLO') {
        console.log('안녕하세요!');
    }
}
}

const watch = watchGenerator();
```

<img src="https://user-images.githubusercontent.com/49816869/150682730-1ea58bfc-d834-4485-b9d5-a3ba39643b2f.png" width="500" />


- 위와 같이 redux-saga는 우리가 디스패치하는 액션을 모니터링하여 그에 따라 필요한 작업을 따로 수행할 수 있는 미들웨어이다.

### (2) 비동기 카운터 만들기

**라이브러리 설치)**

`$ yarn add redux-saga`

**counter 리덕스 모듈 수정)**

재너레이터 함수를 **사가(saga)**라 부른다.

```jsx
import { createAction, handleActions } from "redux-actions";
import { delay, put, takeEvery, takeLatest } from "redux-saga/effects";

//액션타입 정의
const INCREASE = "counter/INCREASE";
const DECREASE = "counter/DECREASE";

const INCREASE_ASYNC = "counter/INCREASE_ASYNC";
const DECREASE_ASYNC = "counter/DECREASE_ASYNC";

//액션 생성 함수
export const increase = createAction(INCREASE);
export const decrease = createAction(DECREASE);

// 마우스 클릭 이벤트가 payload 안에 들어가지 않도록
// () => undefined를 두 번째 파라미터로 넣어 줍니다.
export const increaseAsync = createAction(INCREASE_ASYNC, () => undefined);
export const decreaseAsync = createAction(DECREASE_ASYNC, () => undefined);

function* increaseSaga() {
  yield delay(1000); // 1초를 기다립니다.
  yield put(increase()); // 특정 액션을 디스패치합니다.
}

function* decreaseSaga() {
  yield delay(1000); // 1초를 기다립니다.
  yield put(decrease()); // 특정 액션을 디스패치합니다.
}

export function* counterSaga() {
  // takeEvery는 들어오는 모든 액션에 대해 특정 작업을 처리해 줍니다.
  yield takeEvery(INCREASE_ASYNC, increaseSaga);
  // takeLatest는 기존에 진행 중이던 작업이 있다면 취소 처리하고
  // 가장 마지막으로 실행된 작업만 수행합니다.
  yield takeLatest(DECREASE_ASYNC, decreaseSaga);
}

(...)
```

**루트 사가 추가)**

```jsx
import { combineReducers } from "redux";
import counter from "./counter";
import counter, { counterSaga } from "./counter";
import sample from "./sample";
import loading from "./loading";

const rootReducer = combineReducers({
  counter,
  sample,
  loading,
});

export function* rootSaga() {
  // all 함수는 여러 사가를 합쳐 주는 역할을 합니다.
  yield all([counterSaga()]);
}

export default rootReducer;
```

**스토어에 redux-saga 미들웨어 적용하기)**

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import rootReducer, { rootSaga } from "./modules";
// import loggerMiddleware from "./lib/loggerMiddleware";
import { createLogger } from "redux-logger";
import ReduxThunk from "redux-thunk";
import createSagaMiddleware from "redux-saga";

//스토어 생성
const logger = createLogger();
const sagaMiddleware = createSagaMiddleware();
const store = createStore(
  rootReducer,
  applyMiddleware(logger, ReduxThunk, sagaMiddleware)
);

sagaMiddleware.run(rootSaga);

ReactDOM.render(
  //리덕스 적용
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

결과 → 정상 작동!

<img src="https://user-images.githubusercontent.com/49816869/150682755-1bdbb635-336b-4035-bb55-373c964192c8.png" width="500" />

> ✅ **리덕스 개발자 도구를 적용해 어떤 액션이 디스패치되고 있는지 확인해보기**

**리덕스 개발자 도구 라이브러리 설치)**

`$ yarn add redux-devtools-extension`

**App.js 변경)**

```jsx
import React from "react";
import CounterContainer from "./containers/CounterContainer";
import SampleContainer from "./containers/SampleContainer";

const App = () => {
  return (
    <div>
      <CounterContainer />
    </div>
  );
};

export default App;
```

**index.js에 개발자 도구 적용)**

applyMiddleWare 부분을 composeWithDevTools로 감싸주면 된다.

```jsx
(...)
import { composeWithDevTools } from "redux-devtools-extension";

//스토어 생성
const logger = createLogger();
const sagaMiddleware = createSagaMiddleware();
const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(logger, ReduxThunk, sagaMiddleware))
);
(...)
```

**결과)**

<img src="https://user-images.githubusercontent.com/49816869/150682780-68809af6-6b2a-4ab4-8aa2-baca6fcf7f13.png" width="500" />

- +1 버튼을 누르면 INCREASE_ASYNC와 INCREASE 액션이 두 번 디스패치 된다.
    - takeEvery를 사용하여 increaseSaga를 등록했기 때문

<img src="https://user-images.githubusercontent.com/49816869/150682800-8e820307-8349-411d-9b83-3f51948b2fe0.png" width="500" />

- -1 버튼을 누르면 DECREASE_ASYNC가 두 번 디스패치 되지만 DECREASE는 한 번 디스패치 된다.
    - takeLatest를 사용하여 decreaseSaga를 등록했기 때문(여러 액션이 중첩되어 디스패치 되었을 때 마지막 액션만 제대로 처리)

### (3) API 요청 상태 관리하기

**sample 리덕스 모듈 수정)**

```jsx
import { createAction, handleActions } from "redux-actions";
import { call, put, takeLatest } from "redux-saga/effects";
import * as api from "../lib/api";
import createRequestThunk from "../lib/createRequestThunk";
import { startLoading, finishLoading } from "./loading";

// 액션 타입을 선언합니다.
// 한 요청당 세 개를 만들어야 합니다.

const GET_POST = "sample/GET_POST";
const GET_POST_SUCCESS = "sample/GET_POST_SUCCESS";
// const GET_POST_FAILURE = "sample/GET_POST_FAILURE";
const GET_POST_FAILURE = "sample/GET_POST_FAILURE";

const GET_USERS = "sample/GET_USERS";
const GET_USERS_SUCCESS = "sample/GET_USERS_SUCCESS";
// const GET_USERS_FAILURE = "sample/GET_USERS_FAILURE";
const GET_USERS_FAILURE = "sample/GET_USERS_FAILURE";

export const getPost = createAction(GET_POST, (id) => id);
export const getUsers = createAction(GET_USERS);

function* getPostSaga(action) {
  yield put(startLoading(GET_POST)); // 로딩 시작
  // 파라미터로 action을 받아 오면 액션의 정보를 조회할 수 있습니다.
  try {
    // call을 사용하면 Promise를 반환하는 함수를 호출하고, 기다릴 수 있습니다.
    // 첫 번째 파라미터는 함수, 나머지 파라미터는 해당 함수에 넣을 인수입니다.
    const post = yield call(api.getPost, action.payload); // api.getPost(action.payload)를 의미
    yield put({
      type: GET_POST_SUCCESS,
      payload: post.data,
    });
  } catch (e) {
    // try/catch 문을 사용하여 에러도 잡을 수 있습니다.
    yield put({
      type: GET_POST_FAILURE,
      payload: e,
      error: true,
    });
  }
  yield put(finishLoading(GET_POST)); // 로딩 완료
}

function* getUsersSaga() {
  yield put(startLoading(GET_USERS));
  try {
    const users = yield call(api.getUsers);
    yield put({
      type: GET_USERS_SUCCESS,
      payload: users.data,
    });
  } catch (e) {
    yield put({
      type: GET_USERS_FAILURE,
      payload: e,
      error: true,
    });
  }
  yield put(finishLoading(GET_USERS));
}

export function* sampleSaga() {
  yield takeLatest(GET_POST, getPostSaga);
  yield takeLatest(GET_USERS, getUsersSaga);
}
```

- API를 호출해야 하는 상황에는 사가 내부에서 직접 호출하지 않고, call 함수를 사용한다.
    - call 함수의 첫 번째 인수로 호출하고 싶은 함수를, 뒤에 오는 인수들은 해당 함수에 넣어 주고 싶은 인수를 적어준다.

**루트 사가에 등록)**

```jsx
import { combineReducers } from "redux";
import { all } from "redux-saga/effects";
import counter, { counterSaga } from "./counter";
import sample, { sampleSaga } from "./sample";
import loading from "./loading";

const rootReducer = combineReducers({
  counter,
  sample,
  loading,
});

export function* rootSaga() {
  // all 함수는 여러 사가를 합쳐 주는 역할을 합니다.
  yield all([counterSaga(), sampleSaga()]);
}

export default rootReducer;
```

**App.js 렌더링)**

```jsx
import React from "react";
import CounterContainer from "./containers/CounterContainer";
import SampleContainer from "./containers/SampleContainer";

const App = () => {
  return (
    <div>
      <SampleContainer />
    </div>
  );
};

export default App;
```

<img src="https://user-images.githubusercontent.com/49816869/150682846-96b0a0be-11a3-41d6-b351-c297c5060a67.png" width="500" />


### (4) 리팩토링

```jsx
import { call, put } from "redux-saga/effects";
import { startLoading, finishLoading } from "../modules/loading";

export default function createRequestSaga(type, request) {
  const SUCCESS = `${type}_SUCCESS`;
  const FAILURE = `${type}_FAILURE`;

  return function* (action) {
    yield put(startLoading(type)); // 로딩 시작
    try {
      const response = yield call(request, action.payload);
      yield put({
        type: SUCCESS,
        payload: response.data,
      });
    } catch (e) {
      yield put({
        type: FAILURE,
        payload: e,
        error: true,
      });
    }
    yield put(finishLoading(type)); // 로딩 끝
  };
}
```

**리팩토링 적용하기)**

```jsx
(...)
import createRequestSaga from "../lib/createRequestSaga";
(...)

const getPostSaga = createRequestSaga(GET_POST, api.getPost);
const getUsersSaga = createRequestSaga(GET_USERS, api.getUsers);

(...)
```

### (5) 알아두면 유용한 기능들

**사가 내부에서 현재 상태 조회하는 방법)**

```jsx
import { delay, put, takeEvery, takeLatest, select } from "redux-saga/effects";
(...)

function* increaseSaga() {
  yield delay(1000); // 1초를 기다립니다.
  yield put(increase()); // 특정 액션을 디스패치합니다.
  const number = yield select((state) => state.counter); // state는 스토어 상태를 의미함
  console.log(`현재 값은 ${number}입니다.`);
}

```

<img src="https://user-images.githubusercontent.com/49816869/150682872-ef9f3e73-caaa-4010-be05-341e3860c229.png" width="500" />


**사가가 실행되는 주기 제한하는 방법)**

takeEvery 대신 throttle 함수 사용하기

→ n초에 단 한번만 호출 될 수 있도록 설정할 수 있다.

ex) `yeid throttle(3000, INCREASE_ASYNC, increaseSaga);`

redux-saga 메뉴얼)

[Redux-Saga - An intuitive Redux side effect manager. | Redux-Saga](https://redux-saga.js.org/)

# 퀴즈

Q1) 액션을 디스패치했을 때 리듀서에서 이를 처리하기에 앞서 사전에 지정된 작업들을 실행할 수 있겠끔 하는 기능은?

- 정답
    
    미들웨어
    

Q2) next(action)을 호출하면 그다음 처리해야 할 미들웨어에게 액션을 넘겨주고, 다음 미들웨어가 없다면 첫 번째 미들웨어부터 다시 처리한다.

- 정답
    
    (O, **X**)
    

Q3) 재너레이터 함수를 기반으로 비동기 작업을 관리해 주는 미들웨어는?

- 정답
    
    redux-saga
