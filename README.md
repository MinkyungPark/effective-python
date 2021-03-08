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

<br><br><br>

# 파이썬 답게 생각하기 

### 1. Pythonic

- 명시적이고 단순하고 가독성이 좋은 것
- Easy to Read, Don't Repeat Yourself
  - 한줄로 작성해서 시각적 잡음을 일으키지 말자
  - or 이나 and를 식에 사용하는 것보다 if/else를 써라
  - 되도록 if/else문을 여러줄로 작성해서 명확하게 만들어줘야 한다.
  - 단지 2,3 번 반복되는 로직이라도 도우미 함수를 작성하자
  - 빈 문자열, 리스트, 0 모두 암시적으로 False가 된 다는 것을 이용하고, <br>
    딕셔너리 키가 없을 경우 KeyError 말고 get을 이용해라
      ```bash
      opacity = dic.get('투명도', [''])[0] or 0
      ```
  - 절대로 for, while 뒤에 else 사용하지 않기
  - 대입식을 사용해 반복을 피하기 (walrus operator/assignment expression)
  - switch문을 if/else의 향연으로 만들지 말고 walrus(대입식)를 이용하자
  - do while도 walrus(대입식) 이용하자

### 2. Dynamically-typted-interpreted-buffers-vectorization-compiled

- Interpreter

  : compile lang은 소스코드를 컴파일해서 실행 파일 run, <br>
  interpreter lang은 한줄씩 기계어로 번역

  - 인터프리터면서 컴파일러, 파이썬의 구현체
    - **Cpython** : <br>(compile) python code(.py) -> bytecode(.pyc)<br>(interpreter[virtual machine]) run<br>확인 import dis dis.dis(function)<br>
      GIL(global interpreter lock)을 사용하므로 하나의 스레드만 객체에 접근 가능
    - **Pypy** : <br>파이썬 자체로 구현되있어 빠르다.<br>JIT(just in time) 컴파일 : 필요시 즉석으로 컴파일

[why python is slow](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)

### 3. Version of Python

- 2.7 -> python(deprecated), 3이상 -> python3
- 현재 실행중인 버전 확인 sys.version_info || sys.version

### 4. Style

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

### 5. Types
- 문자열 Sequence<br>
: bytes에는 텍스트 인코딩 없고 str은 이진 인코딩이 없음<br>
unicode -> binary data : `str.encode()` // default UTF-8<br>
binary -> unicode : `bytes.decode()` // default UTF-8
  1. bytes
      - 부호가 없는 8바이트 데이터 
        ```bash
        a = b'h\x65llo'
        print(list(a))
        print(a)
        >>> [104, 101, 108, 108, 111]
            b'hello'
        ```
      - 종종 아스키 인코딩을 사용해 내부 문자 표시
  2. str
      - str 인스턴스에는 유니코드 code point가 들어있음
  - bytes와 str 는 _호환이 되지 않음._ <br>+,<,>,==,% 등의 연산자 사용할 수 없음
    ```bash
    print(b'foo' == 'foo') # False
    ```
  3. 파일 핸들과 관련된 연산들은 default로 unicode를 요구한다.
      ```bash
      with open('data.bin', 'w') as f:
        f.write(b'\xf1\xf2\xf3') # TypeError: write() argument must be str, not bytes
      ```
      텍스트모드 'w'가 아닌 이진 쓰기 모드 'wb'로 해결 할 수 있다. <br>
      READ도 마찬가지로 'r'가 아닌 'rb'를 이용하면 해결
      - system default encoding check
        ```bash
        $ python3 -c 'import locale; print(locale.getpreferredendcoding())')
        # default encoding이 의심스러운경우
        # 명시적으로 open에 encoding 파라미터 전달
        with open('data.bin', 'r', encoding='cp1252') as f: ~~..
        ``` 


### 6. Formatting
- Formatting 4가지 
  1. % 형식화 연산자
    - 형식 지정자 : %s, %d .. ex print('2진수: %d, 16진수 %d' % (x, y))
      - 문제점 : <br>
      오른쪽 튜플(()) 값의 타입이나 순서 바꿀 시 직접 검사<br>
      튜플을 딕셔너리로 바꾸면 직접 검사나 중복 기입 부분은 해결되지만 형식화 부분이 길어진다. <br>
  2. format(), str.format()
      ```bash
      $ help('FORMATTING')
      ```
      여전히 키 반복, 중복 등의 문제가 있음. 웬만하면 위 두개 사용X
  3. f-string: Interpolation
    - 형식문자열 f, 바이트 문자 b, raw 문자 r 붙이는 것과 비슷하다.

### 7. Unpacking
- 인덱스를 사용하기보다 언패킹을 사용해서 시각적 잡음을 줄이자.
  ```bash
  item = ('호박엿','식혜')
  first, second = item
  print(first, '&', second) # 호박엿 & 식혜
  ```
- 임시 변수를 사용하지 않고도 값을 바꿀 수 있다.
  ```bash
  a[i-1],a[i] = a[i], a[i-1]
  ```
- 모든 iterable에 unpacking이 적용 가능 -> enumerate
  - enumerate는 lazy generator
  - enumerate & zip
- 여러 계층의 경우도 가능 ex) (key, (name, val))

---
<br><br><br>

# List and Dictionary

- python dictionary
  - hash table, associative array
  - 분할 상환(Armotization) 방식으로 상수 시간의 복잡도를 가짐
  - 동적 정보를 저장하기 이상적
  - 물론 데이터를 추가만하고 조회를 잘 안쓴다면 Armotization의 연산 빈도에 대해 가정한 내용이 깨져서 효율적이지 않을 수 있다.

### 8. Sequence Slicing
- 어떤 클래스에서도 사용이 가능하다.
- __getitem___ __setitem___

<br><br><br>

# title

### Generateor
- generator : iterator를 생성해주는 함수, 함수 안에 yield 키워드를 사용
  - enumerate
  - zip
    - 가장 짧은 길이의 이터레이터가 끝날 때 까지 튜플을 내놓는다.
    - 가장 긴 길이의 이터레이터를 내놓으려면 zip_longest

### Comprehension


- if/else
- try/except
- try/except/else
- try/exceipt/else/finally
- try/finally