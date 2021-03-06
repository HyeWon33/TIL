# 2장 로봇 운영체제 ROS

## 2.1 ROS 소개

**로봇 운영체제**(ROS,Robot Operating System)는 로봇 응용 프로그램을 개발할 때 필요한 하드웨어 추상화, 하위 디바이스 제어, 일반적으로 사용되는 기능의 구현, 프로세스간의 메시지 패싱, 패키지 관리, 개발환경에 필요한 라이브러리와 다양한 개발 및 디버깅 도구를 제공한다. ROS는 로봇 응용 프로그램 개발을 위한 운영체제와 같은 로봇 플랫폼이다. 하드웨어 플랫폼을 하드웨어 추상화로 포함하고 있으며, 로봇 응용 소프트웨어 개발을 지원을 위한 소프트웨어 플랫폼이면서 이기종의 하드웨어에서 사용 가능한 운영 체제와 같은 기능을 갖추고 있다. _위키백과



## 2.2 메타 운영체제 (Meta-Operating System)

- 애플리케이션과 분산 컴퓨팅 자원 간의 가상화 레이어로 분산 컴퓨팅 자원을 활요앟여 스케줄링 및 로드, 감시, 에러 처리 등을 실행하는 시스템
- 미들웨어(Middleware), 소프트웨어 프레임워크(software framework)
- 기존은 전통적인 운영체제를 이용하면서, 로봇 응용프로그램 개발에 필수인 로봇과 센서를 하드웨어 추상화 개넘으로 제어하고, 사용자의 로봇 응용프로그램 개발을 위한 지원 시스템.



## 2.3 ROS의 목적

- ROS는 로보틱스 연구, 개발에서의 코드 재사용을 극대화하는 것에 초점이 잡혀있다.
  - 분산 프로세스 : 최소 단위의 실행 가능한 프로세스(노드, Node) 형태로 프로그램하며, 각 포르세스는 독립적으로 실행되면서 유기적으로 데이터를 주고 받는다.
  - 패키지 단위 관리 : 같은 목적을 갖는 복수 개의 프로세스를 패키지 단위로 관리하기 때문에 개발은 물론 사용하기에도 편하고 공유 및 수정 후 재배포도 쉽다.
  - 공개 리포지토리 : 각 패키지는 개발자가 선호하는 공개 리포지토리(예. github) 등에 패키지를 공개하고 각 라이선스도 밝히게 되어 있다.
  - API 형태 : ROS를 활용한 프로그램을 개발할 때 ROS는 단순히 API를 불러와 자신이 사용하던 코드에 쉽게 삽입할 수 있도록 설계되었다. 각 장에 소개된 소스 코드를 보면 ROS 프로그래밍과 C++, Python 프로그램이 별반 다를 게 없다는 것을 알게될 것이다.
  - 복수의 프로그래밍 언어 지원 : ROS 프로그램은 다양한 언어를 지원하기 위해 클라이언트 라이브러리(Client Library)를 제공한다. 즉 익숙한 언어를 사용해 ROS 프로그램을 개발하면 된다.



## 2.6 ROS의 역사, 2.7 ROS 버전

- 2007년 스탠퍼드 대학 인공지능 연구소(AILAB)에서 Switchyard로 시작된 로봇 소프트웨어 프레임워크 연구를 윌로우 개러지(Willow Garage)가 이어받아 ROS(Robot Operating System)라는 이름으로 개발을 이어갔다.
- 그 뒤 오픈 소스 로봇 공학 재단인 OSRF(Open Source Robotics Foundation)로 이양.
- 2017년부터 오픈 로보틱스(Open Robotics)라는 이름으로 바뀌어 ROS를 개발, 운영, 관리.

### 2.7.1 버전 규칙

- ROS는 1.0 버전을 제외하고는 우분투와 안드로이드처럼 버전명을 알파벳 순서로 짓고 있다.
- ROS의 상징으로 거북이를 사용한 이유는 1960년대에 MIT의 인공지능연구소에서 교육용 프로그래밍으로 나온 로고(Logo)의 영향이 크다.

### 2.7.2 버전 주기

- 1년에 1번 정식 버전을 릴리즈
- 5월 23일은 세계 거북이의 날
- 2년에 한 번씩 릴리즈 되는 우분투 LTS(Long Term Support) 버전에 맞추어 나오는 ROS 버전ㅇ들은 LTS 서비스가 종료되는 5년간 지원하게 된다.
  - 2016의 우분투 16.04LTS를 지원하는 ROS 버전인 ROS Kinetic Kame 버전은 2021년 5월까지 지원.

  

  

  

표윤석, 조한철, 정려운, 임태훈. 『ROS 로봇 프로그래밍』  
https://book.naver.com/bookdb/book_detail.nhn?bid=12443870