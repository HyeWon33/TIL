# # 1. 응용 문제

# ## Function

# ### 1. 함수 정의



# def mul_list(data, start_in, end_in, prin):
#     if end_in is None:
#         m_data = data[start_in:]
#     else:
#         m_data = data[start_in:end_in+1]

#     if start_in is None:
#         m_data = data[:end_in+1]
#     else:
#         m_data = data[start_in:end_in+1]

#     mul = 1
#     a = 0
#     for ind, num in enumerate(m_data):
#         mul*=num

#     if prin:
#         print("m_data : ", m_data, "\nmul : ", mul)

#     return mul

# # def main():
# #     data = [2, 4, 6]
# #     mul_list(data, 0, 2, True)

# # if __name__ == "__main__":
# #     main()




# ### 2. Keyword Arguments

# data = [2, 4, 6, 8, 10]
# M = mul_list(data, 2, 4, True)

# print(" 입력 값이 어느 입력인자로 들어가야 하는지 명시적으로 보여줄 수 있다. 이렇게 입력하는 인자를 keyword argument (키워드 인자)라 한다.\n")
# print("키워드 인자는 반드시 위치 인자 뒤에 나와야 한다")
# M = mul_list(data, 2, 4, prin=True)
# M = mul_list(data, 2, end_in=4, prin=True)
# M = mul_list(data, start_in=2, end_in=4, prin=True)
# M = mul_list(data=data, start_in=2, end_in=4, prin=True)

# # M = mul_list(data, start=2, 4, True) #에러

# print("keyword argument 키워드 인자 섞어도 괜찮다.")
# M = mul_list(data, start_in=2, end_in=4, prin=True)
# M = mul_list(data, end_in=4, start_in=2, prin=True)
# M = mul_list(data, start_in=2, end_in=7, prin=True)

# ### 3. 인자 기본값 지정

# def mul_list_with_default(data, start_in=0, end_in=0, prin=False):
#     return mul_list(data, start_in, end_in, prin)

# print("function default arguments")
# avg = mul_list_with_default(data)
# print("amul_list_with_default(data) =>", avg)
# avg = mul_list_with_default(data, 3)
# print("mul_list_with_default(data, 3) =>", avg)
# avg = mul_list_with_default(data, end_in=5)
# print("mul_list_with_default(data, end_in=5) =>", avg)

### 연습문제

# def sum_list(list1, list2, shortlen, start=0, verbose=True):
#     list1 = list1[start:]
#     list2 = list2[start:]
#     if shortlen is False:
#         short = list1 if len(list1) < len(list2) else list2
#         longl = list2 if len(list1) < len(list2) else list1
#         for i in range(len(longl) - len(short)):
#             short.append(0)
#         sum_result = [s+l for s, l in zip(short, longl)]
#     else:
#         sum_result = [s+l for s, l in zip(list1, list2)]
#     if verbose:
#         print(f"{list1} + {list2} = {sum_result}")
#     return sum_result

# sum_list([1,2,3], [2,3,4,5,6], True)
# sum_list([1,2,3,], [2,3,4,5,6], False)

### 4. 변경 가능한 입력인자 개수

#### 4.1 *args

# pe_st = {"kim" : [172, 72, 270], "lee" : [160, 60, 260], "park" : [150, 50, 250]}

# def average_multi_subjects(scores, *args):
#     averages = {}
#     print("[pe_st_multi] args:", args)
#     print("[pe_st_multi] *args:", *args)
#     for subject in args:
#         avg = mul_list_with_default(data=scores[subject], start_in = 0, end_in = 2, prin=False)
#         print(f" {subject} 의 키 몸무게 발사이즈의 곱 : {avg:.1f}")
#         averages[subject] = avg
#     return averages

# result = average_multi_subjects(pe_st, "kim")
# result = average_multi_subjects(pe_st, "kim", "lee", "park")

# def average_variable_arguments(data, multiple, *args):
#     # do some process ...
#     data = [d*multiple for d in data]
#     avg = mul_list_with_default(data, *args)
#     return avg


# def main():
#     data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     result = average_variable_arguments(data, 10, 1, 7)
#     print("average_variable_arguments(data, 10, 1, 7) =>", result)
#     result = average_variable_arguments(data, 10, 1, 7, True)
#     print("average_variable_arguments(data, 10, 1, 7, True) =>", result)

#     result = mul_list_with_default(data, 1, 7)
#     print("average_list_with_default(data, 1, 7) =>", result)
#     result = mul_list_with_default(data, 1, 7, True)
#     print("average_list_with_default(data, 1, 7, True) =>", result)


