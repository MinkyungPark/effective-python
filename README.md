# EFFECTIVE PYTHON

```bash
파이썬 코드를 더 빠르게 실행시킬수 있는 방법
> 정렬된 리스트 검색시 bisect 사용하기

오류를 줄일 수 있는 방법
> 별표 식을 사용해 언패킹 하기

파이썬다운 코드를 작성하는 방법
> zip으로 여러 리스트 동시에 이러테이션 하기

과 같은 팁과 스킬을 배울 수 있음
```

<br>

### 📌 Keyword

- 제너레이터, 이터레이터, 데코레이터
- 왈라스 연산자
- 다형성
- 메타클래스
- 디스크립터
- 동시성/병렬성
- 스레드, 큐, 코루틴, 이벤트루프, 비동기
- 프로파일링, 모킹과 테스트
- 가상 환경
- 타입 힌트
- 경고

[코드1](https://github.com/gilbutITbook/080235)
[코드2](https://github.com/bslatkin/effectivepython)

---

<br>

## 1. Python

### ✔️ Pythonic

- 명시적이고 단순하고 가독성이 좋은 것

### ✔️ Dynamically-typted-interpreted-buffers-vectorization-compiled

- Interpreter

  : compile lang은 소스코드를 컴파일해서 실행 파일 run, <br>
  interpreter lang은 한줄씩 기계어로 번역

  - 인터프리터면서 컴파일러, 파이썬의 구현체
    - **Cpython** : <br>(compile) python code(.py) -> bytecode(.pyc)<br>(interpreter[virtual machine]) run<br>확인 import dis dis.dis(function)<br>
      GIL(global interpreter lock)을 사용하므로 하나의 스레드만 객체에 접근 가능
    - **Pypy** : <br>파이썬 자체로 구현되있어 빠르다.<br>JIT(just in time) 컴파일 : 필요시 즉석으로 컴파일

[why python is slow](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)

### ✔️ Version of Python

- 2.7 -> python(deprecated), 3이상 -> python3
- 현재 실행중인 버전 확인 sys.version_info || sys.version

### ✔️ Style

- vscode에서 formatting, pylint와 Black를 이용하기
- [PEP 8 스타일 가이드](https://www.python.org/dev/peps/pep-0008/), [번역](https://wikidocs.net/7896)
- 파일명, 함수, 변수, 애트리뷰트 lowercase_underscore [snake case]
- 클래스 CapitalizedWord [camel case]
- 모듈 수준 상수 ALL_CAPS

---

- instance method of class의 first argument명은 반드시 'self'
- class method의 first argument명은 반드시 'cls'
- 보호되야 하는 instance attribute -> \_leading_underscore
- private instance attribute -> \_\_leading_underscore

---

- 1줄 79개 문자 이하, 다음 줄 4칸 스페이스
- 각 함수와 클래스 사이에는 두 줄 띄기
- 클래스 안 메스더와 메서드 사이는 한 줄 띄기
- dic = {key: value, key: value}

---

- 빈컨테이너([]), 빈 시퀀스('') 검사 len X, 암묵적으로 False 취급 이용, <br>
  if not Container/Sequece 이용, 비어있지 않은 경우 if Container/Sequece
- 한 줄 짜리 if, for, while 루프, except 복합문 X 여러줄에 배치
- 식 줄바꿈 할 경우 \대신 식을 괄호로 싸고 줄바꿈 들여쓰기

---

- from package import module에서 package명 되도록 생략X <br>
  상재 경로 임포트 하는 경우 from . import module
- import 명시 순서 -> 표준 라이브러리, 서드 파티, 직접 만든 모듈 순 그리고 알파벳 순

<br>

### ✔️ D

### ✔️ D

### ✔️ D

`
