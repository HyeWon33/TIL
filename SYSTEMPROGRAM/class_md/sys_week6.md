# 22년 04월 05일 화요일

## Module and Package

### 3. 패키지 만들기

```python
#dict_ops.py
def add(foo, bar):
    out = {}
    for key in foo:
        out[key] = foo[key] + bar[key]
    return out

def subtract(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] - bar[key]
    return out

def multiply(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] * bar[key]
    return out

def divide(foo, bar):
    out = {}
    for key in foo:
        if key in bar:
            out[key] = foo[key] / bar[key]
    return out 
```

```python
#use_package.py
import package.list_ops as lo #내가 폴더 이름은 pakcage로 만들어서 바꿔줘야 한다.
import package.dict_ops as do

weights = [65, 90, 42, 76]
heights = [1.65, 1.78, 1.59, 1.80]
heights_sq = lo.multiply(heights, heights)
bmi = lo.divide(weights, heights_sq)
print("BMI : ", bmi)

w_names = ["RM", "Suga", "Jin", "V"]
h_names = ["Jimin", "RM", "Suga", "Jin"]
weights = dict(zip(w_names, weights))
heights = dict(zip(h_names, heights))
print("dict weights:", weights)
print("dict heightss:", heights)

heights_sq = do.multiply(heights, heights)
bmi = do.divide(weights, heights_sq)
print("BMI:", bmi)
```



### 연습문제

-  dict_ops.py에 코드 추가, iter_ops 파일 추가



## Use Basic Packages

## 강력한 파이썬의 패키지들

## 1. Utilities

### 1.1 sys.path

```python
import sys

print(sys.path)
```

```python
import sys
new_path = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/pakcage"
sys.path.append(new_path)

import list_ops
print(list_ops.spam)
```

- 부모폴더와 자식폴더는 `//` 또는 `\`로 구분해야한다. 경로를 탐색기에서 복사해서 붙이면 그냥 `/` 하나만 있는데 둘 중 하나로 수정해줘야 한다. 

### 1.2 파일이나 폴더 생성/삭제

- 교수님은 코딩을 잘하시니까 사진 삭제도 코딩을 하셔서 하시는구나...거리감이 느껴진다...
- os.mkdir(dirpath): `dirpath` 경로에 폴더를 만든다.
- shutil.rmtree(dirpath, ignore_errors): `dirpath` 경로의 폴더를 지운다.
- os.remove(filepath): `filepath` 경로의 파일을 지운다.

```python
import os
import shutil
tempdir = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir"
tempfile1 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile1.txt"
tempfile2 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile2.txt"

def create():
    os.mkdir(tempdir)
    try:
        os.mkdir(tempdir)
    except FileExistsError as e:
        print(e)

    with open(tempfile1, "w") as f:
        f.write("blurblur 1")

    with open(tempfile2, "w") as f:
        f.write("blurblur 2")
    
    print("create two files")

    #파일 이동
    shutil.move(tempfile1, tempfile1.replace("/tempdir", ""))
    shutil.move(tempfile2, tempfile2.replace("tempfile2", "tf2"))
    


def delete():
    os.remove(tempfile1)
    try:
        os.remove(tempfile1)
    except FileNotFoundError as e:
        print(e)
    
    shutil.rmtree(tempdir)
    try:
        shutil.retree(tempdir)
    except FileNotFoundError as e:
        print(e)

    shutil.rmtree(tempdir, ignore_errors=True)
    print("delete tempdir")

if __name__ == "__main__":
    create()
    # delete()
```



### 1.3 파일 폴더 존재 확인

파일이나 폴더가 이미 있는지 확인하는 함수

- os.path.isdir()
- op.path.isfile()

```python
import os
import shutil
tempdir = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir"
tempfile1 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile1.txt"
tempfile2 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile2.txt"
os.mkdir(tempdir)

if os.path.isfile(tempfile1):
    print(f"{tempfile1} exists. remove it now")
    os.remove(tempfile1)
else:
    print(f"{tempfile1} does NOT exists")

if os.path.isdir(tempdir):
    print(f"{tempdir} exists. remove it now")
    shutil.rmtree(tempdir)
else:
    print(f"{tempdir} does NOT exists")
