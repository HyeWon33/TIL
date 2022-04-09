# 1. 파이썬 시작하기

## 001 
#화면에 문자열 출력

# print("Hello World")



## 002
# '

# print("Mary's cosmetics")


## 003
# "

# print('신씨가 소리질렀다. "도둑이야".')



## 004

# print("C:\Windows")


## 005
# \t, \n

# print("안녕하세요. \n만나서\t\t반갑습니다.")
# \n : 개행
# \t : 탭



## 006

# print("오늘은", "일요일")
# # >> 오늘은 일요일
# print("오늘은"+"일요일")
# # >> 오늘은일요일



## 007
# naver;kakao;sk;samsung

# print("naver;kakao;sk;samsung")

# 정답
# print("naver", "kakao", "sk", "samsung", sep=";")
# sep인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론을 출력한다.



## 008
# naver/kakao/sk/samsung

# print("naver", "kakao", "sk", "samsung", sep="/")



## 009
# print("first");print("second")

# ...

# 정답
# print("first", end=""); print("second")
# # end=""은 print문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있다.
# # 기본 값으로는 개행 \n이 들어가 있다.



# 010
# 5/3

# print(5/3)