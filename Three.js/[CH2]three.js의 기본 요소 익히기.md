# 기본 장면 구성요소 살펴보기

![강사님 그림이 훨씬 귀엽지만 ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f73be92a-4af4-40eb-b94a-849c891cd1ac/084B7A37-7E61-45AE-B4C9-8E5569AE426E.jpeg)

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
