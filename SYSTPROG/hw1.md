# 1. 응용

## 1. 파이썬 변수와 타입


```python
ex = "bye"
print("type : ", type(ex), "value : ", ex)
ex = "4321"
print("type : ", type(ex), "value : ", ex)
ex = "4.321"
print("type : ", type(ex), "value : ", ex)
ex = "False"
print("type : ", type(ex), "value : ", ex) 
```

    type :  <class 'str'> value :  bye
    type :  <class 'str'> value :  4321
    type :  <class 'str'> value :  4.321
    type :  <class 'str'> value :  False
    


```python
import numpy as np
import pandas as pd
exarray = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]
print("exarray : \n",exarray)
exarray = np.array(exarray)
print("np.array : \n",exarray)
exarray = pd.DataFrame(exarray)
print("pd.DataFrame : \n",exarray)
```

    exarray : 
     [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]
    np.array : 
     [[1.1 2.2 3.3]
     [4.4 5.5 6.6]
     [7.7 8.8 9.9]]
    pd.DataFrame : 
          0    1    2
    0  1.1  2.2  3.3
    1  4.4  5.5  6.6
    2  7.7  8.8  9.9
    

## 2. 숫자 타입


```python
import sys
aa = 1.5
bb = 2
print("float ", type(aa), sys.getsizeof(aa))
print("integer ", type(bb), sys.getsizeof(bb))

print(aa + bb)
print(aa - bb)
print(aa * bb)
print(aa / bb)
print(aa ** 2)
print(aa % bb)
print(aa // bb)
```

    float  <class 'float'> 24
    integer  <class 'int'> 28
    3.5
    -0.5
    3.0
    0.75
    2.25
    1.5
    0.0
    

## 3. 조건문(if)과 비교 연산자


```python
print("--if statments--")
if 12 // 3 > 42 // 14:
    print("12 // 3 > 42 // 14")
elif 12 // 3 != 42 // 14:
    print("12 // 3 != 42 // 14")
elif 12 // 3 >= 42 // 14:
    print("12 // 3 >= 42 // 14")
else:
    print("12 // 3 < 42 // 14")
```

    --if statments--
    12 // 3 > 42 // 14
    

### is, and, or, in 연산자


```python
print('float "is" and "=="')
intvar = 12.1
print("intvar == 12.1 : ", intvar == 12.1)
print("intvar is 12.1 : ", intvar is 12.1)

print('\nbool "is" and "=="')
boolvar = False
print("boolvar == False : ", boolvar == False)
print("boolvar is False : ", boolvar is False)

print('\nList "is" and "=="')
foo = [1.1, 2.1]
bar = [1.1, 2.1]
print("foo == bar:", foo == bar)
print("foo is bar:", foo is bar)

print('\n"goo = bar" "is" and "=="')
goo = bar
goo[0] = 1
print("bar, goo:", bar, goo)
print("foo == goo", foo == goo)
print("bar is goo", bar is goo)
```

    float "is" and "=="
    intvar == 12.1 :  True
    intvar is 12.1 :  False
    
    bool "is" and "=="
    boolvar == False :  True
    boolvar is False :  True
    
    List "is" and "=="
    foo == bar: True
    foo is bar: False
    
    "goo = bar" "is" and "=="
    bar, goo: [1, 2.1] [1, 2.1]
    foo == goo False
    bar is goo True
    


```python
ex = 10.5
if (ex % 2 == 0) and (ex > 15):
    print("ex는 짝수고 15보다 크다.")
if (ex % 2 != 0) or (ex < 0):
    print("ex가 홀수거나 0보다 작다")
```

    ex가 홀수거나 0보다 작다
    

## 4. 문자열 타입


```python
ex1 = "Food"
ex2 = 'Coupon'

print("type(ex1) : ", type(ex1))
print("type(ex2) : ", type(ex2))

print("문자열 안에 '작은따옴표'")
print('문자열 안에 "큰따옴표"')

print("특수문자 기호 ==== \" : 큰따옴표, \' : 작은따옴표, \\ : 역슬래시, \t : 탭, \n : 줄바꿈 문자")
```

    type(ex1) :  <class 'str'>
    type(ex2) :  <class 'str'>
    문자열 안에 '작은따옴표'
    문자열 안에 "큰따옴표"
    특수문자 기호 ==== " : 큰따옴표, ' : 작은따옴표, \ : 역슬래시, 	 : 탭, 
     : 줄바꿈 문자
    

