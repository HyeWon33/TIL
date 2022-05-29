파이썬에서 for문 많이 돌면 안 좋다. C언어는 상관 없는데 파이썬은 반복 많이하면 느려진다. 함수를 사용해라.

커널 크게 잡으면 넓게 잡고 효과 커진다.



### 2.4 Bilateral Filter

컬러 비슷한 영역 -> 스무딩

컬러 다른 영역 평균 낼 때 가중치 적게 준다.







## 3. Edge Detection

- 이미지 좌표계

  - ![이미지_좌표계](C:\Users\hjw14\Desktop\TIL\SYSTEMPROGRAM\이미지_좌표계.png)

  

  

### 3.1 1차 미분 필터

- 합이 0이여야 한다. +가 있으면 -가 있어야 한다.

- 소벨 엣지 Sobel edge
  - 양 옆에 있는 6개의 픽셀에 대해 차이를 구한다.
- 샤르 엣지 Scharr edge
  - 엣지의 방향성의 정확도 개선한 필터이다.
- 합이 0이 되게 하면 엣지 추출..





### 3.2 2차 미분 필터

- 라플라시안 필터
- 소벨 엣지보다 얇은 엣지 구할 수 있다.





### 3.3 캐니 엣지

- 유용하고 좋은 필터이다.
- 위에서는 엣지가 끊어지는 경우가 있다. 그래서 영사처리가 힘들 때도 있는데 캐니 엣지는 가급적이면 엣지를 잘 끊어지지 않게 신경쓴 거다잉.
- 노이즈 제거 -> 소벨 엣지 적용 -> 엣지가 두줄 세줄일 때 강한 한 줄만 남기고 다 제거 -> Hysteresis Thresholding(끊어지지 않게 해주는 것.)  Min보다 크면 Max를 그냥 예속 이어준다....강한 엣지와 연결된 약간 엣지를 살려줘잉 근데 Min아래로 내려가면 끊어지는겨~
- threshold1, threshold2 가 Min, Max





## 4. Mophology

침식과 팽창연산이 있다.

### 4.1 Erosion and Dilation

침식erosion -> 밝은 영역을 깎는 연산

팽창dilation -> 밝은 영역 확장 연산

### 4.2 Opening and Closing

나는 노이즈만 없애고 싶은데 글씨 크기도 달라져 이걸 유지하려면~

열림연산 : 침식 연산 -> 팽창 연산

닫힘 연산 : 팽창 연산 -> 침식 연산





#### 프로젝트

> 영상에서 사람이 인식할 수 있는 무언가 객체를 찾아보는 것. 영상에 동전 뿌려놓으면 동전 찾기, 차선 찾기, 공의 개수 세기, 뭐 이런거 해보기



# Segmentation

## 1. Hough Transform

**허프 공간(Hough Space)** : 찾고자 하는 도형의 파라미터 공간(Parameter Space)





### 1.1 Hough Line Transform

영상에서 직선 찾기



lines = **cv2.HoughLines**(image, rho, theta, threshold[, lines, srn, stn, min_theta, max_theta])

- image: 8-bit, single channel binary source image. 주로 원본 영상에 **가우시안 블러와 캐니 엣지**를 적용한 영상을 입력 영상으로 쓴다.
- rho, theta 너무 크거나 너무 작게 잡으면 좋지 않다.
- 3차원 shape으로 나온다.



**cv2.HoughLinesP**

- 더 빠르다
- 검출 결과 다르다.
- 시작점과 끝점 좌표 표현 (x1,y1,x2,y2)
- minLineLength : 선분의 최소 길이
- maxLineGap : 거리 사이 
- 주의할 점은 크기가 (Nx4)가 아니라 (Nx1x4)라는 것이다.







