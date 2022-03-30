# Three.js란?

**WebGL**

- 웹 상에서 그래픽을 표편할 때 쓰는 라이브러리
- JS를 사용한다
- 2D, 3D 그래픽을 표현한다. (특히 3D)

<장점>

- GPU를 이용해서 그림을 그리기 때문에 성능이 좋다.

<단점>

- Low level 이기 때문에 간단한 도형을 구현해도 개발시간이 오래 걸리게 된다.

→ Three.js는 이런 WebGL을 쉽고 간편하게 사용할 수 있게 해주는 라이브러리 이다.

# 개발 준비하기

- vscode 사용 → live server 확장 팩 설치
- chrome 사용

# three.js 사용 방법 1

three.js

three.min.js(압축 버전)

**→ html에 src속성에 경로를 넣고 쓸 때 사용**

three.module.js

**→ js 모듈방식을 이용해 사용**

# 자바스크립트 module 기본

**module을 쓰는 이유**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <script src="hello.js"></script>
    <script src="main.js"></script>
  </body>
</html>
```

위와 같이 불러와야 할 js가 여러 개일 경우 하나하나 추가하는 것은 번거롭다.

이 때, 모듈을 쓰면 main이 되는 js에 다른 js를 불러와 한번에 추가할 수 있게 된다.

```jsx
export function hello1() {
  console.log("Hello 1!");
}
```

내보낼 js함수에는 export 키워드를 붙여준다.

```jsx
import { hello1 } from "./hello.js";

hello1();
```

js함수를 불러올 때는 import를 사용한다.

함수를 불러왔기 때문에 {}를 사용한다.

from 다음엔 경로를 붙여준다.

그리고 호출한다.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <!-- <script src="hello.js"></script> -->
    <script type="module" src="main.js"></script>
  </body>
</html>
```

module방식을 써야 하기 때문에 type을 설정해준다.

**여러 함수를 import 시킬 경우**

```jsx
// import { hello1, hello2 } from "./hello.js";
import * as hello from "./hello.js";

hello.hello1();
helllo.hello2();
```

첫 번째 방식처럼 모든 함수를 {}안에 불러와도 되지만,

\*를 써서 모든 함수를 불러온 후, as키워드를 통해 이름을 붙이고 object처럼 사용할 수 있다.

```jsx
import hello1 from "./hello.js";

hello1();
```

{}를 쓰지 않을 경우 default 에러가 뜨는데,

```jsx
export default function hello1() {
  console.log("Hello 1!");
}
```

이렇게 기본 값을 지정해 주면 {}를 쓰지 않고 사용할 수 있다.

# three.js 사용 방법 2

three.module.js 사용법

```jsx
<script type="module" src="main.js"></script>
```

```jsx
import * as THREE from "./three.module.js";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);

  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;

  renderer.render(scene, camera);
}

animate();
```

# 웹팩(Webpack) 살펴보기

**번들링**이란?

js파일들, 이미지, css등을 하나의 모듈로 보고, 이런 모듈들을 배포용으로 포장하는 작업을 말한다.

이런번들링 작업을 수행하는 툴들을 **번들러** 라고 한다.

이 번들러 중 가장 인기있는 친구가 바로 **웹팩**!

[webpack](https://webpack.js.org/)

**웹팩 다운 받기** → [https://github.com/jmyoow/webpack-js-html](https://github.com/jmyoow/webpack-js-html)

**웹팩 살펴보기**

1. package.json의 devDependencies

- 우리 프로젝트를 다른 사람이 다운받아서 쓸 때, `npm i` 명령만 입력해도 devDependencies의 모든 패키지들이 자동으로 설치 된다.
- `npm i -D` 처럼 D옵션을 주면 개발환경에서만 사용할 패키지라는 것을 알리는 것이다.
  - -D 옵션을 주지 않으면 dependencies에 설치가 된다.
  - 웹팩 자체가 개발 시 사용하는 것이기 때문에 웹팩과 관련된 것은 -D옵션을 주도록 하자.

2. src 폴더

- 우리가 개발할 소스코드들이 들어갈 곳이다.

3. dist 폴더

- `npm run build` 명령어로 생성된 폴더, 최종 배포할 파일들이 올라가게 된다.
- dist폴더를 통째로 웹 서버에 올리면 배포 짜란~

4. webpack.config.js

- webpack 설정 파일
- 코드 자세히 보기

```jsx
entry: {
	main: './src/main.js', //js 모듈 빌드시 시작점이 되는 파일
},
output: {
	path: path.resolve('./dist'),
	filename: '[name].min.js'
},
devServer: { //소스코드 고치면 자동 새로고침 해주는 설정
	liveReload: true
},
optimization: { //빌드시 소스코드 압축 되도록 하는 설정
		minimizer: webpackMode === 'production' ? [
			new TerserPlugin({ //최종 배포용 파일에서 콘솔로그 날려주는 설정
				terserOptions: {
					compress: {
						drop_console: true
					}
				}
			})
		] : [],
		splitChunks: {
			chunks: 'all'
		}
	},
```

- **babel**
  최신 문법으로 개발한 자바스크립트를 예전 브라우저에서도 잘 돌아가도록 변환해주는 역할을 한다.
- dist 폴더에 복제시킬 파일들
  ```jsx
  new CopyWebpackPlugin({
    patterns: [
      { from: "./src/main.css", to: "./main.css" },
      { from: "./src/images", to: "./images" },
    ],
  });
  ```

**Custom해서 웹팩 사용해보기**

# three.js 사용 방법 3

```jsx
1. 모듈 설치
터미널에 아래 점선 사이의 내용을 붙여 넣고 엔터를 누르세요.
----------
npm i -D @babel/cli @babel/core @babel/preset-env babel-loader clean-webpack-plugin copy-webpack-plugin core-js cross-env html-webpack-plugin source-map-loader terser-webpack-plugin webpack webpack-cli webpack-dev-server
----------
npm i three
----------

2. 개발용 서버 구동
터미널에 아래 점선 사이의 내용을 붙여 넣고 엔터를 누르세요.
----------
npm start
----------

3. 빌드(배포용 파일 생성)
터미널에 아래 점선 사이의 내용을 붙여 넣고 엔터를 누르세요.
----------
npm run build
----------

(!)
npm start 또는 npm run build 실행 시 에러가 난다면 Node.js를 LTS 버전(장기 지원 버전)으로 설치 후 다시 시도해 보세요.
터미널에 아래 점선 사이의 내용을 붙여 넣고 엔터를 누르면 설치할 수 있어요.
----------
n lts
----------

(!)
ERROR in unable to locate '경로...'
위와 같은 에러가 발생한다면, webpack.config.js의 CopyWebpackPlugin에 설정된 파일이 있는지 확인해주세요.
CSS나 이미지 폴더 등이 필요하지 않다면 webpack.config.js에서 CopyWebpackPlugin 부분 전체를 주석 처리 해주세요.
```

**main.js에서 three.js 불러오는법**

웹팩을 사용하기 때문에 다음과 같이 import 해온다.

`import * as THREE from "three";`

→ Webpack을 이용한 방법을 기본으로 진행
