# 22년 03월 29일 화요일

# Class and File IO

## Python Class

### 1. 클래스 사용법

```python
class Dog:
    def __init__(self, name): #__init__ : 생성자 함수. return 불가능.
        self.name = name	#self는 c++에서 this. 반드시 self 붙여야 한다. self말고 다른 이름 써도 괜찮긴하다.
        self.position = 0 
        #멤버 변수 init 함수 내에서만 생성해주는 것이 좋다.

    def bark(self):
        print(f"{self.name}: Wal! Wal!")

    def move(self, distance):
        self.position += distance
        print(f"{self.name} is at {self.position}")

def main():
    puppy = Dog("dangdang")
    puppy.bark()	
    puppy.move(10)	
    print("current position:", puppy.position)

if __name__ == "__main__":
    main()
```



### 2. 상속과 다형성

- 상속 inheritance : 클래스 사이에 부모와 자식 혹은 상위와 하위 관계가 있어서 자식 클래스는 부모 클래스 함수와 변수를 물려받는다.
- 다형성 polymorphism : 형태는 같은데 다른 일을 하는 함수가 여러개 있을 수 있다는 것이다. 상속을 통해 부모 클래스에서 받은 메소드들을 오버라이딩(overriding :  다형성을 구현하는 문법. 재정의)을 통해서 바꿔쓸 수 있다.
  - 코드 절약, 기능을 한 곳으로 응집시켜서 버그를 줄이고 변화에 강인한 코드를 만든다.

```python
#함수 사이 1칸 클래스 사이 2칸 클래스 내부 함수 사이 1칸 밖 함수는 2칸 뛰어잇

class Animal:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print("my name is", self.name)
        
    def sound(self):
        print("...")
        
        
class Cow(Animal): #상속. 파이썬은 접근지정자가 없다.
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        print("ummer~~~")
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        print("nyaong~~")

def main():
    cow = Cow("cow1")
    cow.introduce()
    cow.sound()
    animals = [Animal("ani"), Cow("cow2"), Cat("cat")]
    for i, ani in enumerate(animals):
        print("index : ", i)
        ani.introduce()
        ani.sound()

if __name__ == "__main__":
    main()
```



## 파일 입출력

```python
fout = open("testfile.txt", "w")
fout.write("I think.")
fout.close()
# print("file was written")

fin = open("testfile.txt", "r")
contents = fin.read()
fin.close()
print(contents)
```



### 1. 파일 열기

- open()

``` python
try:
    f = open("nofile.txt", "r")
except FileNotFoundError as fe:
    print(fe)
```

- 파일을 열 때 위 예시처럼 `fp = open(filename, mode)` 이렇게 열어도 되지만 이 경우 반드시 `fp.close()`를 실행해야 한다.
- 깜빡하기 쉬운데 이렇게 열고 닫아야 하는 코드가 있을 경우 파이썬에서는 **context manager**라는 기능을 쓴다.

```python
fr = open("testfile.txt", "r")
fr.read()
fr.close()

with open("testfile.txt", "r") as fr:
    data = fr.read()
    print("check closed : ", fr.closed)

print("outside context manager")
# data = fr.read() #파일 이미 닫쳐서 이 문자 쓰면 에러난다.
print("check closed : ", fr.closed)


class File:
    def __enter__(self):
        pass

    def __excit__(self, exc_type, exc_val, exc_tb):
        pass
```

- with open으로 객체 열고 닫지 않으면 자동으로 파일 닫기가 된다.



### 2. 파일 쓰기

```python
springx3 = ["봄 봄 봄 봄이 왔네요",
            "우리가 처음 만났던 그때의 향기 그대로",
            "그대가 앉아 있었던 그 벤치 옆에 나무도 아직도 남아있네요",
            "살아가다 보면 잊혀질 거라 했지만",
            "그 말을 하면 안될거란걸 알고 있었소",
            "그대여 너를 처음 본 순간 나는 바로 알았지",
            "그대여 나와 함께 해주오 이 봄이 가기 전에"]

print("\nwrite lyrics into file")
with open("springx3.txt", "w") as f:
    for i, line in enumerate(springx3):
        f.write(f"{i:2}:" + line + "\n")
```



### 3. 파일 읽기

- read(size=-1)
- readline()
- readlines()

```python
#springx3.txt 위치 바꾸고 싶다.
print("use read")
with open("springx3.txt", "r") as f:
    lyrics = f.read()
    print(lyrics)

print("use readline")
with open("springx3.txt", "r") as f:
    lyrics = []
    line = f.readline()
    while line:
        line = line.rstrip("\n")
        lyrics.append(line)
        line = f.readline()
print("\n".join(lyrics))

print("use readlines")
with open("springx3.txt", "r") as f:
    lyrics = f.readlines()
    lyrics = [line.rstrip("\n") for line in lyrics]
    print("\n".join(lyrics))
```



### 연습문제

다음 코드에서 `matrix_str`은 2x2 행렬을 나타내는 문자열이다. 이를 파일로 출력 후 다시 파일을 읽어서 2중 리스트에 저장한 후 행렬의 determinant를 구하시오. 파일을 읽고 쓸때 `with` 키워드를 이용하시오.

```python
matrix_str = "4 2\n5 3"
# matrix.txt 에 저장

# 파일 읽어서 matrix에 2중 리스트로 저장

print("read matrix:", matrix)
# => read matrix: [[4, 2], [5, 3]]
# determinant 계산
```

```python
#교수님
with open("matrix.txt", "r") as f:
    data = f.readlines()

data = [d.rstrip("\n") for d in data]
data = [d.split() for d in data]

data = [[int(elem) for elem in row] for row in data]
# ↓↓
# numdata = []
# for row in data:
#     numrow = [int(elem) for elem in row]
#     numdata.append(numrow)

print(data)

determinant = data[0][0] * data[1][1] - data[0][1] * data[1][0]
    
print("determinant : ", determinant)
```

~~~python
# 나...
# with open("matrix.txt", "w") as fw:
#     matrix_str = "4 2\n5 3"

# matrix = []

# with open("matrix.txt", "w") as f:
#     for i, line in enumerate(matrix_str):
#         print(i, line)
#         matrix = matrix_str.split(" ")

# # matrix[[4, 2], [5, 3]]
# #      0,0  0,1  1,0   1,1

# # print("read matrix : ", matrix)



# matrix_str = "4 2\n5 3"
# with open("matrix.txt", "w") as f:
#     f.write(matrix_str)
~~~



# Module and Package



## 1. 모듈과 패키지는 무엇인가?

- 모듈 Module : 각각의 파이썬 파일
- 패키지 Package : 여러 모듈을 묶은 폴더



## 2. 모듈 만들기

```python
import list_ops

foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]
print(f"{foo} + {bar} = {list_ops.add(foo, bar)}")

print(f"ham : {list_ops.ham}")
# print(f"eggs : {list_ops.eggs}") #에러
print(f"{list_ops.ham} * {list_ops.ham} =" f"{list_ops.multiply(list_ops.ham, list_ops.spam)}")
```



~~~python
#모듈 이름 짧게 변경
import list_ops as lo

foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]

goo = lo.subtract(foo, bar)
print(f"{foo} - {bar} = {goo}")
~~~



~~~python
from list_ops import add, subtract, spam

foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]

goo = add(foo, bar)
print("{} + {} = {}".format(foo, bar, goo))
goo = subtract(bar, foo)
print("{} - {} = {}".format(bar, foo, goo))
print("spam = {}".format(spam))
~~~