### 문자열 연산


```python
print(("뱅"*3 +" "+ "빵야"*2 + " ")*2)
```

    뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 
    

### 문자열 인덱싱과 슬라이싱


```python
a = "Life is too fast"
#    0123456789012345
print("index 's' : ", a[6], " ", a[14])
print("slicing 'Life is' : ", a[:7])
print("slicing 'too' : ", a[8:11])
print("slicing 'fast' : ", a[12:])
print("slice 'Life' : ", a[0:-12])
```

    index 's' :  s   s
    slicing 'Life is' :  Life is
    slicing 'too' :  too
    slicing 'fast' :  fast
    slice 'Life' :  Life
    

### 문자열 포매팅(Formatting)

#### 포맷 코드


```python
print("%d, %s -> %")
print("cm : %d" % 122)
print("kg : %f" % 22.2)

name = "kim"
cm = 122
kg = 22.2
pattern = "name : %5s, cm : %5d, kg : %10.2f"
char_intro = pattern % (name, cm, kg)
print(char_intro)
print(pattern % ("Lee", 133, 33.3))
```

    %d, %s -> %
    cm : 122
    kg : 22.200000
    name :   kim, cm :   122, kg :      22.20
    name :   Lee, cm :   133, kg :      33.30
    

#### format 함수


```python
print("{}.format()")
print("name : {}".format("Lee"))
print("cm : {}".format(144))
print("kg : {}".format(44.4))

name = "Lee"
cm = 144
kg = 44.4

pattern = "name : {:<5}, cm : {:<5}, kg : {:<5.2f}"
char_intro = pattern.format(name, cm, kg)
print(char_intro)
print(pattern.format("kim", 300, 13.2))
```

    {}.format()
    name : Lee
    cm : 144
    kg : 44.4
    name : Lee  , cm : 144  , kg : 44.40
    name : kim  , cm : 300  , kg : 13.20
    

#### f문자열


```python
name = "Lee"
cm = 144
kg = 44.4
char_intro = f"name : {name:<5}, cm : {cm:<5}, kg : {kg:<5.2f}"
print(char_intro)
char_intro = f"name : {'Ye':<5}, cm : {342:<5}, kg : {1.2:<5.2f}"
print(char_intro)
```

    name : Lee  , cm : 144  , kg : 44.40
    name : Ye   , cm : 342  , kg : 1.20 
    

### 문자열 함수


```python
print("count()")
bb = ("뱅"*3 +" "+ "빵야"*2 + " ")*2
print(bb)
print("count '뱅' : ", bb.count('뱅'))
```

    count()
    뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 
    count '뱅' :  6
    


```python
print("find(), index()")
bb = ("뱅"*3 +" "+ "빵야"*2 + " ")*2
pyind = bb.find("뱅")
print(f"'뱅' found at {pyind} in `{bb}`")
pyind = bb.find("뱅", pyind+1)
print(f"'뱅' found at {pyind} in `{bb}`")
pyind = bb.find("뱅", pyind+1)
print(f"'뱅' found at {pyind} in `{bb}`")
pyind = bb.find("뺑")
print(f"'뺑' found at {pyind} in `{bb}`")

pyind = bb.index("뱅")
print(f"'뱅' indexed at {pyind} in `{bb}`")
pyind = bb.index("뱅", pyind+1)
print(f"'뱅' indexed at {pyind} in `{bb}`")
pyind = bb.index("뱅", pyind+1)
print(f"'뱅' indexed at {pyind} in `{bb}`")
try:
    pyind = bb.index("뺑")
    print(f"'뺑' found at {pyind} in `{bb}`")
except ValueError as ve:
    print("'뺑' not indexed, value error:", ve)
```

    find(), index()
    '뱅' found at 0 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뱅' found at 1 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뱅' found at 2 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뺑' found at -1 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뱅' indexed at 0 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뱅' indexed at 1 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뱅' indexed at 2 in `뱅뱅뱅 빵야빵야 뱅뱅뱅 빵야빵야 `
    '뺑' not indexed, value error: substring not found
    


