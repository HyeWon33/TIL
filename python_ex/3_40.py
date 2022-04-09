## 041 upper 메서드
# 대문자로 변경

# ticker = "btc_krw"
# print(ticker.upper())
# upper 경우에도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환된다. 반횐된 새로운 객체를 새로운 변수로 바인딩.



## 042 lower 메서드

# ticker = "BTC_KRW"
# print(ticker.lower())



## 043 capitalize 메서드

# string = 'hello'
# print(string.capitalize())



## 044 endswith 메서드
# ~로 끝나는지 확인

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))



## 045 endswith 메서드
# xlsx 또는 xls로 끝나는지 확인

# file_name = "보고서.xls"
# print(file_name.endswith("xlsx") or file_name.endswith("xls"))
# # 정답
# print(file_name.endswith("xlsx", "xls"))



## 046 startswith 메서드
# ~로 시작하는지 확인

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))



## 047 split 메서드

# a = "hello world"
# print(a.split())



## 048 split 메서드

# ticker = "btc_krw"
# print(ticker.split("_"))



## 049 split 메서드

# data = "2020-05-01"
# print(data.split("-"))



## 050 rstrip 메서드

# data = "039490         "
# print(data.rstrip())