# if __name__ == "__main__":
#     main()



#### 4.2 **kwargs

# def average_keyworded_args(data, multiple, **kwargs):
#     print("[average_subjects_varargs] kwargs:", kwargs)
#     data = [d*multiple for d in data]
#     avg = mul_list_with_default(data, **kwargs)
#     return avg

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = average_keyworded_args(data, 10, start_id=1, end_id=3)
# print("average_keyworded_args(data, start_id=1, end_id=3) =>", result)

### 연습문제

# def sum_list(list1, list2, shortlen, start=0, verbose=True):
#     list1 = list1[start:]
#     list2 = list2[start:]
#     if shortlen is False:
#         short = list1 if len(list1) < len(list2) else list2
#         longl = list2 if len(list1) < len(list2) else list1
#         for i in range(len(longl) - len(short)):
#             short.append(0)
#         sum_result = [s+l for s, l in zip(short, longl)]
#     else:
#         sum_result = [s+l for s, l in zip(list1, list2)]
#     if verbose:
#         print(f"{list1} * {list2} = {sum_result}")
#     return sum_result

# sum_list([1,2,3], [2,3,4,5,6], True)
# sum_list([1,2,3,], [2,3,4,5,6], False)

### 5. 변수 범위(Scope)

# global_num = 5
# def add_ten_local():
#     local_num = global_num + 10
#     print("add_ten_local 값 :", local_num)

# def add_ten_global():
#     try:
#         global_num = global_num + 10
#         print("add_ten_global 값 :", global_num)
#     except NameError as ne:
#         print(ne)

# def add_ten_global_two_steps():
#     try:
#         local_num = global_num + 10
#         global_num = local_num
#         print("add_ten_global_two_steps 값 :", global_num)
#     except NameError as ne:
#         print(ne)

# def add_ten_global_use_global():
#     global global_num
#     global_num = global_num + 10
#     print("add_ten_global_use_global 값 :", global_num)


# def main():
#     add_ten_local()
#     add_ten_global()
#     add_ten_global_two_steps()
#     add_ten_global_use_global()
#     print("global_num=", global_num)


# if __name__ == "__main__":
#     main()

### 6. 바람직한 파이썬 코딩 스타일

# def main():
#     data_lis = [2, 4, 6, 8, 10, 1, 2, 3, 4, 5]
#     result = average_keyworded_args(data_lis, 10, start=1, skip=[2, 3])
#     print(f"average_keyworded_args(data_lis, start=1, skip=[2, 3]) => {result}")
#     result = average_keyworded_args(data_lis, 10, start=1, end=7)
#     print(f"average_keyworded_args(data_lis, start=1, end=7) => {result}")

# def average_keyworded_args(data_lis, multiple, **kwargs):
#     data_lis = [d*multiple for d in data_lis]
#     avg = average_list_with_default(data_lis, **kwargs)
#     return avg

# def average_list_with_default(data_lis, start=0, end=None, skip=None, verbose=False):
#     if skip is None:
#         skip = []
#     return average_list(data_lis, start, end, skip, verbose)

# def average_list(data_lis, start, end, skip, verbose):
#     if end is None:
#         avg_data = data_lis[start:]
#     else:
#         avg_data = data_lis[start:end]

#     sum = 0
#     for ind, num in enumerate(avg_data):
#         if ind not in skip:
#             sum += num
#     dlen = len(avg_data) - len(skip)
#     average = sum / dlen
#     if verbose:
#         print(f"average {start}~{end} with skipping {skip} = {average}")
#     return average

# if __name__ == '__main__':
#     main()


## Class and File IO

### 1. 클래스 사용법


# class Fruit:
#     def __init__(self, name):
#         self.name = name
#         self.cnt = 0
#         self.price = 0

#     def num(self, cnt):
#         self.cnt = cnt
#         print("사과 ", self.cnt, "개")

#     def pri(self):
#         self.price = 1000 * self.cnt
#         print(f"사과 {self.cnt}개 가격은 {self.price}")
        

# def main():
#     app = Fruit("apple")
#     app.num(5)
#     app.pri()
#     print(f"과일 이름은 {app.name}이고 {app.cnt}개를 구매하면 {app.price}원이다.")
    

# if __name__ == '__main__':
#     main()


### 2. 상속과 다형성

