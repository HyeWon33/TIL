# empty_list1 = []
# empty_list2 = list()
# basic_list = ["Hello", 1234, 1.234, True]
# depth2_list = ["Hello", 1234, [1.234, True]] 
# depth3_list = [["Hello"], [1234, [1.234, True]]]

# print(basic_list[2])
# print(basic_list[-2])

# print(depth2_list[2])
# print(depth2_list[2][0])

# print(depth3_list[1])
# print(depth3_list[1][1])
# print(depth3_list[1][1][0])

# print(basic_list[1:3]) #리스트로 출력
# print(basic_list[:3])

#겹치는 구간만 꺼내고 아예 안 겹치면 그냥 빈 리스트 나온다.
# print(basic_list[2:10]) 
# print(basic_list[4:10])

#인덱싱은 범위 벗어나면 에러 슬라이싱은 빈 리스트 나온다.

# print(list(depth2_list[2][:1]))
# print(depth2_list[2][:1])

# mammal = ["dog", "cat", "human"]
# reptile = ["snake", "lizard", "frog"]
# bird = ["eagle", "sparrow", "chicken"]
# animal = mammal + reptile + bird
# print(animal)

# members = ["나연", "정연", "지효"]
# tests = ["vocl", "dance", "rap"]
# first_row = members[0:1] * 3 + members[1:2]*3 + members[2:3]*3
# second_row  = tests * 3
# print(first_row)
# print(second_row)

# string = "system programming"


# print(len(string))
# mylist = [1,3,5,6,7,10]
# print(len(mylist))

# del string

# mylist = [1,2,3,4,5]
# del mylist[2]
# print(mylist)

# mylist = [1,2,3,4,5]
# mylist[0] = "Life"
# print(mylist)
# mylist[1:4] = ["is", "too", "short"]
# print(mylist)

# mylist = [1,2,3,4,5]
# mylist[1:4] = ["is", "too"] 
# print(mylist) # >> [1, 'is', 'too', 5]


# mylist = [1,2,3,4,5]
# mylist[1:4] = ["is", "too", "too", "too", "too"] 
# print(mylist) # >> [1, 'is', 'too', 'too', 'too', 'too', 5]

# path = ["/home", "ian", "work", "ian-lecture"]
# print("/".join(path))
# time = ["13", "20", "30"]
# print(":".join(time))

# twice = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# if "채영" in twice:
#     print("채영은 트와이스 입니다.")
# if "채령" not in twice:
#     print("채령 is not twice")

# tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
# print("sort", tottenham.sort())
# print("sort result", tottenham)


# tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
# tottenham.sort()
# print("line up", tottenham)
# tottenham.remove("Moura") #remove
# print("remove moura", tottenham)
# tottenham.insert(1, "Son")
# print("Son in", tottenham)

# #pop : 입력이 없으면 마지막 원소를 삭제.
# print("pop Alli", tottenham.pop(0))
# print("pop Alli : ", tottenham)
# del tottenham[3]
# print("del rose : ", tottenham)

# #append : 맨 뒤에 추가
# tottenham.append('Davies')
# tottenham.append('Llorente')
# print("append", tottenham)

# #reverse : 순서를 거꾸로 뒤집는다. in-place 함수
# tottenham.reverse()
# print("reverse : ", tottenham)

# wdgirls_debut = ["선예", "예은", "소희", "현아", "선미"]

# wdgirls_debut.pop(0)
# wdgirls_debut.pop(1)
# wdgirls_debut.remove("현아")

# wdgirls_debut.append("유빈")
# wdgirls_debut.insert(3, "혜림")
# print(wdgirls_debut)


# => wdgirls_final = ["예은", "선미", "유빈", "혜림"]

# tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
# for member in tottenham:
#     print("member : ", member)

# tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
# for member in tottenham:
#     print("member : ", member)
#     print("initial : ", member[0])


# tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
# print("type : ", type(tottenham))
# tottenham = iter(tottenham)
# print("type : ", type(tottenham))
# #iter 면 next 쓸 수 있다.
# print("0", next(tottenham))
# print("1", next(tottenham))
# print("2", next(tottenham))



# numbers = [1,2,3,4,5]
# for a in numbers:
#     print(f"square of {a} = {a**2}")


# pooh = {"species" : "bear", "age" : 5, "weight" : 50}
# tigger = {"species" : "tiger", "age" : 4, "weight" : 40}
# print("pooh's species is ", pooh["species"])
# print("pooh's weight is ", pooh["weight"])
# print("tiger's age is ", tigger["age"])


# pooh = {"species": "bear", "age": 5, "weight": 50}
# print("pooh's age", pooh["age"])
# pooh["age"] = 10
# print("pooh's age", pooh["age"])
# pooh["height"] = 1.2
# print(pooh)
# del pooh["weight"]
# print(pooh)

# print(pooh["ace"])


# pooh = {"species": "bear", "age": 5, "weight": 50}

# try: 
#     print("pooh's color", pooh["color"])
# except KeyError as ke:
#     print("key error", ke)

# if "color" in pooh:
#     print("pooh's color", pooh["color"])
# else:
#     print("pooh has no color")


# scores = {"pooh": 80, "tigger": 70, "piglet": 90, "rabbit": 85}
# print("names:", scores.keys())
# print("scores:", scores.values())
# print("items:", scores.items())

# print("names:", list(scores.keys()))
# print("scores:", list(scores.values()))
# print("items:", list(scores.items()))

# scores = {"pooh": 80, "tigger": 70, "piglet": 90, "rabbit": 85}

# for name in scores:
#     print("name : ", name, "value : ", scores[name])

# for val in scores.keys():
#     print("name : ", val)

# for val in scores.values():
#     print("score : ", val)

# for val in scores.items():
#     print("name:score : ", val)

# for name, score in scores.items():
#     print("name:score : ", name, ":", score)



# basic_tuple1 = ("Hello", 1234, 1.234, True)
# basic_tuple2 = "Hello", 1234, 1.234, True
# depth2_tuple = ("Hello", 1234, (1.234, True))

# print(basic_tuple1[0])
# print(basic_tuple1[2:])



# entrance_order = ["k3", "aventador", "k3", "a6", "cayenne", "a6"]
# car_set = set(entrance_order)
# print("car set : ", car_set)
# car_list = list(car_set)
# print("car list : ", car_list)
# print(car_list[2:])

# large_comps = {"samsung", "hyundai", "lg", "sk"}
# motor_comps = {"hyundai", "kia", "gm"}

# print("intersection : ", large_comps & motor_comps)
# print("intersection : ", large_comps.intersection(motor_comps))

# print("union : ", large_comps | motor_comps)
# print("union : ", large_comps.union(motor_comps))

# print("diff : ", large_comps - motor_comps)
# print("diff : ", large_comps.difference(motor_comps))

marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

myhero = "batman"
if myhero in marvel_heroes:
    print("batman in marver")
elif myhero in dc_heroes:
    print("batman in dc")
else:
    print("villlain")

for hero in marvel_heroes:
    print("marvel : ", hero)

i=0
while i < len(dc_heroes) and dc_heroes[i].endswith('man'):
    print(f"     {dc_heroes[i]}")
    i+=1