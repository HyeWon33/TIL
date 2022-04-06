# 22년 03월 22일 화요일

# Control statements: if, for and while

## 1. Basic Usages



## 2. 반복문 제어 (continue, break)

- 반복문을 돌리다 보면 조건에 따라 중간에 처리를 건너뛰고 싶거나 그만두고 반복문을 종료하고 싶을 때가 있다. continue는 반복문에서 continue 이후의 과정을 건너뛰고 다음 loop로 넘어가는 것이고 break는 반복문 자체를 끝낸다.

```python
marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

for hero in marvel_heroes:
    if hero.startswith("spider"):
        print("  Peter Parker ... ")
        continue
    if hero.startswith("capt"):
        print(" One Captain is enough ... ")
        break
    print(f"  {hero} is cool")
    
name = None
print("Press 'q' to quit")
while name != 'q':
    print("type dc hero's name")
    name = input()
    if name == 'q':
        break
    if name not in dc_heroes:
        print(f"{name} is not dc hero")
        continue
    index = dc_heroes.index(name)
    print(f"{name}'s index = ", index)
```



## 3. for 응용 (enumerate, zip)

- enumerate : for 문에서 리스트를 반복할 시 원소 뿐만 아니라 인덱스도 받을 수 있는 객체를 만들어 준다.
- zip : 두 개의 리스트를 묶어서 각 리스트의 원소가 하니씩 합쳐진 튜플의 반복 객체를 만들어준다.

```python
marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

print(list(enumerate(marvel_heroes)))

# for elen in enumerate(marvel_heroes):
#     i, name = elen
#     print(i, name)

for i, name in enumerate(marvel_heroes):
    print(i, name)

print(list(zip(marvel_heroes, dc_heroes)))
# [('iron man', 'batman'), ('thor', 'superman'), ('hulk', 'aquaman'), ('spider man', 'wonder woman'), ('black widow', 'harley quinn')]

for marvel, dc in zip(marvel_heroes, dc_heroes):
    print(marvel, dc)

for index, name in enumerate(marvel_heroes):
    if index >= 3:
        break
    print("marvel hero : ", index, name)

for mv, dc in zip(marvel_heroes, dc_heroes):
    print(f"{mv} vs {dc}")

print(list(enumerate(zip(marvel_heroes, dc_heroes))))
#구조화된 튜플로 받아야 사용 가능
for ind, (mv, dc) in enumerate(zip(marvel_heroes, dc_heroes)):
    if ind >= 3:
        break
    if ind%2 == 1:
        print(f"{mv} vs {dc} : {mv} win!")
    else:
        print(f"{mv} vs {dc} : {dc} win!")
```



## 4. List Comprehension

- 파이썬에는 리스트를 선언하는 `[]` 안에 `for`문을 넣어 저 두 개의 `for`문을 한 줄로 처리하는 방법이 있는데 이를 `list comprehesion`이라고 한다.

```python
marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

super_heros = []
for hero in marvel_heroes:
    super_heros.append(hero + "_super")
print("super heroes", super_heros)

#man으로 끝나는거 모은다.
man_heros = []
for hero in marvel_heroes:
    if hero.endswith("man"):
        man_heros.append(hero)
print("man heroes", man_heros)
#너무 길어. 한 줄로 줄이는게 list comprehension

super_heros_v2 = [hero + "_super " for hero in marvel_heroes]
#대괄호로 리스트 만드는데 원소들 하나씩 안 써주고 for문으로 넣는다.
#hero + "_super " <= 새로운 원소 들어가는거...?
print("super horoes", super_heros_v2)


man_heros_v2 = [hero for hero in marvel_heroes if hero.endswith("man")]
print("man heroes v2 : ", man_heros_v2)

int_square = [i**2 for i in range(10)]
print(int_square)
```

```python
marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
abilities = ["suit", "Mjölnir", "physical power", "spider web"]

heroes = {name: power for nmae, power in zip(marvel_heroes)}
print("heroes abbility : ", heroes)

heroes_v2 = dict(zip(marvel_heroes, abilities))
print("heroes abilities v2 : ", heroes_v2)
```



# Function

## 1.함수 정의

- 선언과 정의 나누지 않고 바로 정의만하면 된다.
- 다중 입력과 다중 출력을 지원하고 입력이나 출력이 없을 수도 있다.
- 동적타입이라 타입 안 적고 입력 인자 이름만 적어도 괜찮다.

```python
def add(n1, n2):
    return n1+n2

print(add(10, 20))
print(add(3, 7))
```

```python
def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind + start not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

    return average

data = list(range(10))
print(average_list(data, 1, 8, [5], True))
```



## 2. Keyword Arguments

- 이렇게 입력하는 인자를 keyword argument (키워드 인자)라 한다. 반면 기존 방식대로 순서에 의해 할당되는 입력 인자를 positional argument (위치 인자)라 한다.

- ```python
  avg = average_list(data, 2, 7, skip=[4], verbose=True)
  avg = average_list(data=data, start=2, end=7, skip=[4], verbose=True)
  avg = average_list(data, start=2, 7, [4]) #에러
  ```

- 키워드 인자는 반드시 위치 인자 뒤에 나와야 한다

- 키워드 인자 끼리는 순서를 섞어도 된다.

  - `avg = average_list(data, end=7, start=2, skip=[4], verbose=True)`



## 3. 인자 기본값 지정

```python
def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind + start not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

    return average

def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)

data = list(range(10))
avg = average_list_with_default(data)
avg = average_list_with_default(data, 5)
avg = average_list_with_default(data, end = 5)
avg = average_list_with_default(data, skip=[3, 4])
```



