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

## 1) 새 Context 만들기

1. Contexts 폴더 만들기 (꼭 contexts 디렉터리에 만들 필요는 없지만 구분을 위해!)
2. createContext 함수를 사용해 새 Context 만들기

**contexts/color.js)**

```jsx
import { createContext } from "react";

const ColorContext = createContext({ color: "black" });

export default ColorContext;
```

## 2) Consumer 사용하기

**Consumer란?**

Context 변화를 구독하는 React 컴포넌트

Consumer를 사용해 함수 컴포넌트안에서 context를 구독할 수 있다.

**components/ColorBox.js**

```jsx
import React from "react";
import ColorContext from "../contexts/color";

const ColorBox = () => {
  return (
    <ColorContext.Consumer>
      {(value) => (
        <div
          style={{ width: "64px", height: "64px", background: value.color }}
        />
      )}
    </ColorContext.Consumer>
  );
};

export default ColorBox;
```

- Consumer 사이에 중괄호를 열어 그 안에 함수를 넣어 주었는데 이런 패턴을 Function as a child, 혹은 **Render Props**라고 한다.

**Render Props?**

컴포넌트의 children이 있어야 할 자리에 일반 JSX 혹은 문자열이 아닌 함수를 전달하는 것

- App.js
    
    ```jsx
    import React from "react";
    import ColorBox from "./components/ColorBox";
    
    const App = () => {
      return (
        <div>
          <ColorBox />
        </div>
      );
    };
    
    export default App;
    ```
    

## 3) Provider

Provider를 사용해 Context의 value를 변경할 수 있다.

**App.js 수정)**

```jsx
import React from "react";
import ColorBox from "./components/ColorBox";
import ColorContext from "./contexts/color";

const App = () => {
  return (
    <ColorContext.Provider value={{ color: "red" }}>
      <div>
        <ColorBox />
      </div>
    </ColorContext.Provider>
  );
};

export default App;
```

- createContext 함수를 사용할 때는 Context의 기본값을 넣어주었다.(black)
- 이 때의 기본값은 Provider를 사용하지 않았을 때만 사용된다.

**주의할점!)**

다음과 같이 Provider를 사용하였는데 value값을 명시하지 않으면 기본값을 사용하지 않았기 때문에 오류가 발생한다. 

```jsx
import React from "react";
import ColorBox from "./components/ColorBox";
import ColorContext from "./contexts/color";

const App = () => {
  return (
    <ColorContext.Provider>
      <div>
        <ColorBox />
      </div>
    </ColorContext.Provider>
  );
};

export default App;
```

# 3. 동적 Context 사용하기

<aside>
✅ Context의 value에는 고정 값이 아닌 함수를 전달해 줄 수도 있다!

</aside>

## 1) 동적 Context생성하기

**context/color.js 수정 )**

```jsx
import { createContext } from "react";

const ColorContext = createContext({
  state: { color: "black", subcolor: "yellow" },
  actions: {
    setColor: () => {},
    setSubcolor: () => {},
  },
});

const ColorProvider = ({ children }) => {
  const [color, setColor] = useState("black");
  const [subcolor, setSubcolor] = useState("red");

  const value = {
    state: { color, subcolor },
    actions: { setColor, setSubcolor },
  };

  return (
    <ColorContext.Provider value={value}>{children}</ColorContext.Provider>
  );
};

//const ColorConsumer = ColorContext.Consumer와 같은의미
const { Consumer: ColorConsumer } = ColorContext;

//ColorProvider와 ColorConsumer 내보내기
export { ColorProvider, ColorConsumer };

export default ColorContext;
```