```python
print("upper(), lower()")
mixed = "BanG"
small = "bang"
print(f"compare mixed : {mixed} and small : {small}")
print(f"{mixed} == {small}:", mixed == small)
print(f"{mixed}.lower() == {small}:", mixed.lower() == small)
print(f"{mixed}.upper() == {small}.upper():", mixed.upper() == small.upper())
print(f"{mixed}.lower() is {small}.lower():", mixed.lower() is small.lower())
```

    upper(), lower()
    compare mixed : BanG and small : bang
    BanG == bang: False
    BanG.lower() == bang: True
    BanG.upper() == bang.upper(): True
    BanG.lower() is bang.lower(): False
    


```python
print("strip(), lstrip(), rstrip()")

wise_saying = '      "뱅뱅뱅 빵야빵야빵야 ' \
            '뱅뱅뱅 빵...야빵야빵야..." '
print(wise_saying)
wise_saying = wise_saying.strip()
print(wise_saying)
wise_saying = wise_saying.strip('\"')
print(wise_saying)
wise_saying = wise_saying.rstrip('.')
print(wise_saying)
```

    strip(), lstrip(), rstrip()
          "뱅뱅뱅 빵야빵야빵야 뱅뱅뱅 빵...야빵야빵야..." 
    "뱅뱅뱅 빵야빵야빵야 뱅뱅뱅 빵...야빵야빵야..."
    뱅뱅뱅 빵야빵야빵야 뱅뱅뱅 빵...야빵야빵야...
    뱅뱅뱅 빵야빵야빵야 뱅뱅뱅 빵...야빵야빵야
    


```python
print("replace")
B_said = "빵빵빵. 빵야빵야빵야. 빵빵빵"
We_say = B_said.replace("빵빵빵", "뱅뱅뱅")
emphasize = We_say.replace(".", "!")
print("Bang said : ", B_said)
print("We say:", We_say)
print("emphasize : ", emphasize)
```

    replace
    Bang said :  빵빵빵. 빵야빵야빵야. 빵빵빵
    We say: 뱅뱅뱅. 빵야빵야빵야. 뱅뱅뱅
    emphasize :  뱅뱅뱅! 빵야빵야빵야! 뱅뱅뱅
    


```python
print("split()")
B_said = "빵빵빵. 빵야빵야빵야. 빵빵빵"
We_say = B_said.replace("빵빵빵", "뱅뱅뱅")
print("split by words:", We_say.split("뱅"))
print("split by phrase:", We_say.split("."))
```

    split()
    split by words: ['', '', '', '. 빵야빵야빵야. ', '', '', '']
    split by phrase: ['뱅뱅뱅', ' 빵야빵야빵야', ' 뱅뱅뱅']
    

## 1. List


```python
a_list = []
b_list = list()
c_list = ['kim', '김', 3.2, False]
d_list = [['kim', '김'], [3.2, [False]]]
```

### 1.1 리스트 인덱싱과 슬라이싱


```python
print("'3.2'에 접근하기 -> 인덱싱")
print("c_list", c_list[2])
print("d_list", d_list[1][0])
print("c_list", c_list[-2])
print("d_list", d_list[-1][-2])

print("\n'3.2'에 접근하기 -> 슬라이싱")
print("c_list : ", c_list)
print("[start:end] : ", c_list[0:3])
print("[start:] : ", c_list[1:])
print("[:end] : ", c_list[:2])
print("[start:-end] : ", c_list[1:-1])
print("[:-end] : ", c_list[:-2])
print("[-start:-end] : ", c_list[-3:-1])
print("[partially overlap] : ", c_list[1:10])
print("[out of range] : ", c_list[9:100])
```

    '3.2'에 접근하기 -> 인덱싱
    c_list 3.2
    d_list 3.2
    c_list 3.2
    d_list 3.2
    
    '3.2'에 접근하기 -> 슬라이싱
    c_list :  ['kim', '김', 3.2, False]
    [start:end] :  ['kim', '김', 3.2]
    [start:] :  ['김', 3.2, False]
    [:end] :  ['kim', '김']
    [start:-end] :  ['김', 3.2]
    [:-end] :  ['kim', '김']
    [-start:-end] :  ['김', 3.2]
    [partially overlap] :  ['김', 3.2, False]
    [out of range] :  []
    

### 1.2 리스트 연산