연습문제

- 두 개의 숫자 리스트를 입력인자로 받아 원소별로 합산한 리스트를 출력하는 함수를 구현하시오. 함수는 다음과 같은 입력인자를 가져야 한다. 함수를 구현 후 이를 다양하게 사용해보시오.
  - `list1, list2`: 두 개의 리스트 입력인자는 필수 입력인자로 받음, 기본값이 없는 필수 인자
  - `shortlen`: True이면 두 리스트 중 짧은 쪽에 출력 길이를 맞춤, False이면 두 리스트 중 긴 쪽에 출력 길이를 맞춤 (e.g. [2, 3, 4] + [1, 2, 3, 4, 5] = [3, 5, 7, 4, 5]), 기본값은 True
  - `start`: 지정하면 두 리스트에서 `start` 인덱스부터 더함, 기본값은 0
  - `verbose`: True이면 계산 결과를 함수 내부에서 프린트함, 기본값은 False

- *zip 리스트가 짧은 쪽에 맞춰진다.*

```python
def sum_list(list1k list2, shortlen, start=0, verbose=True):
    list1 = list1[start:]
    list2 = list2[start:]
    if shortlen is False:
        # if len(list1)

        short = list1 if len(list1) < len(list2) else list2
        longl = list2 if len(list1) < len(list2) else list1
        for i in range(len(longl) - len(short)):
            short.append(0)
        sum_result = [s+l for s, l in zip(short, longl)]
    else:
        sum_result = [s+l for s, l in zip(list1, list2)]
    if verbose:
        print(f"{list1} * {list2} = {sum_result}")
    return sum_result

sum_list([1,2,3], [2,3,4,5,6], True)
sum_list([1,2,3,], [2,3,4,5,6], False)
```



## 4. 변경 가능한 입력인자 개수

### 4.1 *args

- C++ 같은 경우 모든 가능한 경우의 입력인자 개수만큼 함수 선언을 따로 해줘야 하지만 파이썬에서는 `*args`라는 입력인자 하나로 여러개의 입력인자를 받을 수 있다. 
- `rgs`라는 이름은 관습적으로 많이 쓰이는 것이고 `*input`처럼 다른 이름으로 바꿀수 있고 앞에 `*`만 붙이면 된다.
- `*args`는 반드시 마지막 입력인자로 들어가야한다.

```python
subject_scores = {"cpp": [57, 36, 80], "java": [46, 88, 72], "ruby": [85, 23, 34]}

def average_multi_subjects(scores, *args):
    averages = {}
    print("args", args) #튜플이 프린트
    print("*args", *args) #언팩. 튜플로 묶여있는 것을 여러 개로 풀어헤치는 것.

result = average_multi_subjects(subject_scores, "cpp")
result = average_multi_subjects(subject_scores, "cpp", "java", "ruby")
```

```python
subject_scores = {"cpp": [57, 36, 80], "java": [46, 88, 72], "ruby": [85, 23, 34]}

def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind + start not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

    return average

def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)
def average_multi_subjects(scores, *args):
    averages = {}
    print("args", args) 
    print("*args", *args) 
    for subject in args:
        avg = average_list_with_default(scores[subject])
        avg = average_list_with_default(scores[subject], verbose=False)
        print(f"average over {subject} scores: {avg:.1f}")
        averages[subject] = avg
    return averages

result = average_multi_subjects(subject_scores, "cpp")
print("result : ", result)
result = average_multi_subjects(subject_scores, "cpp", "java", "ruby")
print("result : ", result)
```

```python
def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind + start not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")
    return average
def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)
def average_multi_subjects(scores, *args):
    averages = {}
    print("args", args) 
    print("*args", *args) 
    for subject in args:
        avg = average_list_with_default(scores[subject])
        avg = average_list_with_default(scores[subject], verbose=False)
        print(f"average over {subject} scores: {avg:.1f}")
        averages[subject] = avg
    return averages

def average_variable_arguments(data, multiple, *args):
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, *args)
    return avg

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = average_variable_arguments(data, 10, 1, 7)
print("average_variable_arguments(data, 10, 1, 7) =>", result)
result = average_variable_arguments(data, 10, 1, 7, [3], False)
print("average_variable_arguments(data, 10, 1, 7, [3], True) =>", result)
result = average_list_with_default(data, 1, 7)
print("average_list_with_default(data, 1, 7) =>", result)
result = average_list_with_default(data, 1, 7, [3], False)
print("average_list_with_default(data, 1, 7, [3], True) =>", result)
```





...





### 4.2 **kwargs

```python
def average_list(data, start, end, skip, verbose):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    for ind, num in enumerate(avg_data):
        if ind + start not in skip:
            sum += num
    dlen = len(avg_data) - len(skip)
    average = sum / dlen
    if verbose:
        print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")
    return average
def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)


# def average_keyworded_args(data, multiple, **kwargs):
#     print("kwargs", kwargs)
#     # print("**kwargs", **kwargs)
#     data = [d*multiple for d in data]
#     avg = average_list_with_default(data, **kwargs)
#     return avg

# data = [1,2,3,4,5,6,7,8,9]
# result = average_keyworded_args(data, 10, start=1, skip=[2, 3], verbose=True)

def average_keyworded_args(data, multiple, *args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, *args, **kwargs)
    return avg

data = [1,2,3,4,5,6,7,8,9]
result = average_keyworded_args(data, 10, 1, skip=[2, 3])
```



## 5. 변수 범위(Scope)





## 6. 바람직한 파이썬 코딩 스타일









