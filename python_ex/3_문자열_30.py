## 031 문자열 합치기

# a = "3"
# b = "4"
# print(a+b)
# # 34



## 032 문자열 곱하기

# print("Hi" * 3)
# # HiHiHi



## 033 문자열 곱하기

# print("-"*80)



## 034 문자열 곱하기
# python java python java python java python java

# t1 = "python"
# t2 = "java"

# t3 = t1 + " " + t2 + " "
# print(t3 * 4)



## 035 문자열 출력
# %formatting

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름 : %s 나이 : %d" % (name1, age1))
# print("이름 : %s 나이 : %d" % (name2, age2))



## 036 문자열 출력
# format()

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름 : {} 나이 : {}".format(name1, age1))
# print("이름 : {} 나이 : {}".format(name2, age2))



## 037 문자열 출력
# f-string

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print(f"이름 : {name1} 나이 : {age1}")
# print(f"이름 : {name2} 나이 : {age2}")



## 038 컴마 제거하기
# 컴마제거 -> 정수 타입

# 상장주식수 = "5,969,782,550"
# num = int(상장주식수.replace(",", ""))
# print(num, type(num))



## 039 문자열 슬라이싱
# 2020/03만 출력

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])



## 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보기.

# data = "   삼성전자    "
# print(data.strip())
# # 문자열에서 strip()메서드를 사요하면 좌우의 공백을 제거할 수 있다. 이때 원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환된다.