```



### 1.4 경로명 만들기

- os.path.join() : 폴더경로와 파일명을 합칠 때
- os.path.basename() : 전체 경로에서 마지막 파일이나 폴더명을  분리할 때
- os.path.dirname() : 그것이 속한 경로명만 추출하고 싶을 때

```python
import os
curfile = __file__
curfile = os.path.abspath(curfile) #경로 받았다
print([curfile]) 

filename = os.path.basename(curfile) #파일 이름.
print("file name : ", filename)

pathname = os.path.dirname(curfile)
print("dir name : ", pathname)

#경로와 파일명 합치기
newfile = os.path.join(pathname, "newfile.txt")
print("new file path : ", newfile)
with open(newfile, "w") as f:
    f.write("new file")

newpath = os.path.join(pathname, "new", "path", "name")
print("new path : ", newpath)
```



### 1.5 파일목록 출력

다수의 파일이나 폴더들을 자동으로 관리해야 한다고 했을 때 일단 어떤 파일들이 있는지 목록을 만들 수 있어야 한다. 

파일 목록을 보는 방법

- os.listdir()
- glob.glob()

```python
import os
import glob
curfile = os.path.abspath(__file__)
curdirpath = os.path.dirname(curfile)
files = os.listdir(curdirpath)
print("file list : ", files)

search_pattern = os.path.join(curdirpath, "*") #전체 다
print("search pattern : ", search_pattern)
fileList = glob.glob(search_pattern)
print("file list : ", fileList)

search_pattern = os.path.join(curdirpath, ".py") #.py로 끝나는거 
print("search pattern : ", search_pattern)
pyfileList = glob.glob(search_pattern)
print(".py file list : ", pyfileList)

filess = [file for file in fileList if os.path.isfile(file)]
dirss = [file for file in fileList if os.path.isdir(file)]
print("file liset : ", filess)
print("dir list : ", dirss)
```

- 경로를 없앤 새로운 file list

```python
#경로명을 없앤 새로운 file list
import os
import glob
curfile = os.path.abspath(__file__)
curdirpath = os.path.dirname(curfile)
files = os.listdir(curdirpath)
print("file list : ", files)

search_pattern = os.path.join(curdirpath, "*") #전체 다
print("search pattern : ", search_pattern)
fileList = glob.glob(search_pattern)
print("file list : ", fileList)

search_pattern = os.path.join(curdirpath, ".py") #.py로 끝나는거 
print("search pattern : ", search_pattern)
pyfileList = glob.glob(search_pattern)
print(".py file list : ", pyfileList)

filess = [os.path.basename(file) for file in fileList if os.path.isfile(file)]
dirss = [os.path.basename(file) for file in fileList if os.path.isdir(file)]

print("file liset : ", filess)
print("dir list : ", dirss)
```





## 2. numpy

http://taewan.kim/post/numpy_cheat_sheet/



### 2.1 Array vs Matrix

### 2.2 Array Creation

```python
import numpy as np

array1d = [1, 2, 3, 4]
array2d = [[1,2], [3, 4]]
array3d = [[[1,2], [3,4]], 
            [[5,6], [7, 8]]]
print("array1d -> ", array1d)
print("array1d : ", np.array(array1d, dtype=int))
print("array2d -> ", array2d)
print("array2d : \n", np.array(array2d, dtype=int))
print("array3d -> ", array3d)
print("array3d : \n", np.array(array3d, dtype=int))
```



```python
#일정한 패턴 가진 행렬 만들고 싶다.
import numpy as np
print("ones\n", np.ones((2, 4))) #2,4를 하나의 튜플로 만들어서 넣어준다.
print("zeros\n", np.zeros((3, 2))) #영행렬
print("identity\n", np.identity(3)) #대각선만 1인거
print("identity\n", np.eye(3)) #매틀랩에서 쓴다. 위랑 같은 함수다.
print("linear space:", np.linspace(5, 10, 11)) #등차수열 5와 10사이 11개숫자 등간격으로 
print("arange:", np.arange(5, 10, 0.5)) #간격 지정 lineapce와 다른 점은 arange는 끝에 10 안들어간다. 10미만까지 들어간다.
print("permutation:\n", np.random.permutation(10)) #10개의 숫자를 랜덤하게 막 섞어준다. 0~9
```

```python
import numpy as np
print("linear space:", np.linspace(5, 10, 11)) 
print("arange:", np.arange(5, 10, 0.5)) 
print("permutation:\n", np.random.permutation(10)) 
array = np.linspace(5, 19, 11)
indices = np.random.permutation(10)
print("indices : ", indices)
print(array[indices])
```

- np.random
  - np.random.rand(d0, d1, …, dn): 입력한 크기의 난수배열 생성. 값은 [0, 1) 사이의 값을 uniform sampling 한다.
  - np.random.randn(d0, d1, …, dn): 입력한 크기의 난수배열 생성. 값은 평균 0, 표준편차 1의 정규분포로부터 표본추출한다.
  - np.random.randint(low, high, size): 입력한 크기의 정수 난수배열 생성. `[low, high)` 사이의 정수를 랜덤생성하여 `size`의 크기의 배열을 만든다.

```python
import numpy as np

