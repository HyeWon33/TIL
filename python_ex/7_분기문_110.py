## 111 사용자로부터 입력받은 문자열 두번 출력

# a = input("입력 : ")
# print(a*2)



## 112 하나의 숫자 입력받고 10 더해서 출력

# num = int(input("숫자 : "))
# print(num + 10)



## 113 짝수 홀수 판별

# num = int(input("숫자 입력 : "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")



## 114 

# num = int(input("입력값 : "))
# if num+20 > 255:
#     print("출력값 : ", 255)
# else:
#     print("출력값 : ", num+20)



## 115

# num = int(input("입력값 : "))
# if num-20 > 255:
#     print("출력값 : ", 255)
# elif num-20 < 0:
#     print("출력값 : ", 0)
# else:
#     print("출력값 : ", num-20)



## 116 사용자로부터 입력 받은 시간이 정각인지 판별

# tim = input("현재시간 : ")
# tim_lis = tim.split(":")
# if tim_lis[1] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")



## 117 리스트에 포함되어있는지 확인

# # 나
# fruit = ["사과", "포도", "홍시"]
# fru = input("좋아하는 과일은 ? ")
# for i in fruit:
#     if(i == fru):
#         print("정답입니다.")
#         break
#     else:
#         print("오답입니다.")
#         break

# # 답
# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은?")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")



## 118 

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# inv = input("투자 종목 : ")
# if inv in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")



## 119 딕셔너리 키 값에 포함되어있나 확인

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# se = input("제가 좋아하는 계절은 : ")
# if se in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")



## 120 

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# fr = input("좋아하는 과일은? : ")
# if fr in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")