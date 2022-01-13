# CSS 개요

## 1. 기본 문법, 주석

**기본문법)**

`선택자 { 속성: 값; }`

- 선택자 : 스타일(CSS)를 적용할 대상(Selector)
- 속성 : 스타일(CSS)의 종류(Property)
- 값 : 스타일(CSS)의 값(Value)

ex) `div{ color: red; }`

**여러 가지 스타일 지정 하기)**

`선택자 { 속성: 값; 속성: 값; }`

ex) `div { color: red; margin: 20px; }`

**주석 달기)**

`/* 주석 */`

- 단축키 : Ctrl + /

## 2. 선언 방식

> 💡 CSS 선언 방식에는 내장방식, 링크방식, 인라인 방식, @import 방식 이렇게 4가지가 있다.

**1) 내장방식**

<style></style>의 내용(Contents)로 스타일을 작성하는 방식

```html
<style>
  div {
    color: red;
    margin: 20px;
  }
</style>
```

**2) 링크 방식**

<link />로 외부 CSS 문서를 가져와서 연결하는 방식

```html
<link rel="stylesheet" href="./css/main.css" />
```

```css
div {
  color: red;
  margin: 20px;
}
```

**3) 인라인 방식**

요소의 style 속성에 직접 스타일을 작성하는 방식

```html
<div style="color: red; margin: 20px;"></div>
```

**4) @import 방식**

CSS의 @import 규칙으로 CSS 문서 안에서 또 다른 문서를 가져와 연결하는 방식

```html
<link rel="stylesheet" href="./css/main.css" />
```

```css
@import url("./box.css");

div {
  color: red;
  margin: 20px;
}
```

```css
.box {
  background-color: red;
  padding: 20px;
}
```

## 3. CSS 선택자\_기본

**1) 전체 선택자\_Universal Selector)**

모든 요소를 선택.

ex)

```css
* {
  color: red;
}
```

**2) 태그 선택자(Type Selector)**

태그 이름으로 요소 선택.

ex)

```css
li {
  color: red;
}
```

**3) 클래스 선택자(Class Selector)**

HTML class 속성의 값이 ABC인 요소 선택.

ex)

```css
.orange {
  color: red;
}
```

**4) 아이디 선택자(ID Selector)**

HTML id 속성의 값이 ABC인 요소 선택.

ex)

```css
#orange {
  color: red;
}
```

> 💡 기본 선택자 4개는 순서대로 알아두기!

## 4. 선택자\_복합

**1) 일치 선택자(Basic Combinator)**

선택자 2를 동시에 만족하는 요소 선택.

ex) span(태그 선택자)와 .orange(클래스 선택자)를 동시에 선택

```css
span.orange {
  color: red;
}
```

→ `<span class=”orange”>오렌지</span>` 이곳에 css적용!

**2) 자식 선택자(Child Combinator)**

선택자의 자식요소 선택.

ex)

```css
ul > .orange {
  color: red;
}
```

```html
<div>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li class="orange">오렌지</li>
  </ul>
</div>
```

→ `<li class="orange">오렌지</li>` 이곳에 CSS 적용!

**3) 하위(후손) 선택자(Descendant Combinator)**

선택자의 **하위** 요소 선택.

‘띄어쓰기’가 선택자의 기호!

ex)

```css
div .orange {
  color: red;
}
```

```html
<div>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li class="orange">오렌지</li>
    //CSS적용!
  </ul>
  <div>당근</div>
  <p>토마토</p>
  <span class="orange">오렌지</span> //CSS적용!
</div>
<span class="orange">오렌지</span> //CSS 미적용!
```

**4) 인접 형제 선택자(Adjacent Sibling Combinator)**

`ABC + XYZ`

선택자 `ABC`의 다음 형제 요소 `XYZ`하나를 선택.

ex)

```css
.orange + li {
  color: red;
}
```

```html
<ul>
  <li>사과</li>
  <li>딸기</li>
  <li class="orange">오렌지</li>
  <li>망고</li>
  //CSS적용!
  <li>사과</li>
  //하나만 찾기 때문에 CSS미적용!
</ul>
```

## 5. 선택자\_가상 클래스(1)

## 6. 선택자\_가상 클래스(2)

## 7. 선택자\_가상 요소

## 8. 선택자\_속성

## 9. 스타일 상속

## 10. 선택자 우선순위
