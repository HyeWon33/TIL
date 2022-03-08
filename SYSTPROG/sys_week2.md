## 22년 03월 08일 화요일

# 0. setting

- python 3.7 download

- pycharm download

# 1. 수업 계획

- 교재는 블로그

- 출석, 숙제, 중간 프로젝트, 기말 프로젝트

# 2. Intorduction to Python

## 2.1 파이썬 유래

## 2.2 python 2 vs 3

- python3 내용만 봐라

## 2.3 파이썬의 철학

## 2.4 파이썬의 특징

### 2.4.1 문법이 간결하고 쉽다.

### 2.4.2 인간의 언어와 비슷하다.

### 2.4.3 인터프리터 언어다.

### 2.4.4 동적 타임을 지원한다.

### 2.4.5 오픈 소스(open-source)다.

- 터미널에서 명령어로 다운로드 

  - ``` 
    pip install numpy
    ```

# 3. Number and String in Python

## 3.1 파이썬 변수와 타입

``` python
a = "hello"
print("type:", type(a), "value:", a)
# > type: <class 'str'> value: hello

a = 1234
print("type:", type(a), "value:", a)
# > type: <class 'int'> value: 1234

a = 1.234
print("type:", type(a), "value:", a)
# > type: <class 'float'> value: 1.234

a = True	# False도 있는데 첫 문자는 대문자로 써야 한다.
print("type:", type(a), "value:", a)
# > type: <class 'bool'> value: True
```



## 3.2 숫자 타입

### 3.2.1 숫자 연산자

```python
import sys
a = 1234
b = 1.7
print("float", type(a), sys.getsizeof(a))
print("integer", type(b), sys.getsizeof(b))

# 기본적인 사칙연산
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 거듭제곱
print(b ** 2)
# 나누기 후 나머지
print(a % b)
# 나누기 후 몫 . 정수로만 숫자 써준다.
print(a // b)
```

### 3.2.2 연습문제

``` python
a = 13
print(a**3) #2197
print(13**3)

print(hex(a**3)) #0x895

-----------------------

num = 13**3
print(num // 16**2) #8
n3 = num // 16**2
r3 = num % 16**2
n2 = r3// 16
n1 = num % 16
print(n3, n2, n1, r3)
```

## 3.3 조건문(if)과 비교 연산자

```python
if cond1:
    statement1
    statement2
elif cond2:
    statement3
    statement4
else:
    statement5
```

```python
print("if statements")
if 13 ** 3 > 50 **2:
    print("13**2 > 50**2")
elif 13 ** 3 != 2197:
    print("13**3 != 2197")
elif 13 ** 3 >= 30 **2:
    print("13**3 >= 30**2")
else:
    print("13**3 < 30**2")
```