```python
num = ["one", 'two', "three"]
han = ['가', "나", "다"]
numhan = num + han
print("list add : num + han = numhan = ",numhan)

ar = ["1", "2", "3"]
first_row = ar[0:1] + ar[1:2] + ar[2:3]
second_row = num
print("number")
print(first_row)
print(second_row)
```

    list add : num + han = numhan =  ['one', 'two', 'three', '가', '나', '다']
    number
    ['1', '2', '3']
    ['one', 'two', 'three']
    

### 1.3 리스트 관련 함수


```python
print("len()")
b = "bang"
print(f"len of '{b}' : ", len(b))
lis = ['ㅁ', 'ㄴ', 'ㅇ']
print(f"len of '{lis}' : ", len(lis))

print("\ndel")
lis = ['ㅁ', 'ㄴ', 'ㅇ']
del lis[0]
print(lis)

print("\n원소 변경")
lis = ['ㅁ', 'ㄴ', 'ㅇ']
lis[0] = "마"
print("마 lis : ", lis)
lis[1:3] = ["나", "아"]
print("ㅏ lis : ", lis)

print("\njoin()")
lis = ['ㅁ', 'ㄴ', 'ㅇ']
print("joined ㅗ : ", "ㅗ".join(lis))

print("\nin")
lis = ['ㅁ', 'ㄴ', 'ㅇ']
if "ㅎ" in lis:
    print("'ㅎ' is in lis")
if "ㅅ" not in lis:
    print("'ㅅ' is not in lis")
```

    len()
    len of 'bang' :  4
    len of '['ㅁ', 'ㄴ', 'ㅇ']' :  3
    
    del
    ['ㄴ', 'ㅇ']
    
    원소 변경
    마 lis :  ['마', 'ㄴ', 'ㅇ']
    ㅏ lis :  ['마', '나', '아']
    
    join()
    joined ㅗ :  ㅁㅗㄴㅗㅇ
    
    in
    'ㅅ' is not in lis
    

### 1.4 리스트 내장 함수


```python
print("sort, remove, insert, pop, append, reverse")
food = ["치킨", "샐러드", "카레", "비빔밥", "짜장면"]
food.sort()
print("sort food : ", food)

food.remove("짜장면")
print("remove 짜장면 food : ", food)

food.insert(1, "짬뽕")
print("insert 짬뽕 food : ", food)

print("pop 짬뽕 food : ", food.pop(1))
print("food : ", food)

del food[0]
print("del 비빔밥 food : ", food)

food.append("상추")
print("append 상추 food : ", food)

food.reverse()
print("reverse food : ", food)
```

    sort, remove, insert, pop, append, reverse
    sort food :  ['비빔밥', '샐러드', '짜장면', '치킨', '카레']
    remove 짜장면 food :  ['비빔밥', '샐러드', '치킨', '카레']
    insert 짬뽕 food :  ['비빔밥', '짬뽕', '샐러드', '치킨', '카레']
    pop 짬뽕 food :  짬뽕
    food :  ['비빔밥', '샐러드', '치킨', '카레']
    del 비빔밥 food :  ['샐러드', '치킨', '카레']
    append 상추 food :  ['샐러드', '치킨', '카레', '상추']
    reverse food :  ['상추', '카레', '치킨', '샐러드']
    

### 1.5 반복문(for)과 리스트


```python
c_lass = ["캡", "독일", "시프", "빅데", "디지털"]
print("my c_lass")
c_lass = iter(c_lass)
try:
    print("1번 : ", next(c_lass))
    print("2번 : ", next(c_lass))
    print("3번 : ", next(c_lass))
    print("4번 : ", next(c_lass))
    print("5번 : ", next(c_lass))
    print("6번 : ", next(c_lass))
except StopIteration:
    print("error: iterator finished")
```

    my c_lass
    1번 :  캡
    2번 :  독일
    3번 :  시프
    4번 :  빅데
    5번 :  디지털
    error: iterator finished
    


```python
print("square num")
num = [1.1, 2.4, 4.2, 4.5]
for n in num:
    print(f"square of {n} = {n**2}")
```

    square num
    square of 1.1 = 1.2100000000000002
    square of 2.4 = 5.76
    square of 4.2 = 17.64
    square of 4.5 = 20.25
    

## 2. Dictionary


