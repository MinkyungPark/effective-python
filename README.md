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

- 파일명 소문자와 \_
- PEP 8 스타일 가이드

### ✔️ D

### ✔️ D

### ✔️ D
