# 22년 03월 15일 화요일

## 1. List []

 ```python
 #비어있는 리스트 
 empty_list1 = []
 empty_list2 = list()
 #채워져있는 리스트
 basic_list = ["Hello", 1234, 1.234, True]
 depth2_list = ["Hello", 1234, [1.234, True]] #3개의 원소. 3번째 원소가 하나의 리스트
 depth3_list = [["Hello"], [1234, [1.234, True]]] #2개의 원소. 2->2->2 원소
 ```



### 1.1 리스트 인덱싱 슬라이싱

```python
# print(basic_list[2])
# print(basic_list[-2])

# print(depth2_list[2])
# print(depth2_list[2][0])

# print(depth3_list[1])
# print(depth3_list[1][1])
# print(depth3_list[1][1][0])

print(basic_list[1:3]) #리스트로 출력
print(basic_list[:3])

#겹치는 구간만 꺼내고 아예 안 겹치면 그냥 빈 리스트 나온다.
print(basic_list[2:10]) 
print(basic_list[4:10])

#인덱싱은 범위 벗어나면 에러 슬라이싱은 빈 리스트 나온다.

#연습문제
#depth2_list에서 [1.234]를 출력해 보세요. (주의: 1.234가 아닌 [1.234] 입니다.)
print(depth2_list[2][:1])
```



### 1.2 리스트 연산

```python
mammal = ["dog", "cat", "human"]
reptile = ["snake", "lizard", "frog"]
bird = ["eagle", "sparrow", "chicken"]
animal = mammal + reptile + bird
print(animal)

members = ["나연", "정연", "지효"]
tests = ["vocl", "dance", "rap"]
first_row = members[0:1] * 3 + members[1:2]*3 + members[2:3]*3
second_row  = tests * 3
print(first_row)
print(second_row)
```



### 1.3 리스트 관련 함수

```python
#len
string = "system programming"
print(len(string))
mylist = [1,3,5,6,7,10]
print(len(mylist))

#del
del string

mylist = [1,2,3,4,5]
del mylist[2]
print(mylist)

#replace
mylist = [1,2,3,4,5]
mylist[0] = "Life"
print(mylist)
mylist[1:4] = ["is", "too", "short"]
print(mylist)

mylist = [1,2,3,4,5]
mylist[1:4] = ["is", "too"] 
print(mylist) # >> [1, 'is', 'too', 5]

mylist = [1,2,3,4,5]
mylist[1:4] = ["is", "too", "too", "too", "too"] 
print(mylist) # >> [1, 'is', 'too', 'too', 'too', 'too', 5]

#join
#문자열의 함수
path = ["/home", "ian", "work", "ian-lecture"]
print("/".join(path))
time = ["13", "20", "30"]
print(":".join(time))

#in
twice = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
if "채영" in twice:
    print("채영은 트와이스 입니다.")
if "채령" not in twice:
    print("채령 is not twice")
```



### 리스트 내장 함수

- 대부분의 함수들이 in-place 함수다.

  - 리턴 결과가 없고 그냥 수정해주고 끝난다. 결과는 다 들어있다.

  - ```
    tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
    print("sort", tottenham.sort())
    print("sort result", tottenham)
    ```

```python
tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
tottenham.sort()
print("line up", tottenham)
tottenham.remove("Moura") #remove
print("remove moura", tottenham)
tottenham.insert(1, "Son")
print("Son in", tottenham)

#pop : 입력이 없으면 마지막 원소를 삭제.
print("pop Alli", tottenham.pop(0))
print("pop Alli : ", tottenham)
del tottenham[3]
print("del rose : ", tottenham)

#append : 맨 뒤에 추가
tottenham.append('Davies')
tottenham.append('Llorente')
print("append", tottenham)

#reverse : 순서를 거꾸로 뒤집는다. in-place 함수
tottenham.reverse()
print("reverse : ", tottenham)
```

```python
#연습문제
#wdgrls_debut 에서 wdgirls_final로 바꾸기.
#wdgirls_final = ["예은", "선미", "유빈", "혜림"]
wdgirls_debut = ["선예", "예은", "소희", "현아", "선미"]

wdgirls_debut.pop(0)
wdgirls_debut.pop(1)
wdgirls_debut.remove("현아")

wdgirls_debut.append("유빈")
wdgirls_debut.insert(3, "혜림")
print(wdgirls_debut)
```



### 1.5 반복문(for)과 리스트

```python
tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
for member in tottenham:
    print("member : ", member)
    print("initial : ", member[0])
```

- `list, dict, tuple, set` 모두 여러 원소를 담고 있는 iterable 객체이기 때문에 `for`문을 통해서 리스트의 원소들을 하나씩 처리할 수 있다.

```python
tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
print("type : ", type(tottenham))
tottenham = iter(tottenham)
print("type : ", type(tottenham))
#iter 면 next 쓸 수 있다.
print("0", next(tottenham))
print("1", next(tottenham))
print("2", next(tottenham))
```