```python
kim = {"name" : "KIM", "age" : 44, "height" : 145.1}
lee = {"name" : "LEE", "age" : 84, "height" : 163.1}
print("dictionary")
print("kim's age is ", kim["age"])
print("Lee's height is ", lee["height"])
```

    dictionary
    kim's age is  44
    Lee's height is  163.1
    


```python
print("hash ex")
print("hash 2 : ", hash(2))
print("hash oOo : ", hash('oOo'))
try:
    print("hash of []:", hash([]))
except TypeError as te:
    print("[TypeError]", te)
```

    hash ex
    hash 2 :  2
    hash oOo :  5054959937618835319
    [TypeError] unhashable type: 'list'
    

### 2.1 기본 사용법


```python
kim = {"name" : "KIM", "age" : 44, "height" : 145.1}
lee = {"name" : "LEE", "age" : 84, "height" : 163.1}
print("kim's height is ", kim["height"])
kim["height"] = 186.3
print("kim's height is ", kim["height"])
kim["hair"] = "long"
print("kim : ", kim)
del kim["hair"]
print("kim : ", kim)
```

    kim's height is  145.1
    kim's height is  186.3
    kim :  {'name': 'KIM', 'age': 44, 'height': 186.3, 'hair': 'long'}
    kim :  {'name': 'KIM', 'age': 44, 'height': 186.3}
    


```python
lee = {"name" : "LEE", "age" : 84, "height" : 163.1}
try:
    print("\ntry non-existing key")
    print("lee's voice?", lee["voice"])
except KeyError as ke:
    print("[KeyError]", ke)

print("lee's voice?", lee.get("voice"))
if "voice" in lee:
    print("lee's voice is", lee["voice"])
else:
    print("lee has no voice")
```

    
    try non-existing key
    [KeyError] 'voice'
    lee's voice? None
    lee has no voice
    

### 2.2 관련 함수


```python
print("functions")
scores = {"수학": 30, "영어": 55, "국어": 99, "사회": 85}
print("과목 : ", scores.keys())
print("점수 : ", scores.values())
print("items : ", scores.items())

print("과목 : ", list(scores.keys()))
print("점수 : ", list(scores.values()))
print("items : ", list(scores.items()))
```

    functions
    과목 :  dict_keys(['수학', '영어', '국어', '사회'])
    점수 :  dict_values([30, 55, 99, 85])
    items :  dict_items([('수학', 30), ('영어', 55), ('국어', 99), ('사회', 85)])
    과목 :  ['수학', '영어', '국어', '사회']
    점수 :  [30, 55, 99, 85]
    items :  [('수학', 30), ('영어', 55), ('국어', 99), ('사회', 85)]
    

### 2.3 lteration


```python
test = {"수학": 130, "영어": 55, "국어": 99, "사회": 85}
for name in test:
    print("name:", name, "->", test[name])

for name in test.keys():
    print("name:", name, "=>", test[name])

print("\niterate over value")
for score in test.values():
    print("score:", score)
    
print("\niterate over keys and values")
for name, score in test.items():
    print("name:score:", name, ":", score)
```

    name: 수학 -> 130
    name: 영어 -> 55
    name: 국어 -> 99
    name: 사회 -> 85
    name: 수학 => 130
    name: 영어 => 55
    name: 국어 => 99
    name: 사회 => 85
    
    iterate over value
    score: 130
    score: 55
    score: 99
    score: 85
    
    iterate over keys and values
    name:score: 수학 : 130
    name:score: 영어 : 55
    name:score: 국어 : 99
    name:score: 사회 : 85
    


```python
print("\nTuple")
tuple1 = ()
tuple2 = tuple()
tuple3 = ("Hello", 1234, 1.234, True)
tuple4 = "Hello", 1234, 1.234, True
tuple5 = ("Hello", 1234, (1.234, True))
print("tuple1", tuple3[0])
print("tuple1", tuple3[1:])
print("tuple2", tuple4[1])
print("tuple3", tuple5[2][0])

print("\ndistribute values")
s = "jin", "long", 33.3, 40
name, hair, age, weight = s
print("tupled s info:", name, hair, age, weight)
```

    
    Tuple
    tuple1 Hello
    tuple1 (1234, 1.234, True)
    tuple2 1234
    tuple3 1.234
    
    distribute values
    tupled s info: jin long 33.3 40
    

## 4. Set


