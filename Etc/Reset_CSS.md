# 브라우저 스타일 초기화 하기

[reset-css CDN by jsDelivr - A CDN for npm and GitHub](https://www.jsdelivr.com/package/npm/reset-css)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/408bd3a4-f07e-4d2b-9a2c-a8c23638a3f7/Untitled.png)

- reset.css : 원본 파일
- reset.min.css : 경량화 된 파일

<aside>
💡 파일명.min.확장자와 같이 min(Minify 단어의 약어) 키워드는 파일이 난독화나 경량화 되었다는 것을 의미한다. 우리가 외부에서 가져와 사용하는 플러그인, 라이브러리 등을 직접 수정할 상황은 매우 드물기 때문에 굳이 원본을 사용할 필요가 없다.

</aside>

```jsx
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css">
```
