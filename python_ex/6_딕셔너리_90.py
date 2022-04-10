## 091 딕셔너리 생성

# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
# print(inventory)



## 092 딕셔너리 인덱싱

# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
# print(inventory["메로나"][0], "원")



## 093 인덱싱

# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
# print(inventory["메로나"][1], "개")



## 094 추가

# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}

# inventory["월드콘"] = [500, 7]
# print(inventory)



## 095 keys()

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(list(icecream.keys()))



## 096 values()

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(list(icecream.values()))



## 097 values 합

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# price = list(icecream.values())
# print(sum(price))



## 098 update ************

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}

# icecream.update(new_product)
# print(icecream)



## 099 zip, dict


# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = {}
# result.update(zip(keys, vals))
# print(result)

# # 정답
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)



## 100 zip, dict

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)

