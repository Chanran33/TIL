# 기본 장면 구성요소 살펴보기



# 기본 장면 만들기 - Renderer

### Canvas 붙이는 방법 2가지

1.  appendChild를 이용해 body밑에 canvas(renderer.domElement) 붙여주기

    `document.body.appendChild(renderer.domElement);`

2.  index.html의 <body>태그안에 미리 <canvas> 만들어놓기

        ```html
        <body>
          <canvas></canvas>
        </body>
        ```
    → 이쪽이 활용범위가 더 높다!

    ```html
    <body>
      <canvas></canvas>
    </body>
    ```

    ```jsx
    const canvas = document.querySelector("#three-canvas");
    const renderer = new THREE.WebGLRenderer({ canvas: canvas });
    //속성이랑 값이 같을 때는 한번만 써줘도 된다.
    //ex)({ canvas })
    renderer.setSize(window.innerWidth, window.innerHeight);
    ```

# 기본장면 만들기 - Camera

### scene 만들기

```jsx
const scene = new THREE.Scene();
```

### 카메라 만들기

PerspectiveCamera(fov, aspect, near, far)

- fov: 시야각
- aspect: 화면의 가로 세로 비율
- near: 어느정도 가까이 오면 안보이게 할지(가까운 쪽 한계)
- far: 어느정도 멀리 오면 안보이게 할지(먼 쪽 한계)

```jsx
//Camera
const camera = new THREE.PerspectiveCamera(
  75, //시야각(field of view)
  window.innerWidth / window.innerHeight, //종횡비(aspect)
  0.1, //near
  1000 //far
);

camera.position.z = 5;
```

# 기본장면 만들기 - Mesh(물체)

### 물체 만들기

```jsx
//Mesh
const geometry = new THREE.BoxGeometry(1, 1, 1); //직육면체 만들기
const material = new THREE.MeshBasicMaterial({
  // color: 0xff0000
  // color: '#ff0000'
  color: "red",
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh); //scene(무대)에 올리기
```

### 그리기

```jsx
//그리기
renderer.render(scene, camera);
```

<div style="display:flex;">
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/feb986b3-af9f-4c96-88c4-55ec1c393c8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220414T140729Z&X-Amz-Expires=86400&X-Amz-Signature=345637e4fcedcc245c8a5b13074110fb338af98431c36c83ca180c0f5a4f7a1d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" width="300" />
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7bc216bc-fafc-4ee6-9f6f-363369d2588d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220414T140900Z&X-Amz-Expires=86400&X-Amz-Signature=db430f54ab9dec2258c716d1dbbfc7723730c32bde10e8c9883c034f9ea0eb29&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" width="300"/>
</div>

### Anti aliaasing(안티애리어싱) 처리해주기

renderer에서 처리해주면 된다.

```jsx
const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
});
```

연산이 추가되기 때문에 성능저하가 생길 수 있다.

# 직교 카메라(Orthographic Camera)

Perspective Camera

- 사람 눈이 보는 것처럼 원근이 적용되어 있다.

Orthographic Camera

- 원근에 따라 물체의 크기가 다르지 않다.
- 하늘에서 보는 것과 같은 뷰
- **디아블로, 롤**과 같은 게임에서 많이 사용한다.

<img src="https://i.stack.imgur.com/q1SNB.png" width="500px" />
    
### 카메라 만들기

OrthographicCamera(left, right, top, bottom, near, far)

- left: 카메라 절두체 좌평면
- right: 카메라 절두체 우평면
- top: 카메라 절두체 상평면
- bottom: 카메라 절두체 하평면,
- near: 카메라 절두체 근평면,
- far: 카메라 절두체 원평면

(절두체: 입체를 절단하는 하나나 두 평행면 사이의 부분)