# print("===== object oriented programming")
# class Fruit:
#     def __init__(self, name):
#         self.name = name
#     def introduce(self):
#         print("Fruit is", self.name)
#     def sound(self):
#         print("...")
# class Apple(Fruit):
#     def __init__(self, name):
#         super().__init__(name) #부모클래스의 생성자를 호출
#     def sound(self):
#         print("아삭~~~")
# class Banana(Fruit):
#     def __init__(self, name):
#         super().__init__(name)
#     def sound(self):
#         print("물렁~~")

# def main():
#     apple = Apple("apple1")
#     apple.introduce()
#     apple.sound()
#     fruit = [Fruit("fru"), Apple("apple1"), Banana("Banana")]
#     for fru in fruit:
#         fru.introduce()
#         fru.sound()

# if __name__ == '__main__':
#     main()


### 연습문제

# class Operator:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print("Operator is", self.name)

#     def op(self, num1, num2):
#         print(f"{num1}, {num2}")


# class Add(Operator):
#     def __init__(self, name):
#         super().__init__(name) #부모클래스의 생성자를 호출

#     def op(self, num1, num2):
#         print(f"{num1} + {num2} = {num1 + num2}")


# class Minus(Operator):
#     def __init__(self, name):
#         super().__init__(name)

#     def op(self, num1, num2):
#         print(f"{num1} - {num2} = {num1 - num2}")


# class Multiplication(Operator):
#     def __init__(self, name):
#         super().__init__(name)

#     def op(self, num1, num2):
#         print(f"{num1} * {num2} = {num1 * num2}")


# def main():
#     operator = [Add("add"), Minus("minus"), Multiplication("multiplication")]
#     for oper in operator:
#         oper.introduce()
#         oper.op(4, 2)


# if __name__ == '__main__':
#     main()


### 파일 입출력

# fout = open("hw2.txt", "w")
# fout.write("hw2......")
# fout.close()
# print("hw2.txt file was written")

# fin = open("hw2.txt", "r")
# contents = fin.read()
# fin.close()
# print(contents)


#### 1. 파일 열기

# try:
#     f = open("hw2.txt", "r")
# except FileNotFoundError as fe:
#     print(fe)

# with open("hw2.txt", "r") as fr:
#     data = fr.read()
#     print("check closed under 'with':", fr.closed)
#     print(data)

# print("check closed outside 'with':", fr.closed)

#### 2. 파일 쓰기

# bangx3 = ["BANG! BANG! BANG!", "BANG! BANG! BANG!", "빵야 빵야 빵야",
#             "BANG! BANG! BANG!", "BANG! BANG! BANG!", "빵야 빵야 빵야",
#             "다 꼼짝 마라 다 꼼짝 마", "다 꼼짝 마라 다 꼼짝 마",
#             "오늘 밤 끝장 보자 다 끝장 봐", "오늘 밤 끝장 보자",
#             "빵야 빵야 빵야"]

# print("\n 뱅뱅뱅 가사 파일에 쓰기")
# with open("bangx3.txt", "w") as f:
#     for i, line in enumerate(bangx3):
#         f.write(f"{i:2}:" + line + "\n")

#### 3. 파일 읽기

##### read()
# print("use read")
# with open("bangx3.txt", "r") as f:
#     lyrics = f.read()
#     print(lyrics)

##### readline()
# print("use readline")
# with open("bangx3.txt", "r") as f:
#     lyrics = []
#     line = f.readline()
#     while line:
#         line = line.rstrip("\n")
#         lyrics.append(line)
#         line = f.readline()
# print("\n".join(lyrics))

##### readlines()
# print("use readlines")
# with open("bangx3.txt", "r") as f:
#     lyrics = f.readlines()
#     lyrics = [line.rstrip("\n") for line in lyrics]
#     print("\n".join(lyrics))


### 연습문제

# matrix_str = "4 2\n5 3"
# with open("matrix.txt", "w") as f:
#     f.write(matrix_str)

# with open("matrix.txt", "r") as f:
#     data = f.readlines()

# data = [d.rstrip("\n") for d in data]
# data = [d.split() for d in data]

# data = [[int(elem) for elem in row] for row in data]
# # ↓↓
# # numdata = []
# # for row in data:
# #     numrow = [int(elem) for elem in row]
# #     numdata.append(numrow)

# print(data)

# determinant = data[0][0] * data[1][1] - data[0][1] * data[1][0]
    
# print("determinant : ", determinant)



## Module and Package
### 2. 모듈 만들기

# list_ops.py
# def add(foo, bar):
#     re = []
#     for f, b in zip(foo, bar):
#         re.append(f + b)
#     return re

