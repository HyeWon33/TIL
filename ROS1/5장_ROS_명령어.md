# 5장 ROS 명령어

## 5.1 ROS 명령어 정리

- ROS는 쉘(shell) 환경에서 명령어를 입력하여 파일 시스템 이용, 소스 코드 편집, 빌드, 디버깅, 패키지 관리 등을 처리할 수 있다.

(중요도 높은거와 내가 자주 사용했던거 정리)

#### ROS 쉘 명령어

- roscd : 지정한 ROS패키지의 디렉터리로 이동

#### ROS 실행 명령어

- roscore : master(ROS 네임 서비스) + rosout(로그 기록) + parameter server(파라미터 관리)
- rosrun : 노드 실행
- roslaunch : 노드를 여러 개 실행 및 실행 옵션 설정

#### ROS 정보 명령어

- rostopic : ROS 토픽 정보 확인
- rosservice : ROS 서비스 정보 확인
- rosnode : ROS 노드 정보 확인
- rosparam : ROS 파라미터 정보 확인, 수정

#### ROS 캐킨 명령어

- catkin_create_pkg : 캐킨 빌드 시스템으로 패키지 자동 생성
- catkin_make : 캐킨 빌드 시스템에 기반을 둔 빌드

#### ROS 패키지 명령어

- rospack : ROS 패키지와 관련된 정보 보기



## 5.2 ROS 쉘 명령어

- roscd
- rosls
- rosed

### 5.2.1 roscd: ROS 디렉터리 이동

`` roscd [패키지 이름]``

- 패키지가 저장된 디렉터리로 이동하는 명령어이다.

### 5.2.2 rosls : ROS 파일 목록

`` rosls [패키지 이름] ``

- 지정한 ROS 패키지의 파일 목록을 확인하는 명령어이다.

### 5.2.3 rosed  : ROS 편집 명령어

`` rosed [패키지 이름] [파일 이름]``

- 패키지의 특정 파일을 편집할 때 사용하는 명령어이다.



## 5.3 ROS 실행 명령어

- roscore
- rosrun
- roslaunch 
- rosclean

### 5.3.1 roscore : roscore 실행

``roscore [옵션]``

- roscore를 실행하면 노드 간의 메시지 통신에서 연결 정보를 관리하는 마스터가 실행된다.
- 이는 ROS를 사용하기 위해서 제일 먼저 구동되야 하는 필수 요소이다.
- XMLRPC 서버로 구동하게 된다.

### 5.3.2. rosrun : ROS 노드 실행

``rosrun [패키지 이름] [노드 이름]``

- rosrun 은 지정한 패키지에서 하나의 노드를 실행하는 명령어이다.

### 5.3.3 roslaunch : ROS 노드 여럿 실행

``roslaunch [패키지 이름] [launch 파일 이름]``

- roslaunch는 지정한 패키지에서 하나 이상의 노드를 실행하거나 실행 옵션을 설정하는 명령어이다.

### 5.3.4 rosclean : ROS 로그 검사 및 삭제

``rosclean [옵션]``

- ROS 로그 파일을 검사하거나 삭제하는 명령어이다.
- roscore 구동과 함께 모든 노드에 대한 기록은 로그 파일로 기록되는데, 시간이 지날수록 데이터가 축적되므로 주기적으로 rosclean 명령어를 이용하여 삭제할 필요가 있다.



## 5.4 ROS 정보 명령어

토픽, 서비스, 노드, 파라미터 등의 정보를 확인하는 데 사용한다.

### 5.4.1 노드 실행

- 다음에 나오는 명령어들을 사용해 ROS에서 제공하는 turtlesim을 이용하여 관련 노드, 토픽, 서비스 등을 알아볼 것이다.
- roscore 실행
  - ``roscore``
- turtlesim 패키지의 turtlesim_node 노드 실행
  - ``rosrun turtlesim turtlesim_node``
- turtle 패키지의 turtle_teleop_key 노드 실행
  - ``rosrun turtlesim turtle_teleop_key``



### 5.4.2 rosnode : ROS 노드

#### rosnode list : 실행 중인 노드 목록 확인

- roscore에 연결된 모든 노드의 목록을 확인하는 명령어

#### rosnod ping [노드 이름] : 지정된 노드와 연결 테스트

- turtlesim 노드가 실제로 현재 사용 중인 컴퓨터와 연결되어 있는지를 테스트한 것이다.

#### rosnode info [노드 이름] : 지정딘 노드 정보 확인

- rosnode info 명령어를 이용하여 지정한 노드의 정보를 확인할 수 있다.

#### rosnode machine [PC 이름 또는 IP] : 해당 PC에서 실행되고 있는 노드 목록 확인

- 지정된 특정 기기(PC나 단말기)에서 작동 중인 노드의 목록을 확인할 수 있다.

#### rosnode kill [노드 이름] : 지정된 노드 실행 종료

- 실행 중인 노드를 종료하는 명령어이다.

#### rosnode cleanup : 연결 정보가 확인 안되는 유령 노드의 등록 정보 삭제