```
numbers = [1,2,3,4,5]
for a in numbers:
    print(f"square of {a} = {a**2}")
```



## 2. Dictionary {}

```python
pooh = {"species" : "bear", "age" : 5, "weight" : 50}
tigger = {"species" : "tiger", "age" : 4, "weight" : 40}
print("pooh's species is ", pooh["species"])
print("pooh's weight is ", pooh["weight"])
print("tiger's age is ", tigger["age"])
```

- value에는 어떤 객체가 들어가도 상관 없다.

- key는 숫자나 문자열 (혹은 그 변수)을 써야 한다.

- hash() 함수를 통해 key 사용 가능 값 알 수 있다.

  - ```python
    print(hash(1))
    print(hash("hello"))
    print(hash(1.1))
    
    try:
        print(hash([1]))
    except TypeError as te;
    	print(te)
    ```



### 2.1 기본 사용법

- 딕셔너리의 기본 특징은 순서가 없다.(Unordered)

```python
pooh = {"species": "bear", "age": 5, "weight": 50}
print("pooh's age", pooh["age"])
pooh["age"] = 10
print("pooh's age", pooh["age"])
pooh["height"] = 1.2
print(pooh)
del pooh["weight"]
print(pooh)

print(pooh["ace"]) #없는거 쓰면 에러



pooh = {"species": "bear", "age": 5, "weight": 50}

try: 
    print("pooh's color", pooh["color"])
except KeyError as ke:
    print("key error", ke)

if "color" in pooh:
    print("pooh's color", pooh["color"])
else:
    print("pooh has no color")
```



### 2.2 관련 함수

```python
scores = {"pooh": 80, "tigger": 70, "piglet": 90, "rabbit": 85}
print("names:", scores.keys())
print("scores:", scores.values())
print("items:", scores.items())

print("names:", list(scores.keys()))
print("scores:", list(scores.values()))
print("items:", list(scores.items()))
```



### 2.3 Iteration

```python
scores = {"pooh": 80, "tigger": 70, "piglet": 90, "rabbit": 85}

for name in scores:
    print("name : ", name, "value : ", scores[name])

for val in scores.keys():
    print("name : ", val)

for val in scores.values():
    print("score : ", val)

for val in scores.items():
    print("name:score : ", val)

for name, score in scores.items():
    print("name:score : ", name, ":", score)
```



## 3. Tuple ()

- `()`를 생략해도 된다. 튜플은 생성만 할 뿐 원소를 수정하거나 삭제할 수 없다.
- 성된 튜플에서는 값을 읽을 수만 있는데 리스트와 동일하게 인덱싱과 슬라이싱을 통해 읽을 수 있다.

```python
basic_tuple1 = ("Hello", 1234, 1.234, True)
basic_tuple2 = "Hello", 1234, 1.234, True
depth2_tuple = ("Hello", 1234, (1.234, True))

print(basic_tuple1[0])
print(basic_tuple1[2:])
```

```
pooh = "pooh", "bear", 5, 50
name, species, age, weight = pooh
print("tupled pooh info:", name, species, age, weight)	
```



## 4. Set

- 집합(set) 자료 구조는 중복을 허용하지 않는다. 어떤 리스트나 튜플에 중복된 자료가 있을 때 이를 집합으로 변환하면 중복을 없애고 유일한 자료만 남길 수 있다.

```python
entrance_order = ["k3", "aventador", "k3", "a6", "cayenne", "a6"]
car_set = set(entrance_order)
print("car set:", car_set)
```

```python
entrance_order = ["k3", "aventador", "k3", "a6", "cayenne", "a6"]
car_set = set(entrance_order)
print("car set : ", car_set)
car_list = list(car_set)
print("car list : ", car_list)
print(car_list[2:])
```

```python
large_comps = {"samsung", "hyundai", "lg", "sk"}
motor_comps = {"hyundai", "kia", "gm"}

print("intersection : ", large_comps & motor_comps)
print("intersection : ", large_comps.intersection(motor_comps))

print("union : ", large_comps | motor_comps)
print("union : ", large_comps.union(motor_comps))

print("diff : ", large_comps - motor_comps)
print("diff : ", large_comps.difference(motor_comps))
```





# if, for and while



## 1. Basic Usages

```python
if condition1:
	statements_when_condition1_is_true
elif condition2:
	statements_when_condition2_is_true
else:
	statements_when_no_condition_is_true

for elem in something_iterable:
	statements_to_process_elem

while condition:
	statements_while_condition_is_true
```



```python
marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

myhero = "batman"
if myhero in marvel_heroes:
    print("batman in marver")
elif myhero in dc_heroes:
    print("batman in dc")
else:
    print("villlain")

for hero in marvel_heroes:
    print("marvel : ", hero)

i=0
while i < len(dc_heroes) and dc_heroes[i].endswith('man'):
    print(f"     {dc_heroes[i]}")
    i+=1
```

























































































