- ColorProvider라는 컴포넌트에서 value에는 상태는 state로, 업데이트 함수는 actions로 묶어서 전달하고 있다.
- state와 actions 객체를 따로 분리하면 다른 컴포넌트에서 Context의 값을 사용할 때 편하다.
- ColorContext 컴포넌트에서 createContext를 사용할 때 기본값으로 사용할 객체를 넣어주었다.
- 기본값은 Provider value에 넣는 객체의 형태와 일치시키는 것이 좋다.
- Context의 코드를 볼 때 내부 값을 파악하기 좋고, Provider를 사용하지 않을 시 에러 발생도 방지할 수 있다.

## 2) 동적 Context 적용하기

**App.js)**

```jsx
import React from "react";
import ColorBox from "./components/ColorBox";
import { ColorProvider } from "./contexts/color";

const App = () => {
  return (
    <ColorProvider>
      <div>
        <ColorBox />
      </div>
    </ColorProvider>
  );
};

export default App;
```

**components/ColorBox.js)**

```jsx
import React from "react";
import { ColorConsumer } from "../contexts/color";

const ColorBox = () => {
  return (
    <ColorConsumer>
      {(value) => (
        <>
          <div
            style={{
              width: "64px",
              height: "64px",
              background: value.state.color,
            }}
          />
          <div
            style={{
              width: "32px",
              height: "32px",
              background: value.state.subcolor,
            }}
          />
        </>
      )}
    </ColorConsumer>
  );
};

export default ColorBox;
```

**객체 비구조화 할당 문법을 사용해 value 조회 생략하기)**

```jsx
import React from "react";
import { ColorConsumer } from "../contexts/color";

const ColorBox = () => {
  return (
    <ColorConsumer>
      {({ state }) => (
        <>
          <div
            style={{
              width: "64px",
              height: "64px",
              background: state.color,
            }}
          />
          <div
            style={{
              width: "32px",
              height: "32px",
              background: state.subcolor,
            }}
          />
        </>
      )}
    </ColorConsumer>
  );
};

export default ColorBox;
```

## 3) 색상 선택 컴포넌트 만들기

Context의 actions에 넣어 준 함수를 호출하는 컴포넌트 만들기

**components/SelectColors.js )**

```jsx
import React from "react";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

const SelectColors = () => {
  return (
    <div>
      <h2>색상을 선택하세요.</h2>
      <div style={{ display: "flex" }}>
        {colors.map((color) => (
          <div
            key={color}
            style={{
              background: color,
              width: "24px",
              height: "24px",
              cursor: "pointer",
            }}
          />
        ))}
      </div>
      <hr />
    </div>
  );
};

export default SelectColors;
```

App.js에 렌더링하기)

```jsx
import React from "react";
import ColorBox from "./components/ColorBox";
import { ColorProvider } from "./contexts/color";
import SelectColors from "./components/SelectColors";

const App = () => {
  return (
    <ColorProvider>
      <div>
        <SelectColors />
        <ColorBox />
      </div>
    </ColorProvider>
  );
};

export default App;
```

마우스 왼쪽 버튼을 클릭하면 큰 정사각형이, 오른쪽 버튼을 클릭하면 작은 정사각형이 색상을 변경하도록 해보자)

**components/SelectColors.js )**

```jsx
import React from "react";
import { ColorConsumer } from "../contexts/color";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

const SelectColors = () => {
  return (
    <div>
      <h2>색상을 선택하세요.</h2>
      <ColorConsumer>
        {({ actions }) => (
          <div style={{ display: "flex" }}>
            {colors.map((color) => (
              <div
                key={color}
                style={{
                  background: color,
                  width: "24px",
                  height: "24px",
                  cursor: "pointer",
                }}
                onClick={() => actions.setColor(color)}
                onContextMenu={(e) => {
                  e.preventDefault(); //마우스 오른쪽 버튼 클릭 시 메뉴가 뜨는 무시함.
                  actions.setSubcolor(color);
                }}
              />
            ))}
          </div>
        )}
      </ColorConsumer>
      <hr />
    </div>
  );
};

export default SelectColors;
```

- onContextMenu : 오른쪽 버튼 클릭 이벤트