- 연결 정보가 확인되지 않는 유령 노드의 정보를 삭제한다.
- 예기치 못한 일로 노드가 비정상 종료되었을 때, 이 명령어로 연결 정보가 끊어진 노드를 목록에서 삭제한다.



### 5.4.3 rostopic : ROS 토픽

#### rostopic list : 활성화된 토픽 목록 표시

- 현재 송수신되고 있는 모든 토픽의 목록을 확인할 수 있다.
- '-v' 옵션을 추가하면, 퍼블리시 토픽과 서브스크라이브 토픽을 나눠서 보여 주고, 각 토픽의 메시지 타입까지 함께 표시한다.

#### rostopic echo [토픽 이름] : 지정된 토픽의 메시지 내용 실시간 표시

ex : ``rostopic echo /turtle1/pose``

#### rostopic find [토픽 이름] : 지정한 타입의 메시지를 사용하는 토픽 표시

#### rostopic type [토픽 이름] : 지정한 토픽의 메시지 타입 표시

#### rostopic bw [토픽 이름] : 지정한 토픽의 메시지 데이터 대역폭(bandwidth) 표시

#### rostopic hz [토픽 이름] : 지정한 토픽의 메시지 데이터 퍼블리시 주기 표시

#### rostopic info [토픽 이름] : 지정한 토픽의 정보 표시

#### rostopic pub [토픽 이름] [메시지 타입] [파라미터] : 지정한 토픽 이름으로 메시지 퍼블리시



### 5.4.4 rosservice : ROS 서비스

#### rosservice list : 활성화된 서비스 정보 출력

- 활성화된 서비스에 대한 정보를 출력한다. 같은 네트워크에서 사용 중인 서비스가 모두 표시된다.

#### rosservice info [서비스 이름] : 지정한 서비스의 정보 표시

- rosservice의 info 옵션을 이용하여 /turtle1/set_pen 서비스의 노드 이름, URI, 타입, 파라미터들을 확인하는 예제.. 책에..

#### rosservice type [서비스 이름] : 서비스 타입 출력

#### rosservice find [서비스 타입] : 지정한 서비스 타입의 서비스 검색

#### rosservice uri [서비스 이름] : ROSRPC uri 서비스 출력

#### rosservice args [서비스 이름] : 서비스 파라미터 출력

#### rosservice call [서비스 이름] [파라미터] : 입력된 파라미터로 서비스 요청



### 5.4.5 rosparam : ROS 파라미터

#### rosparam list : 파라미터 목록 보기

- 같은 네트워크에서 사용 중인 파라미터 목록이 표시된다.

#### rosparam get [파라미터 이름] : 파리미터 값 불러오기

- 특정 파라미터 값을 확인하고 싶을 때는 rosparam get 명령어를 옵션으로 파라미터 이름을 적어주면 된다.
- 특정 파라미터가 아닌 모든 파라미터의 값을 확인하고 싶을 때에는 옵션으로 '/'를 붙여주면 된다.

#### rosparam dump [파일 이름] : 파라미터를 지정한 파일에 저장

#### rosparam set [파라미터 이름] : 파라미터 값 설정

#### rosparam load [파일 이름] : 파라미터를 지정한 파일에 저장

#### rosparam delete [파라미터 이름] : 파라미터 삭제



### 5.4.6 rosmsg : ROS 메시지 정보

#### rosmsg list : 모든 메시지 목록 표시

- 현재 ROS에 설치된 패키지의 모든 메시지를 목록으로 표시한다.

#### rosmsg show [메시지 이름] : 지정한 메시지 정보 표시

- 지정한 메시지 정보를 표시한다.

#### rosmsg md5 [메시지 이름] : md5sum을 표시

- md5 정보를 확인하는 예제이다.

#### rosmsg package [패키지 이름] : 지정한 패키지에서 사용되는 메시지 목록 표시

- 특정 패키지에서 사용되는 메시지들을 확인할 수 있다.

#### rosmsg packages : 메시지를 사용하는 모든 패키지 목록 표시



### 5.4.7 rossrv : ROS 서비스 정보

#### rossrv list : 모든 서비스 목록 표시

- 이 명령어는 현재 ROS에 설치된 패키지의 모든 서비스를 목적으로 표시한다.

#### rossrv show [서비스 이름] : 지정한 서비스 정보 표시

#### rossrv md5 [서비스 이름] : md5sum을 표시

#### rossrv package [패키지 이름] : 지정한 패키지에서 사용되는 서비스 목록 표시

- 지정 패키지에서 사용되는 서비스들을 확인할 수 있다.

#### rossrv packages : 서비스를 사용하는 모든 패키지 목록 표시



### 5.4.8 rosbag : ROS 로그 정보



## 5.5 ROS catkin 명령어

catkin 빌드 시스템을 사용하여 패키지를 빌드할 때 사용된다.

#### catkin_create_pkg : 패키지를 자동으로 생성

``catkin_create_pkg [패키지 이름] [의존성 패키지1] [의존성 패키지2]..``

