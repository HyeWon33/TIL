## 121 소문자 대문자

# al = input("문자 입력 : ")
# if al.islower() is True:
#     print("소->대 : ", al.upper())
# else:
#     print("대->소 : ", al.lower())



## 122 학점 출력

# score = int(input("score : "))
# if score>80 and score < 101:
#     print("A")
# elif score > 60 and score < 81:
#     print("B")
# elif score > 40 and score < 61:
#     print("C")
# elif score > 20 and score < 41:
#     print("D")
# else:
#     print("E")



## 123 환율..

# mo = input("입력 : ")
# mo_lis = mo.split(" ")
# mo_in = int(mo_lis[0])
# if mo_lis[1] == "달러":
#     print(f"{1167 * mo_in}원")
# elif mo_lis[1] == "엔":
#     print(f"{1.096 * mo_in}원")
# elif mo_lis[1] == "유로":
#     print(f"{1268 * mo_in}원")
# elif mo_lis[1] == "위안":
#     print(f"{171 * mo_in}원")



## 124 큰 숫자 출력
# 다 다른 숫자 입력하자ㅎㅎ

# num1 = int(input("input numer1 : "))
# num2 = int(input("input numer2 : "))
# num3 = int(input("input numer3 : "))

# if num1 > num2:
#     if num3 > num1:
#         print(num3)
#     else:
#         print(num1)
# else:
#     if num3 > num2:
#         print(num3)
#     else:
#         print(num2)
# # 아~ and 조건을 사용해서 더 간결하게 코드를 만들 수 있다.



## 125 통신사 출력 프로그램

# num = input("휴대전화 번호 입력 : ")
# num_lis = num.split("-")
# if num_lis[0] == "011":
#     print("SKT")
# elif num_lis[0] == "016":
#     print("KT")
# elif num_lis[0] == "019":
#     print("LGU")
# elif num_lis[0] == "010":
#     print("당신은 알수없음 사용자 입니다.")

# 변수에 skt kt 등을 저장해서 마지막에 한 번만 출력문을 사용할 수 있다..ㅎㅎ 와우



## 126 우편번호 입력받고 판별

# num = input("우편번호 : ")
# num_lis = list(num)
# gu = 0
# if num_lis[2] == "0" or num_lis[2] == "1" or num_lis[2] == "2":
#     gu = "강북구"
# elif num_lis[2] == "3" or num_lis[2] == "4" or num_lis[2] == "5":
#     gu = "도봉구"
# elif num_lis[2] == "6" or num_lis[2] == "7" or num_lis[2] == "8" or num_lis[2] == "9":
#     gu = "노원구"
# print(gu)

# 정답
# 홀리 쉿
# num = input("우편번호 : ")
# num = num[:3]
# if num in ["010", "011", "012"]:
#     print("강북구")
# elif num in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")



## 127 민증 성별 판별

# num = input("주민등록번호 : ")
# num_lis = num.split("-")
# se=num_lis[1][:1]
# if se in ["1", "3"]:
#     print("남자")
# else:
#     print("여자")

# 정답
# 주민번호 = input("주민등록번호: ")
# 주민번호 = 주민번호.split("-")[1]
# print(주민번호, type(주민번호))
# if 주민번호[0] == "1" or 주민번호[0] == "3":
#     print("남자")
# else:
#     print("여자")



## 128

# num = input("주민등록번호 : ")
# num = num.split("-")[1]
# print(num[1:3], type(num[1:3]))
# if num[1] == "0" and int(num[2]) >= 0 and int(num[2]) < 9:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

#정답
# 주민번호 = input("주민등록번호: ")
# 뒷자리 = 주민번호.split("-")[1]
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")



## 129
