# import sys

# print(sys.path)



import sys
# new_path = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/pakcage"
# sys.path.append(new_path)

# import list_ops
# print(list_ops.spam)



# import os
# import shutil
# tempdir = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir"
# tempfile1 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile1.txt"
# tempfile2 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile2.txt"

# def create():
#     os.mkdir(tempdir)
#     try:
#         os.mkdir(tempdir)
#     except FileExistsError as e:
#         print(e)

#     with open(tempfile1, "w") as f:
#         f.write("blurblur 1")

#     with open(tempfile2, "w") as f:
#         f.write("blurblur 2")
    
#     print("create two files")

#     #파일 이동
#     # shutil.move(tempfile1, tempfile1.replace("/tempdir", ""))
#     # shutil.move(tempfile2, tempfile2.replace("tempfile2", "tf2"))
    


# def delete():
#     os.remove(tempfile1)
#     try:
#         os.remove(tempfile1)
#     except FileNotFoundError as e:
#         print(e)
    
#     shutil.rmtree(tempdir)
#     try:
#         shutil.retree(tempdir)
#     except FileNotFoundError as e:
#         print(e)

#     shutil.rmtree(tempdir, ignore_errors=True)
#     print("delete tempdir")

# if __name__ == "__main__":
#     create()
#     # delete()



# import os
# import shutil
# tempdir = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir"
# tempfile1 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile1.txt"
# tempfile2 = "C:/Users/hjw14/Desktop/TIL/SYSTPROG/tempdir/tempfile2.txt"
# os.mkdir(tempdir)

# if os.path.isfile(tempfile1):
#     print(f"{tempfile1} exists. remove it now")
#     os.remove(tempfile1)
# else:
#     print(f"{tempfile1} does NOT exists")

# if os.path.isdir(tempdir):
#     print(f"{tempdir} exists. remove it now")
#     shutil.rmtree(tempdir)
# else:
#     print(f"{tempdir} does NOT exists")



# import os
# curfile = __file__
# curfile = os.path.abspath(curfile) #경로 받았다
# print([curfile]) 

# filename = os.path.basename(curfile) #파일 이름.
# print("file name : ", filename)

# pathname = os.path.dirname(curfile)
# print("dir name : ", pathname)

# #경로와 파일명 합치기
# newfile = os.path.join(pathname, "newfile.txt")
# print("new file path : ", newfile)
# with open(newfile, "w") as f:
#     f.write("new file")

# newpath = os.path.join(pathname, "new", "path", "name")
# print("new path : ", newpath)



# import os
# import glob
# curfile = os.path.abspath(__file__)
# curdirpath = os.path.dirname(curfile)
# files = os.listdir(curdirpath)
# print("file list : ", files)

# search_pattern = os.path.join(curdirpath, "*") #전체 다
# print("search pattern : ", search_pattern)
# fileList = glob.glob(search_pattern)
# print("file list : ", fileList)

# search_pattern = os.path.join(curdirpath, ".py") #.py로 끝나는거 
# print("search pattern : ", search_pattern)
# pyfileList = glob.glob(search_pattern)
# print(".py file list : ", pyfileList)

# filess = [file for file in fileList if os.path.isfile(file)]
# dirss = [file for file in fileList if os.path.isdir(file)]

# print("file liset : ", filess)
# print("dir list : ", dirss)


#경로명을 없앤 새로운 file list
# import os
# import glob
# curfile = os.path.abspath(__file__)
# curdirpath = os.path.dirname(curfile)
# files = os.listdir(curdirpath)
# print("file list : ", files)

# search_pattern = os.path.join(curdirpath, "*") #전체 다
# print("search pattern : ", search_pattern)
# fileList = glob.glob(search_pattern)
# print("file list : ", fileList)

# search_pattern = os.path.join(curdirpath, ".py") #.py로 끝나는거 
# print("search pattern : ", search_pattern)
# pyfileList = glob.glob(search_pattern)
# print(".py file list : ", pyfileList)

# filess = [os.path.basename(file) for file in fileList if os.path.isfile(file)]
# dirss = [os.path.basename(file) for file in fileList if os.path.isdir(file)]

# print("file liset : ", filess)
# print("dir list : ", dirss)


# import numpy as np

# array1d = [1, 2, 3, 4]
# array2d = [[1,2], [3, 4]]
# array3d = [[[1,2], [3,4]], 
#             [[5,6], [7, 8]]]
# print("array1d -> ", array1d)
# print("array1d : ", np.array(array1d, dtype=int))
# print("array2d -> ", array2d)
# print("array2d : \n", np.array(array2d, dtype=int))
# print("array3d -> ", array3d)
# print("array3d : \n", np.array(array3d, dtype=int))