```python
print("Set")
cos = ["립", "부드러운칫솔", "린스", "휴지", "수간"]
basic_cos = set(cos)
print("cos set:", cos)
```

    Set
    cos set: ['립', '부드러운칫솔', '린스', '휴지', '수간']
    


```python
print("\nset example")
color = {"빨강", "핑크", "보라", "흰색"}
rainbow = {"빨강", "주황", "노랑"}
print("set & : ", color & rainbow)
print("set & interaction ", color.intersection(rainbow))
print("set & | ", color | rainbow)
print("set union : ", color.union(rainbow))
print("set - : ", color - rainbow)
print("set difference : ", color.difference(rainbow))
```

    
    set example
    set & :  {'빨강'}
    set & interaction  {'빨강'}
    set & |  {'핑크', '노랑', '보라', '주황', '빨강', '흰색'}
    set union :  {'핑크', '노랑', '보라', '주황', '빨강', '흰색'}
    set - :  {'핑크', '보라', '흰색'}
    set difference :  {'핑크', '보라', '흰색'}
    

# 2. 연습문제

## 2.1Number and String in Python


### 2.1.1위 연산을 이용해서 13의 3승을 16진수로 표현하시오


```python
a = 13
print(a**3) #2197
print(13**3)

print(hex(a**3)) #0x895
```

    2197
    2197
    0x895
    

### 2.1.2 대리암


```python
marble = \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "그간 많은 stress 견뎌내며 비로소 대리암이 되었다네\n" \
    "모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야\n" \
    "모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나를 보고 웃기라도 하는 날엔 하루 종일 아무것도 할 수 없네\n" \
    "그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "이것이 염산반응이다\n" \
    "이것이 염산반응이다\n" \
    "Hcl이다 CaCO3다\n" \
    "2Hcl + CaCO3 -> CaCl2 +CO2 + H2O다.\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 나는 대리암"
```


```python
# 1)
a = "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n"

print(a * 2 + "그간 많은 stress 견뎌내며 비로소 대리암이 되었다네\n" + "모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야\n" * 2 + a * 2 + "그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야\n" + a * 4 + "이것이 염산반응이다\n" * 2 + "Hcl이다 CaCO3다\n" + "Hcl이다 CaCO3다\n" + a * 2 + "나는 대리암 나는 대리암")
```

    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    그간 많은 stress 견뎌내며 비로소 대리암이 되었다네
    모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야
    모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    이것이 염산반응이다
    이것이 염산반응이다
    Hcl이다 CaCO3다
    Hcl이다 CaCO3다
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암
    나는 대리암 나는 대리암
    


```python
# 2)
print("count '대리암' : ", marble.count('대리암'))

pyind = marble.find("대리암")
pyind = marble.find("대리암", pyind+1)
pyind = marble.find("대리암", pyind+1)
print("find 3 '대리암'  : ", pyind)
```

    count '대리암' :  23
    find 3 '대리암'  :  36
    


```python
# 3)
print(marble.replace("대리암", "석회암"))
```

    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    그간 많은 stress 견뎌내며 비로소 석회암이 되었다네
    모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야
    모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나를 보고 웃기라도 하는 날엔 하루 종일 아무것도 할 수 없네
    그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    이것이 염산반응이다
    이것이 염산반응이다
    Hcl이다 CaCO3다
    2Hcl + CaCO3 -> CaCl2 +CO2 + H2O다.
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 염산과 반응하면 이산화탄소를 내며 녹는 석회암
    나는 석회암 나는 석회암
    

## 2.2 Data Structure 1: List

### 2.2.1 depth2_list에서 [1.234]를 출력해 보세요. (주의: 1.234가 아닌 [1.234] 입니다.)


```python
depth2_list = ["Hello", 1234, [1.234, True]]
print(depth2_list[2][:1])
```

    [1.234]
    

### 2.2.2 wdgirls_debut에서 멤버를 삭제, 추가하여 wdgirls_final을 만들어 보세요.


```python
#wdgirls_final = ["예은", "선미", "유빈", "혜림"]
wdgirls_debut = ["선예", "예은", "소희", "현아", "선미"]

wdgirls_debut.pop(0)
wdgirls_debut.pop(1)
wdgirls_debut.remove("현아")

wdgirls_debut.append("유빈")
wdgirls_debut.insert(3, "혜림")
print(wdgirls_debut)
```

    ['예은', '선미', '유빈', '혜림']
    