# def subtract(foo, bar):
#     re = []
#     for f, b in zip(foo, bar):
#         re.append(f - b)
#     return re

# def multiply(foo, bar):
#     re = []
#     for f, b in zip(foo, bar):
#         re.append(f * b)
#     return re

# def divide(foo, bar):
#     re = []
#     for f, b in zip(foo, bar):
#         re.append(f / b)
#     return re

# spam = [11, 22]
# ham = [33, 44]
# if __name__ == '__main__':
#     eggs = add(spam, ham)

#### 모듈 이름 그대로 가져오는 방법

# import list_ops

# foo = [1, 2, 3, 4, 5]
# bar = [1, 2, 3, 4]
# gor = list_ops.add(foo, bar)
# print(f"{foo} + {bar} = {gor}")
# # => [1, 2, 3, 4, 5] + [1, 2, 3, 4] = [2, 4, 6, 8]
# print(f"list_ops.spam: {list_ops.spam}")
# # => list_ops.spam: [11, 22]
# gor = list_ops.multiply(list_ops.spam, list_ops.ham)
# print(f"{list_ops.spam} * {list_ops.ham} = {gor}")
# # => [11, 22] * [33, 44] = [363, 968]

# foo = [1, 2, 3, 4, 5]
# bar = [1, 2, 3, 4]
# gor = add(foo, bar)
# print(f"{foo} + {bar} = {gor}")
# # => [1, 2, 3, 4, 5] + [24, 52, 13, 27] = [25, 54, 16, 31]
# print(f"list_ops.spam: {spam}")
# # => list_ops.spam: [51, 23]
# gor = multiply(spam, ham)
# print(f"{spam} * {ham} = {gor}")
# # => [51, 23] * [34, 67] = [1734, 1541]

# try:
#     print("list_ops.eggs: {}".format(list_ops.eggs))
# except Exception as e:
#     print(e)
#     # => module 'list_ops' has no attribute 'eggs'


#### 모듈 이름을 바꿔서 가져오는 방법

# import list_ops as l_o

# gor = l_o.subtract(foo, bar)
# print("{} + {} = {}".format(foo, bar, gor))
# gor = l_o.divide(bar, foo)
# print("{} * {} = {}".format(bar, foo, gor))


#### 모듈에서 지정한 객체만 가져오는 방법

# from list_ops import add, subtract, spam

# gor = add(foo, bar)
# print(f"{foo} + {bar} = {gor}")
# gor = subtract(bar, foo)
# print(f"{bar} - {foo} = {gor}")
# print(f"spam = {spam}")


### 3. 패키지 만들기

# # dict_ops.py
# def add_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] + bar[key]
#     return out

# def subtract_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] - bar[key]
#     return out

# def multiply_op(foo, bar):
#     out = {}
#     for i, key in enumerate(foo):
#         if key in bar:
#             out[i] = foo[i] * bar[i]
#     return out

# def divide_op(foo, bar):
#     out = {}
#     for i, key in enumerate(foo):
#         out[i] = foo[i] / bar[i]
#     return out

#use_package.py
# #원래대로 패키지를 만들고 했으면 import를 해줘야 하는데 과제제출을 위해 한 코드에 작성했습니다.
# # import package.list_ops as lo
# # import package.dict_ops as do

# #위의 함수명 앞세 as로 설정한 변수를 써줘야 합니다. 
# #예를들어 lo.multiply_op()이렇게 써줘야 하는데 한 코드에 작성하다보니 분리해서 실행할 때 없던 에러가 생겨서 코드를 수정했습니다.
# #TypeError: list indices must be integers or slices, not float 이런 에러때문에 리스트를 enumerate하고 나온 딕셔너리를 다시 리스트를 바꿔주는 코드를 작성했습니다.

# weights_bmi = [65, 90, 42, 76]
# heights_bmi = [1.65, 1.78, 1.59, 1.80]
# heights_sq = multiply_op(heights_bmi, heights_bmi)
# heights_sq = list(heights_sq.values())
# bmi = divide_op(weights_bmi, heights_sq)
# bmi = list(bmi.values())
# print("BMI:", bmi)




# # dict_ops.py
# def add_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] + bar[key]
#     return out

# def subtract_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] - bar[key]
#     return out

# def multiply_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] * bar[key]
#     return out

# def divide_op(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] / bar[key]
#     return out