#일정한 패턴 가진 행렬 만들고 싶다.
# print("ones\n", np.ones((2, 4))) #2,4를 하나의 튜플로 만들어서 넣어준다.
# print("zeros\n", np.zeros((3, 2))) #영행렬
# print("identity\n", np.identity(3)) #대각선만 1인거
# print("identity\n", np.eye(3)) #매틀랩에서 쓴다. 위랑 같은 함수다.
# print("linear space:", np.linspace(5, 10, 11)) #등차수열 5와 10사이 11개숫자 등간격으로 
# print("arange:", np.arange(5, 10, 0.5)) #간격 지정 lineapce와 다른 점은 arange는 끝에 10 안들어간다. 10미만까지 들어간다.
# print("permutation:\n", np.random.permutation(10)) #10개의 숫자를 랜덤하게 막 섞어준다. 0~9

# print("linear space:", np.linspace(5, 10, 11)) 
# print("arange:", np.arange(5, 10, 0.5)) 
# print("permutation:\n", np.random.permutation(10)) 
# array = np.linspace(5, 19, 11)
# indices = np.random.permutation(10)
# print("indices : ", indices)
# print(array[indices])


# import numpy as np

# print("uniform [0, 1)\n", np.random.rand(3, 4))
# print("normal distrivution 정규분포 [0, 1)\n", np.random.randn(5, 5))
# print("rand int \n", np.random.randint(0, 5, (2, 3)))


# import numpy as np

# foo = np.ones((3, 4, 2))
# print(foo.shape) # 각 ㅊ ㅏ원의 
# print(foo.ndim) #전체 차원수 출력


# import numpy as np

# foo = np.arange(0, 6)
# print("foo -> ", foo, foo.shape)
# print("foo (2,3)\n", foo.reshape(2, 3)) #원소가 6개인데 3X3하라고 하면 에러난다.
# print("foo (2,3)\n", foo.reshape(2, -1))
# foo3d = foo.reshape(2, 3, 1) #1은 가장 안 쪽에 원소1개짜리 배열이 들어있다...
# print("foo (2,3,1)\n", foo3d)
# print("foo (3,2)\n", foo3d.reshape(3, 2))

# '''
# 3X2   2X3
# 01
# 23     012
# 45     345
# '''

# print("foo (3,2)\n", foo3d.reshape(2, 3))



# import numpy as np

# data_list = [[[5, 6, 2], [3, 4, 9]], [[1, 7, 2], [3, 8, 0]]]
# data = np.array(data_list)
# print(data)
# print(data.shape)

# #list
# print("data_list[0] : \n", data_list[0])
# print("data_list[0][1] : \n", data_list[0][1])
# print("data_list[0][1][2] : \n", data_list[0][1][2])
# #numpy배열
# print("data[0] : \n", data[0])
# print("data[0][1] : \n", data[0][1])
# print("data[0][1][2] : \n", data[0][1][2])



#슬라이싱
#numpy 여러 차원 슬라이싱 가능하다.
# import numpy as np

# data_list = [[[5, 6, 2], [3, 4, 9]], [[1, 7, 2], [3, 8, 0]]]
# data = np.array(data_list)

# print(data)
# print(data[:, :, 1]) #1번원소들만 추출... 6478
# print(data[0, :, 1])
# print(data[0, :, 1:])
# print(data[:1, 1:, :])

#하나의 원소들만 가져오긴 했지만 슬라이싱으로 해서 차원이 사라지지 않았다.

# print(data[0, 1, :])
# print(data[:1, 1:, :])
#같지만 인덱싱 슬라이싱 차이...

# print(data[:3, :1, :1])

# data = np.random.randint(0, 10, (3, 4))
# print(data)

# print(data[:2, 2:])




# import numpy as np

# foo = np.array([[9, 3, 2], [1, 3, 9], [1, 6, 8]])
# bar = np.array([[1, 4, 2], [3, 3, 4], [2, 1, 3]])

# print("foo\n", foo)
# print("bar \n", bar)
# print("foo - bar \n", foo - bar)
# print("foo * bar \n", foo * bar) #행렬곱이 아니다.
# print("foo ** bar \n", foo ** bar)
# print("foo @ bar \n", foo @ bar) #행렬곱?



import numpy as np

foo = np.array([[9, 3, 2], [1, 3, 9], [1, 6, 8]])
bar = np.array([[1, 4, 2], [3, 3, 4], [2, 1, 3]])

print("foo\n", foo)
print("bar \n", bar)

print("foo > bar \n", foo > bar)
print("foo[foo > bar] \n", foo[foo > bar]) #일차원 배열로 나올 수 밖에 없다...
print("foo[bar < 3] \n", foo[bar < 3]) #bar가 3보다 작은 위치에 있는 foo를 찾는다.