# 4. Consumer 대신 Hook 또는 static contextType 사용하기

## 1) useContext Hook 사용하기

**components/ColorBox.js)**

```jsx
import React, { useContext } from "react";
import ColorContext from "../contexts/color";

const ColorBox = () => {
  const { state } = useContext(ColorContext);
  return (
    <>
      <div
        style={{
          width: "64px",
          height: "64px",
          background: state.color,
        }}
      ></div>
      <div>
        style=
        {{
          width: "32px",
          height: "32px",
          background: state.subcolor,
        }}
      </div>
    </>
  );
};

export default ColorBox;
```

- children에 함수를 전달하는 Render Props 패턴이 불편하다면, useContext Hook을 사용하여 간편하게 Context 값을 조회할 수 있다.
- 주의할점은 함수형 컴포넌트에서만 적용이 가능하다는 점이다.

## 2) static contextType 사용하기

클래스형에서 Context를 더 쉽게 사용하고 싶다면, static contextType을 정의하는 방법이 있다.

**SelectColors 컴포넌트를 클래스형으로 수정하기)**

```jsx
import React, { Component } from "react";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

class SelectColors extends Component {
  render() {
    return (
      <div>
        <h2> 색상을 선택하세요.</h2>
        <div style={{ display: "flex" }}>
          {colors.map((color) => (
            <div
              key={color}
              style={{
                background: color,
                width: "24px",
                height: "24px",
                cursor: "pointer",
              }}
            />
          ))}
        </div>
        <hr />
      </div>
    );
  }
}

export default SelectColors;
```

**static contextType 값 지정하기)**

```jsx
import React, { Component } from "react";
import ColorContext from "../contexts/color";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

class SelectColors extends Component {
  static contextType = ColorContext;
  render() {
    return (
      <div>
        <h2> 색상을 선택하세요.</h2>
        <div style={{ display: "flex" }}>
          {colors.map((color) => (
            <div
              key={color}
              style={{
                background: color,
                width: "24px",
                height: "24px",
                cursor: "pointer",
              }}
            />
          ))}
        </div>
        <hr />
      </div>
    );
  }
}

export default SelectColors;
```

- 위와 같이 지정하면 this.context를 조회했을 때 현재 Context의 value를 가리키게 된다.

**SelectColors.js 완성하기)**

```jsx
import React, { Component } from "react";
import ColorContext from "../contexts/color";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

class SelectColors extends Component {
  static contextType = ColorContext;

  handleSetColor = (color) => {
    this.context.actions.setColor(color);
  };

  handleSetSubColor = (subcolor) => {
    this.context.actions.setSubColor(subcolor);
  };

  render() {
    return (
      <div>
        <h2> 색상을 선택하세요.</h2>
        <div style={{ display: "flex" }}>
          {colors.map((color) => (
            <div
              key={color}
              style={{
                background: color,
                width: "24px",
                height: "24px",
                cursor: "pointer",
              }}
              onClick={() => this.handleSetColor(color)}
              onContextMenu={(e) => {
                e.preventDefault();
                this.handleSetSubColor(color);
              }}
            />
          ))}
        </div>
        <hr />
      </div>
    );
  }
}

export default SelectColors;
```

# Q&A

Q1) 한 번에 어느 컴포넌트든 한 번에 원하는 값을 받아 와서 사용할 수 있게 해주는 기능은?

- 정답
    
    Context API
    

Q2) 컴포넌트의 children이 있어야 할 자리에 일반 JSX 혹은 문자열이 아닌 함수를 전달하는 것

- 정답
    
    Render Props
    

Q3) Hooks 중 Context를 더 쉽게 사용할 수 있게 해 주는 함수

- 정답
    
    useContext
    

Q4) 클래스형 컴포넌트에서 Context를 더 쉽게 사용할 수 있게 해 주는 함수

- 정답
    
    static contextType
