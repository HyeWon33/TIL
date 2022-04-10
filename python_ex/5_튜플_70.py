## 071 튜플 만들기

# my_variable = ()
# print(type(my_variable))



## 072

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# print(movie_rank, type(movie_rank))



## 073 ***********

# tup = (1,)
# print(tup, type(tup))
# # 그냥 1만 쓰면 파이썬은 튜플이 아닌 정수로 인식한다. 하나의 데이터가 저장되는 경우 쉼표를 입력해야 한다.



## 074 오류 원인?

# t = (1, 2, 3)
# t[0] = 'a'
# # 튜플은 원소의 값을 변경할 수 없다.



## 075 t의 데이터 타입?

# t = 1, 2, 3, 4
# print(type(t))
# # 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자의 편의를 위해 괄호 없이도 동작한다.



## 076 

# # 튜플의 값은 변경할 수 없기 때문에, 리스트와 달리 t[0] = 'A'는 동작하지 않고 새로운 튜플 t를 만든다.
# t = ('A', 'b', 'c')
# print(t)



## 077 튜플을 리스트로

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest_lis = list(interest)
# print(interest_lis)



## 078 리스트를 튜플로

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_tup = tuple(interest)
# print(interest_tup)



## 079 튜플 언팩킹

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# # 튜플이 풀리나?
# # 풀리네..



## 080 range 함수 ***********

# data = tuple(range(2, 100, 2))
# print(data)