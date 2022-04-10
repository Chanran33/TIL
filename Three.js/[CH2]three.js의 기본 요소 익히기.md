# 기본 장면 구성요소 살펴보기

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f73be92a-4af4-40eb-b94a-849c891cd1ac/084B7A37-7E61-45AE-B4C9-8E5569AE426E.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220330T153803Z&X-Amz-Expires=86400&X-Amz-Signature=15deebc7e657f2d38a518c217042b9193efd7ee81c88b80a44d30830928a51e3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22084B7A37-7E61-45AE-B4C9-8E5569AE426E.jpeg%22&x-id=GetObject" width="500"/>

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