print("uniform [0, 1)\n", np.random.rand(3, 4))
print("normal distrivution 정규분포 [0, 1)\n", np.random.randn(5, 5))
print("rand int \n", np.random.randint(0, 5, (2, 3)))
```





### 2.3 Array Shape

- np.ndarray.shape : 각 차원의 크기 정보를 튜플로 가지고 있다.
- np.ndarray.ndim : 전체 차원수

```python
import numpy as np

foo = np.ones((3, 4, 2))
print(foo.shape) 
print(foo.ndim) 
```



- np.ndarray.reshape() : 배열 차원 변경

```python
import numpy as np

foo = np.arange(0, 6)
print("foo -> ", foo, foo.shape)
print("foo (2,3)\n", foo.reshape(2, 3)) #원소가 6개인데 3X3하라고 하면 에러난다.
print("foo (2,3)\n", foo.reshape(2, -1))
foo3d = foo.reshape(2, 3, 1) #1은 가장 안 쪽에 원소1개짜리 배열이 들어있다...
print("foo (2,3,1)\n", foo3d)
print("foo (3,2)\n", foo3d.reshape(3, 2))

'''
3X2   2X3
01
23     012
45     345
'''

print("foo (3,2)\n", foo3d.reshape(2, 3))
```





### 2.4 Array Indexing, Slicing

```python
import numpy as np

data_list = [[[5, 6, 2], [3, 4, 9]], [[1, 7, 2], [3, 8, 0]]]
data = np.array(data_list)
print(data)
print(data.shape)

#list
print("data_list[0] : \n", data_list[0])
print("data_list[0][1] : \n", data_list[0][1])
print("data_list[0][1][2] : \n", data_list[0][1][2])
#numpy배열
print("data[0] : \n", data[0])
print("data[0][1] : \n", data[0][1])
print("data[0][1][2] : \n", data[0][1][2])
```



# 이거 해봐~~~

```python
#슬라이싱
#numpy 여러 차원 슬라이싱 가능하다.
import numpy as np

data_list = [[[5, 6, 2], [3, 4, 9]], [[1, 7, 2], [3, 8, 0]]]
data = np.array(data_list)

# print(data)
# print(data[:, :, 1]) #1번원소들만 추출... 6478
# print(data[0, :, 1])
# print(data[0, :, 1:])
# print(data[:1, 1:, :])
#하나의 원소들만 가져오긴 했지만 슬라이싱으로 해서 차원이 사라지지 않았다.

print(data[0, 1, :])
print(data[:1, 1:, :])
#같지만 인덱싱 슬라이싱 차이...

data = np.random.randint(0, 10, (3, 4))
print(data)
print(data[:2, 2:])
```



numpy 차원 이해 어렵다.

기하학적으로 이해하려면 어렵고 그냥 숫자 나열인데 2개3개 묶여있다고 생각하는게 정신건강에 좋다.



### 2.5 Array Operations

```python
import numpy as np

foo = np.array([[9, 3, 2], [1, 3, 9], [1, 6, 8]])
bar = np.array([[1, 4, 2], [3, 3, 4], [2, 1, 3]])

print("foo\n", foo)
print("bar \n", bar)
print("foo - bar \n", foo - bar)
print("foo * bar \n", foo * bar) #행렬곱이 아니다.
print("foo ** bar \n", foo ** bar)
print("foo @ bar \n", foo @ bar) #행렬곱?
```











