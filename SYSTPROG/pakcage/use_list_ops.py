# import list_ops

# foo = [1, 2, 3, 4, 5]
# bar = [24, 52, 13, 27]
# print(f"{foo} + {bar} = {list_ops.add(foo, bar)}")

# print(f"ham : {list_ops.ham}")
# # print(f"eggs : {list_ops.eggs}") #에러
# print(f"{list_ops.ham} * {list_ops.ham} =" f"{list_ops.multiply(list_ops.ham, list_ops.spam)}")



#모듈 이름 짧게 변경
# import list_ops as lo

# foo = [1, 2, 3, 4, 5]
# bar = [24, 52, 13, 27]

# goo = lo.subtract(foo, bar)
# print(f"{foo} - {bar} = {goo}")


from list_ops import add, subtract, spam

foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]

goo = add(foo, bar)
print("{} + {} = {}".format(foo, bar, goo))
goo = subtract(bar, foo)
print("{} - {} = {}".format(bar, foo, goo))
print("spam = {}".format(spam))