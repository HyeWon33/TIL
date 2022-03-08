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

### 3.3.1 is, and, or, in 연산자

```python
# # foo = 10
# # bar = 10
# # print(foo == bar)
# # print(foo is bar)

# foo = [10]
# bar = [10]
# goo = foo #주소복사
# print(foo == bar)
# print(foo is bar)
# print(goo is foo)

# # #C언어로 따져보면
# # int* foo = {10};
# # int* bar = (10);
# # int* goo = foo;

# foo [0] = 20
# print(foo, bar, goo)

foo = [1, 2]
bar = [1, 2]
print("foo == bar:", foo == bar)
print("foo is bar:", foo is bar)
goo = bar
goo[0] = 0
print("bar, goo:", bar, goo)
print("foo == goo", foo == goo)
print("bar is goo", bar is goo)
```

```python
value = 12
if(value % 2 == 0) and (value > 10):
    print("value is even and less than 12")
if(value % 2 != 0) or (value < 0):
    print("value is odd or negative")
```

## 3.4 문자열 타입

- 파이썬에서 문자열 다루기 편리하다.

```python
string1 = "Life is too short"
string2 = 'You need python'
# "" 이나 '' 상관 없다.
print("type(string1):", type(string1))

# 문자열 안에 따옴표(', ") 입력
print("Life 'is' too short")
print('Life "is" too short')

print("Life \"is\" too short,\nYou \'need\' python")
안녕 = 10
print(안녕)

print("Life is too short. \n\tyou need python")
```

### 3.4.1 문자열 연산

```python
print("날 " + ("너무" * 3 + " ")*5  + "좋아하면 그때 말해줘")
print("내가 " + ("자꾸" * 3 + " ")*5 + "떠오르면 그때 불러줘")
```

### 3.4.2 문자열 인덱싱과 슬라이싱

```python
text = "Life is too short, You need Python"
# Life is too short, You need Python
# 0         1         2         3 
# 0123456789012345678901234567890123
#                                -2-1
print("print 't'", text[8], text[16], text[30]) #문자

print("slice 'Life'", text[0:4]) #문자열
print("slice 'Life'", text[:4])

print("slice 'short':", text[12:17])

print("slice 'Python':", text[28:34])
print("slice 'Python':", text[28:])

print("slice 'need'", text[23:28])
print("slice 'need'", text[23:-7])

#인덱싱 하면 문자 나오고 슬라이싱 하면 문자열 나온다.
```

### 3.4.3 문자열 포매팅(Formatting)

#### 포맷 코드를 이용한 방법

```python
print("class : %s" % "marrior")
print("HP: %d" % 100)
print("DPS: %f" % 123.12)

pattern = "class: %10s, HP: %5d, DPS: %10.3f"
print(pattern % ("warrior", 100, 145.112))
print(pattern % ("healer", 50, 120.1))
```

#### format함수를 이용한 방법

```python
line1 = "class: {}".format("warrior")
print(line1)
print("HP: {}, DPS: {}".format(100, 123.12))	

pattern = "class: {:<10}, HP: {:<5}, DPS: {:<10.3f}"
print(pattern.format("warrior", 100, 123.12))
print(pattern.format("healer", 200, 834.79))
```

- 교재 https://wikidocs.net/13#format를 보면 `format()` 함수의 인자가 들어가는 순서를 명시적으로 지정하는 방법도이 나와있다.
  순서 지정: `"{0} {1}".format(1, 2)`
  별명 지정: `"{first} {second}".format(first=1, second=2)`
  혼합 지정: `"{} {second}".format(1, second=2)`
  이러한 코드는 결과를 더 명시적으로 예측할 수 있게 해준다. 다만 손이 더 가므로 본문의 예시와 같이 입력 순서를 이용해도 무방하다.

  - ```python
    print("{first} {second}".format(first=1, second=2))
    ```

#### f문자열 포매팅

- 요즘 많이 쓴다.
- 옆으로 길어진다.

```python
_class = "warrior"
HP = 100
DPS = 1456.23

print(f"class:{_class:10}, HP={HP:5}, DPS={DPS:8}")

print(f"class:{'healer':<10}, HP={150:>5}, DPS={123.12:8.5f}")
```

### 3.4.4 문자열 함수

#### count

```python
text = "날 " + ("너무" * 3 + " ")*5 + "좋아하면 그때 말해줘"
print(text)
print("count '너무':", text.count('너무'))
```

#### find, index

- 둘다 인덱스를 리턴 하지만 find 함수는 원하는 문장을 못 찾으면 -1 반환 index 함수는 에러를 내버린다.

```python
text = "For the python, of the python, by the python"
pyind = text.find("python")
print("frist index : ", pyind)
#다음 파이썬 찾을려면 방금 찾은 위치 다음부터 찾게 만든다.
pyind = text.find("python", pyind + 1)
print("second index : ", pyind)
pyind = text.find("python", pyind + 1)
print("third index : ", pyind)
pyind = text.find("ruby")
print(f"'ruby' found at {pyind} in `{text}`")	
```

```python
text = "For the python, of the python, by the python"
pyind = text.index("python")
print("frist index : ", pyind)
#다음 파이썬 찾을려면 방금 찾은 위치 다음부터 찾게 만든다.
pyind = text.index("python", pyind + 1)
print("second index : ", pyind)
pyind = text.index("python", pyind + 1)
print("third index : ", pyind)
# pyind = text.index("ruby")
# print(f"'ruby' found at {pyind} in `{text}`")

try:
    pyind = text.index("hello")
except Exception as e:
    print(e) #e는 예외객체
```

#### upper, lower

```python
mixed = "PYthon"
small = "python"

print(mixed == small)
print(mixed.lower())
print(mixed.upper())
print(mixed.lower() == small.lower()) #내용 같은지 확인 가능
```

#### strip, lstrip, rstrip

```python
wise_saying = ' "Walking on water and developing software ' \
            'from a specification are easy if both are frozen..." '

print(wise_saying)

wise_saying = wise_saying.strip()
print(wise_saying)
wise_saying = wise_saying.strip('"')
print(wise_saying)
wise_saying = wise_saying.rstrip('.')
print(wise_saying)
```

#### replace

```python
from wave import Wave_write


Lincoln_said = "for the people, by the people, of the people"
print(Lincoln_said)
We_say = Lincoln_said.replace("people", "python")
print(We_say)
We_say = Lincoln_said.replace("the ", "")
print(We_say)
```

#### split

```python
print(We_say.split(","))
```

