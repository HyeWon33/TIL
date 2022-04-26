# marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
# dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
# all_heros = marvel_heroes + dc_heroes

# for hero in marvel_heroes:
#     if hero.startswith("spider"):
#         print("  Peter Parker ... ")
#         continue
#     if hero.startswith("capt"):
#         print(" One Captain is enough ... ")
#         break
#     print(f"  {hero} is cool")

# name = None
# print("Press 'q' to quit")
# while name != 'q':
#     print("type dc hero's name")
#     name = input()
#     if name == 'q':
#         break
#     if name not in dc_heroes:
#         print(f"{name} is not dc hero")
#         continue
#     index = dc_heroes.index(name)
#     print(f"{name}'s index = ", index)


# marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
# dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
# all_heros = marvel_heroes + dc_heroes

# print(list(enumerate(marvel_heroes)))

# # for elen in enumerate(marvel_heroes):
# #     i, name = elen
# #     print(i, name)

# for i, name in enumerate(marvel_heroes):
#     print(i, name)

# print(list(zip(marvel_heroes, dc_heroes)))
# # [('iron man', 'batman'), ('thor', 'superman'), ('hulk', 'aquaman'), ('spider man', 'wonder woman'), ('black widow', 'harley quinn')]

# for marvel, dc in zip(marvel_heroes, dc_heroes):
#     print(marvel, dc)

# for index, name in enumerate(marvel_heroes):
#     if index >= 3:
#         break
#     print("marvel hero : ", index, name)

# for mv, dc in zip(marvel_heroes, dc_heroes):
#     print(f"{mv} vs {dc}")

# print(list(enumerate(zip(marvel_heroes, dc_heroes))))
# #구조화된 튜플로 받아야 사용 가능
# for ind, (mv, dc) in enumerate(zip(marvel_heroes, dc_heroes)):
#     if ind >= 3:
#         break
#     if ind%2 == 1:
#         print(f"{mv} vs {dc} : {mv} win!")
#     else:
#         print(f"{mv} vs {dc} : {dc} win!")


# marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
# dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
# all_heros = marvel_heroes + dc_heroes

# super_heros = []
# for hero in marvel_heroes:
#     super_heros.append(hero + "_super")
# print("super heroes", super_heros)

# #man으로 끝나는거 모은다.
# man_heros = []
# for hero in marvel_heroes:
#     if hero.endswith("man"):
#         man_heros.append(hero)
# print("man heroes", man_heros)
# #너무 길어. 한 줄로 줄이는게 list comprehension

# super_heros_v2 = [hero + "_super " for hero in marvel_heroes]
# #대괄호로 리스트 만드는데 원소들 하나씩 안 써주고 for문으로 넣는다.
# #hero + "_super " <= 새로운 원소 들어가는거...?
# print("super horoes", super_heros_v2)


# man_heros_v2 = [hero for hero in marvel_heroes if hero.endswith("man")]
# print("man heroes v2 : ", man_heros_v2)

# int_square = [i**2 for i in range(10)]
# print(int_square)

# marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
# dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
# abilities = ["suit", "Mjölnir", "physical power", "spider web"]

# heroes = {name: power for nmae, power in zip(marvel_heroes)}
# print("heroes abbility : ", heroes)

# heroes_v2 = dict(zip(marvel_heroes, abilities))
# print("heroes abilities v2 : ", heroes_v2)


# def add(n1, n2):
#     return n1+n2

# print(add(10, 20))
# print(add(3, 7))



# def average_list(data, start, end, skip, verbose):
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
#     if verbose:
#         print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

#     return average

# data = list(range(10))
# print(average_list(data, 1, 8, [5], True))


# def average_list(data, start, end, skip, verbose):
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
#     if verbose:
#         print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

#     return average

# def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
#     if skip is None:
#         skip = []
#     return average_list(data, start, end, skip, verbose)

# data = list(range(10))
# avg = average_list_with_default(data)
# avg = average_list_with_default(data, 5)
# avg = average_list_with_default(data, end = 5)
# avg = average_list_with_default(data, skip=[3, 4])



# def add_op(list1, list2, start=0, shortlen=True, verbose=False):
#     if shortlen is True:
#         if len(list1) > len(list2):

#     else:
#         print()
    
