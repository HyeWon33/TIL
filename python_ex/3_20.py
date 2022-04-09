## 021
# 문자열 인덱싱

# letters = 'python'
# print(letters[0], letters[2])
# # 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부른다. 파이썬 인덱싱은 0부터 시작한다.



## 022
# 뒤에 4자리만 출력

# license_plate = "24가 2210"
# print(license_plate[4:])
# # 문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부른다. 음수 값은 문자열 뒤에서부터 인덱싱 또는 슬라이싱함을 의미한다. 슬라이싱에서 시작 인덱스를 생략하면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미한다.



## 023 *******************
# 홀만 출력

# string = "홀짝홀짝홀짝"

# print("실행 예 : ")

# # 정답
# print(string[::2])
# 슬라이싱할 때 시작인덱스:끝인덱스:stride(보폭, 간격)을 지정할 수 있다.
# 문자열을 작성하게되면, 각 문자마다 고유의 번호가 매겨지는데 이 번호를 오프셋이라고 하고, 오프셋을 이용하여 문자열에서 문자를 추출하는 것을 인덱싱이라 한다.



## 024
# 문자열 거꾸로 뒤집어 출력

# string = "PYTHON"
# re_string = string[::-1]

# print(re_string)



## 025 *******************
# -제거하고 출력

# phone_number = "010-111-2222"

# print("실행 예")

# # 정답
# # replace 메서드 : 문자열을 일부 치환할 수 있다. 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴된다.
# phon_num = phone_number.replace("-", " ")
# print(phon_num)



## 026
#025번 문제 붙여서 출력

# phone_number = "010-111-2222"
# # 정답
# phon_num = phone_number.replace('-', '')
# print(phon_num)
# # 아니 replace할 때 저기 뛰었다고 출력이 뛰어져서 나왔구나...



## 027 *******************

# url = "http://sharebook.kr"

# # 정답 
# # splite 사용
# do_url = url.split(".")
# print(do_url[1])



## 028 문자열은 immutable

# lang = 'python'
# lang[0] = 'p'
# print(lang)
# # 에러난다. 문자열은 수정할 수 없다.



## 029 replace 메서드
# a-> A

# string = 'abcdfe2a354a32a'
# u_string = string.upper() # 아~ 이건 다 대문자로 바꾸는거지
# print(u_string)

# a_string = string.replace("a", "A")
# print(a_string)



## 030 replace 메서드

# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# #abcd가 그대로 출력된다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문에 replace메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
# b = string.replace('b', 'B')
# print(b)