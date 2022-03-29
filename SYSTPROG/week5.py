# class Dog:
#     def __init__(self, name): #__init__ : 생성자 함수. return 불가능.
#         self.name = name	#self는 c++에서 this. 반드시 self 붙여야 한다. self말고 다른 이름 써도 괜찮긴하다.
#         self.position = 0 
#         #멤버 변수 init 함수 내에서만 생성해주는 것이 좋다.

#     def bark(self):
#         print(f"{self.name}: Wal! Wal!")

#     def move(self, distance):
#         self.position += distance
#         print(f"{self.name} is at {self.position}")

# def main():
#     puppy = Dog("dangdang")
#     puppy.bark()	
#     puppy.move(10)	
#     print("current position:", puppy.position)

# if __name__ == "__main__":
#     main()


# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def introduce(self):
#         print("my name is", self.name)
        
#     def sound(self):
#         print("...")
        
        
# class Cow(Animal): #상속. 파이썬은 접근지정자가 없다.
#     def __init__(self, name):
#         super().__init__(name)
        
#     def sound(self):
#         print("ummer~~~")
        
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
        
#     def sound(self):
#         print("nyaong~~")

# def main():
#     cow = Cow("cow1")
#     cow.introduce()
#     cow.sound()
#     animals = [Animal("ani"), Cow("cow2"), Cat("cat")]
#     for i, ani in enumerate(animals):
#         print("index : ", i)
#         ani.introduce()
#         ani.sound()

# if __name__ == "__main__":
#     main()



# 함수 사이 1칸 클래스 사이 2칸 클래스 내부 함수 사이 1칸 밖 함수는 2칸 뛰어잇




# fout = open("testfile.txt", "w")
# fout.write("I think.")
# fout.close()
# # print("file was written")

# fin = open("testfile.txt", "r")
# contents = fin.read()
# fin.close()
# print(contents)


# try:
#     f = open("nofile.txt", "r")
# except FileNotFoundError as fe:
#     print(fe)


# fr = open("testfile.txt", "r")
# fr.read()
# fr.close()

# with open("testfile.txt", "r") as fr:
#     data = fr.read()
#     print("check closed : ", fr.closed)

# print("outside context manager")
# # data = fr.read()
# print("check closed : ", fr.closed)


# class File:
#     def __enter__(self):
#         pass

#     def __excit__(self, exc_type, exc_val, exc_tb):
#         pass


# with open으로 객체 열고 닫지 않으면 자동으로 파일 닫기가 된다.



# springx3 = ["봄 봄 봄 봄이 왔네요",
#             "우리가 처음 만났던 그때의 향기 그대로",
#             "그대가 앉아 있었던 그 벤치 옆에 나무도 아직도 남아있네요",
#             "살아가다 보면 잊혀질 거라 했지만",
#             "그 말을 하면 안될거란걸 알고 있었소",
#             "그대여 너를 처음 본 순간 나는 바로 알았지",
#             "그대여 나와 함께 해주오 이 봄이 가기 전에"]

# print("\nwrite lyrics into file")
# with open("springx3.txt", "w") as f:
#     for i, line in enumerate(springx3):
#         f.write(f"{i:2}:" + line + "\n")


#springx3.txt 위치 바꾸고 싶다.
# print("use read")
# with open("springx3.txt", "r") as f:
#     lyrics = f.read()
#     print(lyrics)

# print("use readline")
# with open("springx3.txt", "r") as f:
#     lyrics = []
#     line = f.readline()
#     while line:
#         line = line.rstrip("\n")
#         lyrics.append(line)
#         line = f.readline()
# print("\n".join(lyrics))

# print("use readlines")
# with open("springx3.txt", "r") as f:
#     lyrics = f.readlines()
#     lyrics = [line.rstrip("\n") for line in lyrics]
#     print("\n".join(lyrics))



# with open("matrix.txt", "w") as fw:
#     matrix_str = "4 2\n5 3"

# matrix = []

# with open("matrix.txt", "w") as f:
#     for i, line in enumerate(matrix_str):
#         print(i, line)
#         matrix = matrix_str.split(" ")

# # matrix[[4, 2], [5, 3]]
# #      0,0  0,1  1,0   1,1

# # print("read matrix : ", matrix)



# matrix_str = "4 2\n5 3"
# with open("matrix.txt", "w") as f:
#     f.write(matrix_str)

# with open("matrix.txt", "r") as f:
#     data = f.readlines()

# data = [d.rstrip("\n") for d in data]
# data = [d.split() for d in data]

# data = [[int(elem) for elem in row] for row in data]
# # ↓↓
# # numdata = []
# # for row in data:
# #     numrow = [int(elem) for elem in row]
# #     numdata.append(numrow)

# print(data)

# determinant = data[0][0] * data[1][1] - data[0][1] * data[1][0]
    
# print("determinant : ", determinant)