#     if len(list1) > len(list2):
#         s = len(list2)
#     elif len(list1) == len(list2):
#         s = len(list1)



#     if verbose is True:
#         print()
#     else:
#         return 

# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7]

# add_op(list1, list2)


# def sum_list(list1k list2, shortlen, start=0, verbose=True):
#     list1 = list1[start:]
#     list2 = list2[start:]
#     if shortlen is False:
#         # if len(list1)

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

# subject_scores = {"cpp": [57, 36, 80], "java": [46, 88, 72], "ruby": [85, 23, 34]}

# def average_multi_subjects(scores, *args):
#     averages = {}
#     print("args", args) #튜플이 프린트
#     print("*args", *args) #언팩. 튜플로 묶여있는 것을 여러 개로 풀어헤치는 것.

# result = average_multi_subjects(subject_scores, "cpp")
# result = average_multi_subjects(subject_scores, "cpp", "java", "ruby")


# subject_scores = {"cpp": [57, 36, 80], "java": [46, 88, 72], "ruby": [85, 23, 34]}

# def average_list(data, start, end, skip, verbose):
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
#     if verbose:
#         print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")

#     return average

# def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
#     if skip is None:
#         skip = []
#     return average_list(data, start, end, skip, verbose)
# def average_multi_subjects(scores, *args):
#     averages = {}
#     print("args", args) 
#     print("*args", *args) 
#     for subject in args:
#         avg = average_list_with_default(scores[subject])
#         avg = average_list_with_default(scores[subject], verbose=False)
#         print(f"average over {subject} scores: {avg:.1f}")
#         averages[subject] = avg
#     return averages

# result = average_multi_subjects(subject_scores, "cpp")
# print("result : ", result)
# result = average_multi_subjects(subject_scores, "cpp", "java", "ruby")
# print("result : ", result)










# def average_list(data, start, end, skip, verbose):
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
#     if verbose:
#         print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")
#     return average
# def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
#     if skip is None:
#         skip = []
#     return average_list(data, start, end, skip, verbose)
# def average_multi_subjects(scores, *args):
#     averages = {}
#     print("args", args) 
#     print("*args", *args) 
#     for subject in args:
#         avg = average_list_with_default(scores[subject])
#         avg = average_list_with_default(scores[subject], verbose=False)
#         print(f"average over {subject} scores: {avg:.1f}")
#         averages[subject] = avg
#     return averages

# def average_variable_arguments(data, multiple, *args):
#     data = [d*multiple for d in data]
#     avg = average_list_with_default(data, *args)
#     return avg

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = average_variable_arguments(data, 10, 1, 7)
# print("average_variable_arguments(data, 10, 1, 7) =>", result)
# result = average_variable_arguments(data, 10, 1, 7, [3], False)
# print("average_variable_arguments(data, 10, 1, 7, [3], True) =>", result)
# result = average_list_with_default(data, 1, 7)
# print("average_list_with_default(data, 1, 7) =>", result)
# result = average_list_with_default(data, 1, 7, [3], False)
# print("average_list_with_default(data, 1, 7, [3], True) =>", result)





# def average_list(data, start, end, skip, verbose):
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
#     if verbose:
#         print(f"average over indices [{start}~{end}] with skipping index {skip} = {average}")
#     return average
# def average_list_with_default(data, start=0, end=None, skip=[], verbose=False):
#     if skip is None:
#         skip = []
#     return average_list(data, start, end, skip, verbose)


# # def average_keyworded_args(data, multiple, **kwargs):
# #     print("kwargs", kwargs)
# #     # print("**kwargs", **kwargs)
# #     data = [d*multiple for d in data]
# #     avg = average_list_with_default(data, **kwargs)
# #     return avg

# # data = [1,2,3,4,5,6,7,8,9]
# # result = average_keyworded_args(data, 10, start=1, skip=[2, 3], verbose=True)

# def average_keyworded_args(data, multiple, *args, **kwargs):
#     print("args", args)
#     print("kwargs", kwargs)
#     data = [d*multiple for d in data]
#     avg = average_list_with_default(data, *args, **kwargs)
#     return avg

# data = [1,2,3,4,5,6,7,8,9]
# result = average_keyworded_args(data, 10, 1, skip=[2, 3])





def main():
    print("main")

if __name__ == "__main__":
    main()