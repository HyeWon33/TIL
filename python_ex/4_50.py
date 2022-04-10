## 051 리스트 생성

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)



## 052 리스트에 원소 추가

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)



## 053 중간에 추가

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)



## 054 삭제

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove("럭키")
# print(movie_rank)

# # 정답
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)



## 055 두 개 삭제

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# movie_rank.remove("스플릿")
# movie_rank.remove("배트맨")
# print(movie_rank)

# # 정답
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)



## 056 리스트 합치기

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# lang3 = lang1 + lang2
# print(lang3)



## 057 리스트 최댓값 최솟값을 출력 ***********

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max : ", max(nums))
# print("min : ", min(nums))



## 058 리스트의 합 ************

# nums = [1, 2, 3, 4, 5]

# # 정답
# print(sum(nums))
# # sum이라는 함수도 있구나..



## 059 데이터 개수

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))



## 060 리스트 평균

# nums = [1, 2, 3, 4, 5]
# print(sum(nums) / len(nums))