#### catkin_make : 캐킨 빌드 시스템에 기반을 둔 빌드

- catkin_make는 사용자가 만든 패키지 또는 다운로드한 패키지를 빌드하는 명령어이다.
- 모든 패키지가 아닌 일부 패키지만 비륻하려면 '--package [패키지 이름]' 옵션을 지정하여 실행한다.
  - ``catkin_make --pkg user_ros_tutorials``

#### catkin_eclipse : 캐킨 빌드 시스템으로 생성한 패키지를 이클립스에서 사용할 수 있게 변경

- 통합개발환경(IDE) 중 하나인 이클립스(Eclipse)를 사용하여 사용자가 만든 패키지를 관리하고 프로그래밍하는 환경을 구축하는 명령어이다.

#### catkin_generate_changelog : CHANGELOG.rst 파일 생성

- 패키지의 버전을 업데이트할 때 변경 사항을 기술하는 CHANGELOG.rst 파일을 만드는 명령이다.

#### catkin_prepare_release : 릴리즈를 준비할 때 사용되는 변경 이력과 버전 태그 관리

- catkin_generate_changelog 명령으로 생성된 CHANGELOG.rst를 업데이트할 때 사용하는 명령이다.
- catkin_generate_changelog와 catkin_prepare_release 명령은 작성한 패키지를 공식 ROS 리포지토리에 등록할 때나, 등록된 패키지의 버전을 업데이트할 때 사용하는 명령어이다.

#### catkin_init_workspace : 캐킨 빌드 시스템의 작업 폴더의 초기화

- 사용자 작업 폴더(~/catkin_ws/src)의 초기화 명령어이다.
- 이 명령어는 특별한 경우를 제외하고는 ROS 설치 시에 단 한번 실행하게 된다.

#### catkin_find : 캐킨 검색, 작업 공간을 찾아서 표시

- 프로젝트별 작업 폴더를 표시하는 명령어이다.
- 사용하고 있는 모든 작업 폴더를 알아낼 수 있다.



## 5.6 ROS 패키지 명령어

패키지의 정보 표시 및 관련 패키지의 설치 등 ROS 패키지 조작에 사용한다.



#### rospack : 지정한 ROS 패키지의 관련 정보를 표시

``rospack [옵션] [패키지 이름]``

- 지정한 ROS 패키지와 관련한 저장 위치, 의존 관계, 전체 패키지 목록 등의 정보를 표시하는 명령어로 find, list, depends-on, depends, profile 등의 옵션을 사용할 수 있다.
- rospack find [패키지 이름] : 해당 패키지의 저장 위치가 표시된다.
- rospakc list : PC에 있는 모든 패키지를 표시하는 명령어이다.
  - grep을 조합하면 쉽게 패키지를 찾을 수 있다.
  - rospack list | grep turtle
- rospack depends-on [패키지 이름] : 지정한 패키지를 이용하는 패키지의 목록만 표시된다.
- rospack depends [패키지 이름] : 지정한 패키지의 실행에 필요한 의존성 패키지의 목록이 표시된다.
- rospack profile : 패키지가 저장되어 이는 'opt/ros/kinetic/share' 또는 '~/catkin_ws/src' 등의 작업 폴더 및 패키지의 정보를 확인하여 패키지 인덱스를 재구축하는 명령어이다.

#### rosinstall : ROS 추가 패키지 설치

SVN, Mercurial, Git, Bazaar 등의 소스 코드 매니지먼트(SCM)에서 관리하고 있는 ROS 패키지를 자동으로 설치 또는 업데이트하는 명령어이다.

#### rosdep : ROS 해당 패키지의 의존성 파일 설치

``rosdep [옵션]``

- 지정한 패키지의 의존 관계 파일을 설치하는 명령어이다.
- 옵션으로는 check, install, init, update
  - rosdep check [패키지 이름] : 지정한 패키지의 의존성을 확인한다.
  - rosdep install [패키지 이름] : 지정한 패키지의 의존 패키지가 설치된다.
  - rosdep init [패키지 이름] 
  - rosdep update [패키지 이름]

#### roslocate : ROS 패키지의 정보 표시

``roslocate [옵션] [패키지 이름]``

- roslocate는 패키지가 사용하고 있는 ROS 버전, SCM 종류, 리포지토리 위치 등 패키지 관련 정보를 표시하는 명령어이다. 옵션으로는 info, vcs, type, uri, repo

#### roscreate-pkg : ROS 패키지의 자동 생성(구 rosbuild 시스템에서 사용)

- catkin_create_pkg 명령어와 같이 패키지를 자동 생성하는 명령어이다.

#### rosmake : ROS 패키지를 빌드(구 rosbuild 시스템에서 사용)

- catkin_make 명령어와 같이 패키지를 빌드하는 명령어이다.





표윤석, 조한철, 정려운, 임태훈. 『ROS 로봇 프로그래밍』
https://book.naver.com/bookdb/book_detail.nhn?bid=12443870