# #use_package.py
# weights_bmi = [65, 90, 42, 76]
# heights_bmi = [1.65, 1.78, 1.59, 1.80]
# w_names = ["RM", "Suga", "Jin", "V"]
# h_names = ["Jimin", "RM", "Suga", "Jin"]
# weights = dict(zip(w_names, weights_bmi))
# heights = dict(zip(h_names, heights_bmi))
# print("dict weights:", weights)
# print("dict heights:", heights)
# heights_sq = multiply_op(heights, heights)
# bmi = divide_op(weights, heights_sq)
# print("BMI:", bmi)



### 연습문제

#iter_ops

#dict_ops
# def add(foo, bar):
#     return {fkey: foo[fkey] + bar[fkey] for fkey in foo if fkey in bar}

# def subtract(foo, bar):
#     return {fkey: foo[fkey] - bar[fkey] for fkey in foo if fkey in bar}

# def multiply(foo, bar):
#     return {fkey: foo[fkey] * bar[fkey] for fkey in foo if fkey in bar}

# def divide(foo, bar):
#     return {fkey: foo[fkey] / bar[fkey] for fkey in foo if fkey in bar}

# #list_ops
# def add(foo, bar):
#     return [f+b for f, b in zip(foo, bar)]

# def subtract(foo, bar):
#     return [f-b for f, b in zip(foo, bar)]

# def multiply(foo, bar):
#     return [f*b for f, b in zip(foo, bar)]

# def divide(foo, bar):
#     return [f/b for f, b in zip(foo, bar)]


# def check_prime_number(numbers):
#     out = []
#     for i in numbers:
#         for j in range(2, i):
#             if i % j == 0:
#                 out.append(False)
#                 break
#             out.append(True)
#             break
#     return out


# def main():
#     lis = [341, 12, 523, 59]
#     print(check_prime_number(lis))

# if __name__ == "__main__":
#     main()









# 4.2 **kwargs

# def aver_list(data, start, end, skip, verbose):
#     if end is None:
#         avg_data = data[start:]
#     else:
#         avg_data = data[start:end]

#     sum = 0
#     for ind, num in enumerate(avg_data):
#         if ind + start not in skip:
#             sum += num
#     dlen = len(avg_data) - len(skip)
#     average = sum / dlen

#     return average

# def aver_list_with_default(data, start=0, end=None, skip=None, verbose=False):
#     if skip is None:
#         skip = []
#     return aver_list(data, start, end, skip, verbose)

# def aver_keyworded_args(data, multiple, **kwargs):
#     print("[average_subjects_varargs] kwargs:", kwargs)
#     data = [d*multiple for d in data]
#     avgverage = aver_list_with_default(data, **kwargs)
#     return avgverage

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = aver_keyworded_args(data, 10, start=1, skip=[2, 3], end=2)
# print("aver_keyworded_args(data, start=1, skip=[2, 3], end=2) =>", result)
# result = aver_keyworded_args(data, 5, start=1, end=7)
# print("aver_keyworded_args(data, start=1, end=7) =>", result)



## funciton.. 연습문제

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
        print(f"average over indices [{start}~{end}) with skipping index {skip} = {average}")
    return average


def average_list_with_default(data, start=0, end=None, skip=None, verbose=False):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip, verbose)


def average_multi_subjects(scores, *args):
    averages = {}
    print("[average_multi_subjects] args:", args)
    print("[average_multi_subjects] *args:", *args)
    for subject in args:
        avg = average_list_with_default(scores[subject], verbose=False)
        print(f"average over {subject} scores: {avg:.1f}")
        averages[subject] = avg
    return averages


def average_keyworded_args(data, multiple, **kwargs):
    print("[average_subjects_varargs] kwargs:", kwargs)
    data = [d*multiple for d in data]
    avg = average_list_with_default(data, **kwargs)
    return avg

def average_subjects_kwargs(scores, multiple, *args, **kwargs):
    avger = {}
    print("[average_multi_subjects] *args : ", *args)
    for subject in args:
        scores[subject] = [d*multiple for d in scores[subject]]
        avg = average_list_with_default(scores[subject], verbose=False, **kwargs)
        print(f"average over {subject} scores  : {avg:.1f}")
        avger[subject] = avg
    return avger

def main():
    subject_scores = {"cpp": [57, 36, 80, 53, 23], "java": [46, 88, 72, 15, 54], "ruby": [85, 23, 34, 91, 42]}

    result = average_subjects_kwargs(subject_scores, 10, "cpp", "java", start=1, end=4, skip=[2])
    print(result)


if __name__ == '__main__':
    main()