# 4장 ROS의 중요 콘셉트

## 4.1. ROS 용어 정리

#### ROS

- 로봇의 응용프로그램을 개발하기 위한 운영체제와 같은 로봇 소프트웨어 플랫폼이다.

#### 마스터 master

- 노드와 노드 사이의 연결과 메세지 통신을 위한 네임 서버와 같은 역할을 한다.
- roscore가 실행 명령어다.
- 마스터를  실행하면 각 노드의 이름을 등록하고 필요에 따라 정보를 받을 수 있다. 
- 마스터 없이는 노드 간의 접속, 토픽과 서비스 같은 메세지 통신을 할 수 없다.

#### 노드 Node

- ROS에서 실행되는 최소 단위의 프로세서를 지칭한다. 즉 하나의 실행 가능한 프로그램으로 생각하면 된다.
- ROS에서는 하나의 목적에 하나의 노드를 작성, 재사용 쉽게 구성하여 개발하기 권한다.
- 노드는 구동과 함께 마스터에 노드 이름과 publishser, subscriber, service server, service client에서 사용하는 토픽 및 서비스 이름, 메세지 형태. URI 주소와 포트를 등록한다. 이 정보들을 기반으로 각 노드는 노드끼리 토픽과 서비스를 이용하여 메세지를 주고받을 수 있다.

#### 패키지 package

- ROS를 구성하는 기본 단뒤이다.
- ROS의 응용프로그램은 패키지 단위로 개발되며 패키지는 최소한 하나 이상의 노드를 포함하거나 다른 패키지의 노드를 실행하기 위한 설정 파일들을 포함하게 된다.

#### 메타패키지 metapackage

- 공통된 목적을 지닌 패키지들의 집합
- 예) Navigation 메타패키지는 AMCL, DWA, EKF ... 등으로 구성되어 있다.

#### 메시지 message

- 노드는 message를 통해 노드 간의 데이터를 주고 받는다.
- 메시지는 interger, floating, point, boolean과 같은 변수 형태이다. 또한 메시지 안에 메시지를 품고 있는 간단한 데이터 구조나 메시지들이 나열된 배열과 같은 구조도 사용할 수 있다.
- 메시지를 이용한 통신 방법으로 단방향 메시지 송수신 방식의 topic, 양방향 메시지 request/response 방식의 service를 이용한다.

#### 토픽 topic

- 이야깃거리

-  publisher 노드가 하나의 이야깃거리에 대해서 토픽으로 마스터에 등록한 후, 이야깃서리에 대한 이야기를 메시지 형태로 퍼블리시 한다.
- 이 이야깃거리를 수신받기를 원하는 subscriber 노드는 마스터에 등록된 토픽의 이름에 해당하는 퍼블리셔 노드의 정보를 받는다.

#### 퍼블리시 및 퍼블리셔 publish/publisher

- publish는 토픽의 내용에 해당하는 메시지 형태의 데이터를 송신하는 것을 말한다.
- publisher 노드는 publish를 수행하기 위하여 토픽을 포함한 자신의 정보들을 마스터에 등록하고, subscribe를 원하는 subscribe 노드에 메시지를 보낸다.
- publisher는 이를 실행하는 개체로써 노드에서 선언한다. 그리고 하나의 노드에서 복수로 선언할 수 있다.

#### 서브스크라이브 및 서브스크라이버 subscribe/subscriber

- subscribe는 토픽의 내용에 해당하는 메시지 형태의 데이터를 수신하는 것을 말한다.
- subscriber 노드는 subscribe를 수행하기 위하여 토픽을 포함한 자신의 정보들을 마스터에 등록하고, 구독하고자 하는 토픽을 퍼블리시하는 퍼블리셔 노드의 정보를 마스터로부터 받는다.
- publish와 subscribe 개념의 토픽 방식은 비동기 방식이라 필요에 따라서 주어진 데이터를 전송하고 받기에 매우 훌륭한 방법이다.  
- 한 번의 접속으로 지속적인 메시지를 송수신하기 때문에 지속해서 메시지를 발송해야 하는 센서 데이터에 적합하여 많이 사용된다. 

#### 서비스 service

- 서비스 메시지 통신은 특정 목적의 작업에 해당되는 서비스를 요청하는 service client와 service response을 담당하는 service server간의 동기적 양방향 서비스 메시지 통신을 말한다.
- 토픽과는 달리 일회성 메시지 통신이다. 
- 서비스의 요청과 응답이 완료되면 연결된 두 노드의 접속은 끊긴다.

#### 서비스 서버 service server

- service server는 요청을 입력으로 받고, 응답을 출력으로 하는 서비스 메시지 통신의 서버 역할을 말한다.
- request와 response은 모두 메시지로 되어 있으며, 서비스 요청을 받으면 지정된 서비스를 수행한 다음 그 결과를 서비스 클라이언트에 전달한다.
- 서비스 서버는 정해진 명령을 받아 수행하는 노드에 사용된다.

#### 서비스 클라이언트 service client

- service client는 요청을 출력으로 하고, 응답을 입력으로 받는 서비스 메시지 통신의 클라이언트 역할을 말한다.
- request와 response는 모두 메시지로 되어 있으며, 서비스 요청을 서비스 서버에 전달하고 그 결괏값을 받는다. 서비스 클라이언트는 정해진 명령을 지시하고 결괏값을 받는 노드에 사용된다.

#### 액션 action

- action은 service처럼 양방향을 요구하나 요청 처리 후 응답까지 오랜 시간이 걸리고 중간 결괏값이 필요한 경우에 사용되는 메시지 통신 방식이다.
- action파일도 service와 비슷하게 요청과 응답에 해당되는 목표(goal)와 결과(result) 그리고 결과값에 해당되는 피드백(feedback)이 추가되었다.
- action client와 목표에 맞추어 정해진 일을 수행하고 액션 피드백과 결과를 전달하는 action server로 구성되어 있고 이들 간의 비동기식 양방향 메시지 통신을 수행한다.

#### 액션 서버 action server

- action server는 action client로부터 목표를 입력으로 받고, 결과 및 피드백 값을 출력으로 하는 메시지 통신의 서버 역할을 말한다.
- action client로부터 목푯값을 전달 받은 후 지정된 실질적인 액션의 실행을 담당한다.

#### 액션 클라이언트 action client

- action client는 목표를 출력으로 하고, action server로부터 결과 및 피드백 값을 입력으로 받는 메시지 통신의 클라이언트 역할을 말한다.
- action server에게 목표를 전달하고 결과 및 피드백을 수신받아 다음 지시를 내리거나 목표를 취소하는 역할을 한다.

#### 파라미터 parameter

- ROS에서 parameter는 노드에서 사용되는 파라미터를 말한다.
- parameter는 default로 설정값들이 지정되어 있고, 필요에 따라 외부에서 읽거나 쓸 수 있다. 특히 외부에서 쓰기 기능을 이용하여 상황에 따라 설정값을 실시간으로 바꿀 수 있기 때문에 매우 유용하다.
  - 예를 들어 외부 장치와 연결되는 PC의 USB 포트나 카메라 캘리브레이션 값, 모터 속도나 명령어들의 최댓값과 최솟값 등의 설정을 지정할 수 있다.

#### 파라미터 서버 parameter server

- 패키지에서 파라미터를 사용할 때, 각 파라미터를 등록하는 서버를 말한다.
- 마스터의 한 기능이기도 하다.

#### 캐킨 catkin

- catkin은 ROS의 빌드 시스템을 말한다.
- ROS의 빌드 시스템은 기본적으로 CMake(Cross Platform Make)를 이용하고 있어서 패키지 폴더에 CMakeLists.txt라는 파일에 빌드 환경을 기술하고 있다.

#### ROS 빌드 rosbuild

- ROS 빌드는 catkin 빌드 시스템 이전에 사용되었던 빌드 시스템이고 지금까지도 일부 사용하는 사용자들이 있기는 하지만 추천하지 않는다.

#### roscore

- roscore는 ROS 마스터를 구동하는 명령어다.

#### rosrun

- rosrun은 ROS의 기본 실행 명령어다.
- 패키지에서 하나의 노드를 실행하는데 사용된다.

#### roslaunch

- rosrun은 하나의 노드를 실행하는 명령어라면 roslaunch는 여러 노드를 실행하는 개념이다.
- 이 명령어를 통해 하나 그 이상의 정해진 노드를 실행시킬 수 있다.
- *.launch 파일을 사용하여 실행 노드에 대한 설정을 해주는데 이는 XML(Extensible Markup Language)에 기반을 두고 있으며, XML 태그 형태의 다양한 옵션을 제공한다.

#### bag

- ROS에서 주고받는 메시지의 데이터는 저장할 수 있는데 이때 사용되는 파일 포맷을 bag라고 하며 확장자로 *.bag를 사용한다.
- ROS에서는 이 bag를 이용하여 메시지를 저장하고 필요할 때 이를 재생하여 이전 상황을 그대로 재현할 수 있다.
  - 예를 들어 센서를 이용한 로봇 실험을 실행할 때, 센서값을 bag를 이용하여 메시지 형태로 저장한다. 이 저장된 메시지는 같은 실험으로 수행하지 않아도 저장해둔 bag 파일을 재생하는 것으로 그 당시에 센서값을 반복해서 사용할 수 있다.
  - 특히 rosbag의 기록, 재생의 기능을 활용하면 반복되는 프로그램 수정이 많은 알고리즘 개발에 매우 유용하다.

#### ROS Wiki

#### 리포지토리 repository

- repository는 패키지가 저장된 웹상의 URL 주소며 svn, hg, git 등의 소스 관리 시스템을 이용하여 이슈, 개발, 내려받기 등을 관리하고 있다.

#### 그래프 graph

- 노드, 토픽, 퍼블리셔, 서브스크라이버 관계는 graph를 통해 시각적으로 그 관계를 나타나게 할 수 있다.
- 현재 실행 중인 메시지 통신을 그래프로 나타낸 것으로 일회성의 서비스에 대한 그래프는 작성할 수 없다.
- 실행은 rqt_graph 패키지의 rqt_graph 노드를 실행하면 된다.
  - rqt_graph
  - rosrun rqt_graph rqt_graph

#### 네임 name

- 노드, 파라미터, 토픽, 서비스에는 모두 name이 있다.
- 이 name을 마스터에 등록하고 각 노드의 파라미터, 토픽, 서비스를 사용할 때 이름을 기반으로 검색, 메시지를 전송한다.
- 또한 네임은 살행할 때 변경할 수 있기 때문에 매우 유연하고, 같은 노드, 파라미터, 토픽, 서비스라고 하여도 다른 네임으로 중복하여 사용할 수 있다.
- 이러한 네임의 사용으로 ROS는 큰 규모의 프로젝트, 복잡한 구조의 시스템에도 적합하다.

#### 클라이언트 라이브러리 client library

- ROS는 사용되는 언어의 의존성을 낮추기 위해 클라이언트 라이브러리로 각종 언어의 개발환경ㅇ르 제공한다. 주요  클라이언트 라이브러리는 C++, Python, Lisp...

#### URI

- Uniform Resource Identifier : 통합 자원 식별자는 인터넷에 있는 자원을 나타내는 유일한 주소다.

#### MD5

- Message-Digest algorithm 5는 128bit 암호화 해시 함수다. 주로 프로그램이나 파일이 원본 그대로인지를 확인하는 무결성 검사 등에 사용된다.
- ROS의 메시지를 이용한 통신에서 메시지 송수신 무결성을 검사한다.

#### XML

- Extensible Markup Language는 W3C에서 다른 특수 목적의 마크업 언어를 만드는 용도로 권장하는 다목적 마크업 언어(markup language)이다.
- 태그 등을 이용하여 데이터의 구조를 명기하는 언어의 한 가지이다.
- ROS에서는 *.launch, *.urdf, package.xml 등 다양한 부분에서 사용되고 있다.

#### XMLRPC

- XML-Remote Procdure Call이란 RPC 프로토콜의 일종으로서, 인코딩 형식에서는 XML을 채택하고, 전송 방식에서는 접속상태를 유지하지 않고 점검하지 않는 요청과 응답 방식의 HTTP 프로토콜을 사용한다.
- 매우 단순한 규약으로서, 작은 데이터 형식이나 명령을 정의하는 정도로만 사용하고 있어서 꽤나 단순한 편이다. 그래서 매우 가볍고, 댜양한 프로그래밍 언어를 지원하기 때문에 여러 종류의 하드웨어와 언어를 지원하는 ROS에 매우 적합하다.

#### TCP/IP

- Transmission Control Protocol은 전송 제어 프로토콜이다. 
- 흔히 TCP/IP라 부르는데 이는 인터넷 프로토콜 계층의 시각에서 보면 Internet Protocol을 기반으로 전송 제어 프로토콜인 TCP를 사용하여 데이터의 전달을 보증하고 보낸 순서대로 송수신한다.
- TCPROS 메시지 및 서비스에서 사용되는 TCP/IP 기반의 메시지 방식을 TCPROS라고 한다.

#### CMakeLists.txt

- ROS의 빌드 시스템인 캐킨은 기본적으로 CMake를 이용하고 있어서 패키지 폴더에 CMakeLists.txt 파일에 빌드 환경을 기술하고 있다.

#### package.xml

- 패키지의 정보를 담은 XML 파일로 패키지 이름, 저작자, 라이선스, 의존성 패키지 등을 기술하고 있다.







## 4.2. 메세지 통신

- 그림 4-1 노드 간의 메시지 통신

- | 종류    | 차이점 |        |                                                              |
  | ------- | ------ | ------ | ------------------------------------------------------------ |
  | topic   | 비동기 | 단방향 | 연속적으로 데이터를 송수힌 하는 경우에 사용                  |
  | service | 동기   | 양방향 | 요청 처리가 순간적인 현재 상태의 요청 및 응답 등에 사용      |
  | action  | 비동기 | 양방향 | 요청 처리 후 응답까지 오랜 시간이 걸려서 서비스를 이용하기 어려운 경우나 중간 피드백값이 필요한 경우에 사용 |



### 4.2.1. 토픽(topic)

- 토픽 메시지 통신 : 정보를 송신하는 publisher와 정보를 수신하는 subscriber가 토픽 메시지 형태로 정보를 송수신하는 것이다.
- 토픽을 수신받기를 원하는 subscribe 노드는 마스터에 등록된 토픽 이름에 해당하는 publisher 노드의 정보를 받는다. 이 정보를 기반으로 subscriber 노드는 publisher 노드와 직접 연결하여 메시지를 송수신한다.
- 토픽은 단방향 통신이면서 한 번의 접속으로 지속해서 메시지를 송수힌하기 때문에 지속해서 메시지를 발송해야 하는 센서 데이터에 적합하다.
- 하나의 publisher에 여럿의 subscriber의 통신, 하나의 토픽에 대해 여럿의 publisher에 하나의 subscriber의 통신, 여럿의 publisher에 여럿의 subscriber의 통신도 가능하다. 1:N, N:1, N:N 통신 가능하다.

### 4.2.2. 서비스(service)

- 서비스 메시지 통신 : 서비스를 request하는 service client와 서비스 response를 담당하는 service server간의 동기적 양방향 서비스 메시지 통신을 말한다.
- 서비스는 request가 있을 때만 response하는 서비스 서버와 요청하고 응답받는 서비스 클라이언트로 나뉜다.
- 일회성 메시지 통신이다. 따라서 서비스의 request과 response가 완료되면 연결된 두 노드는 접속이 끊긴다.
- 이러한 서비스는 로봇에 특정 동작을 수행하도록 요청할 때에 사용되는 명령어로 많이 사용되거나, 혹은 특정 조건에 따라 이벤트를 발생할 노드에 사용된다.
- 일회성 통신 방식이라서 네트워크에 부하가 적기 때문에 토픽을 대체하는 수단으로도 사용되는 등 매우 유용한 통신수단이다.
- 그림 4-3 서비스 메시지 통신

### 4.2.3. 액션(action)

- 액션 메시지 통신 : 요청을 처리 후 응답까지 오랜 시간이 걸리고 중간 결괏값이 필요한 경우에 사용되는 메시지 통신방식이다.
- 서비스와 많이 비슷한데 request와 response에 해당하는 목표(goal)와 결과(result) 그리고 피드백(feedback)이 추가되었다.
  - 요청 처리 후 응답까지 오랜 시간이 걸리고 중간 결괏값이 필요할 때 이 피드백을 이용하여 관련 데이터를 전송한다.
- 메시지 전송방식 자체는 비동기식인 토픽과 동일하다.
- feedback은 액션의 goal을 정하는 action client와 목표에 맞추어 정해진 일을 수행하고 액션 피드백과 결과를 전달하는 action server 간의 비동기식 양방향 메시지 통신을 수행한다. 
- 액션은 서비스와 달리 목푯값을 전달한 후, 임의의 시점에서 목표를 취소하는 명령어를 전달할 수 있는 기능도 갖고 있는 등 복잡한 로봇의 엄무를 지시하는데 많이 사용된다.



- publishser, subscriber, service server, service client, action server, action client는 모두 각각 다른 노드 안에 존재하게 되는데 이러한 노드들이 메시지 통신을 하는 데에는 접속이 필요하다.
- 이때 노드 간의 접속을 돕는 것이 마스터이다. 마스터는 노드의 이름, 토픽과 서비스, 액션의 이름 URI 주소와 포트, 파라미터 등의 네임 서버와 같은 역할을 한다.
- 즉 노드는 생성과 동시에 마스터에 자신의 정보를 등록하고, 다른 노드가 마스터에 자신의 정보를 등록하고, 다른 노드가 마스터를 통해 접속하려는 노드의 정보를 마스터로부터 취득한다. 그런 다음, 노드와 노드가 직접 접속하여 메시지 통신을 수행한다. 
- 그림 4-5 메시지 통신

### 4.2.4. 파라미터(parameter)

- 메시지 통신에는 크게 토픽, 서비스, 액션으로 나뉘고 큰 틀에서 파라미터 또한 메시지 통신이라고 볼 수 있다.
- 파라미터는 노드에서 사용되는 글로벌 변수라고 생각하면 된다.
- 파라미터는 필요에 따라서 외부에서 이 매개변수를 읽거나 쓸 수 있다. 특히 외부에서 쓰기 기능을 이용하여 설정값을 실시간으로 바꿀 수 있기 때문에 상황에 따라 유연하게 대처할 수 있어서 매유 유용한 방법이다.
- 파라미터는 엄밀히 따지면 메시지 통신은 아니지만 필자는 메시지를 이용한다는 점에서 메시지 통신 범위라고 본다.

### 4.2.5. 메세지 통신의 흐름

- 마스터는 노드들의 정보를 관리하며, 각 노드는 필요에 따라 다른 노드와 접속, 메시지 통신을 수행한다.

#### 마스터 구동

- 노드 간의 메시지 통신에서 연결 정보를 관리하는 마스터는 ROS를 사용하기 위해서 제일 먼저 구동해야 하는 필수 요소이다.

- roscore

- XMLRPC로 서버를 구동한다.

- 마스터는 노드 간의 접속을 위하여 노드들의 name, topic, service, action name, 메시지 형태, URI 주소와 포트를 등록받고, 요청이 있을 때 이 정보를 다른 노드에 알린다.

- ```
  $ roscore
  ```

#### 서브스크라이버 노드 구동

- subscriber 노드는 구동과 함께 마스터에 자신의 서브스크라이버 노드 이름, 토픽 이름, 메시지 형태, URI 주소와 포트를 등록한다.

- 마스터와 노드는 XMLRPC를 이용하여 통신한다.

- ```
  $ rosrun Package_Name Node_Name
  $ roslaunch Package_Name Launch_Name
  ```

#### 퍼블리셔 노드 구동

- publisher 노드는 구동과 함께 마스터에 자신읜 퍼브릴셔 노드 이름, 토픽 이름, 메시지 형태, URI 주소와 포트를 등록한다.
- 마스터와 노드는 XMLRPC를 이용하여 통신한다.

#### 퍼블리셔 정보 알림

- 마스터는 서브스크라이버 노드에 서브스크라이버가 접속하기 원하는 퍼블리셔의 이름, 토픽 이름, 메시지 형태, URI 주소와 포트 등의 정보를 전송한다.

#### 서브스크라이버 노드의 접속 요청

- 서브스크라이버 노드는 마스터로부터 받은 퍼블리셔 정보를 기반으로 퍼블리셔 노드에 직접 접속을 요청한다.
- 이때 전송하는 정보로는 자신의 서브스라이버 노드 이름, 토픽 이름, 메시지 방식이 있따.
- 퍼블리셔 노드와 서브스크라이버 노드는 XMLRPC를 이용해 통신한다.

#### 퍼블리셔 노드의 접속 응답

- 퍼블리셔 노드는 서브스크라이버 노드에 접속 응답에 해당하는 자신의 TCP 서버의 정보인 URI 주소와 포트를 전송한다.
- 퍼블리셔 녿으와 서브스크라이버 노드는 XMLRPC를 이용하여 통신한다.

#### TCPROS 접속

- 서브스크라이버 노드는 TCPROS를 이용하여 퍼블리셔 노드에 대한 클라이언트를 만들고, 퍼블리셔 노드와 직접 연결한다.

#### 메시지 전송

- 퍼블리셔 노드는 서브스크라이버 노드에 정해진 메시지를 전송한다.
- 노드 간 통신은 TCPROS라는 TCP/IP 방식을 이용한다.

#### 서비스 요청 및 응답

- 앞서 설명한 내용은 메시지 통신 중에 토픽에 해당한다. 토픽 메시지 통신은 퍼블리셔나 서브스크라이버가 중지하지 않는 이상, 메시지를 연속해서 퍼블리시하고 서브스크라이브한다.
- 서비스 클라이언트 : 서비스를 요청
- 서비스 서버 : 서비스를 요청받아 정해진 프로세스를 수행하고 응답
- 서비스 서버와 클라이언트의 접속은 TCPROS 접속과 같지만, 서비스는 토픽과 달리 1회에 한해 접속하여, 요청과 응답을 수행하고 서로의 접속을 끊는다. 다시 필요하면 접속부터 새롭게 진행해야 한다.

#### 액션 목표, 결과, 피드백

- 서비스의 요청과 응답의 중간 결괏값 전달용으로 피드백을 추가한 형태이지만 실제 구동 방식은 토픽과 같다.
- 실제로 rostopic 명령어를 이용하여 토픽을 확인하면 액션은 goal, status, cancel, result, feedback과 같이 액션에서 사용하는 5개의 토픽을 확인할 수 있다.
- TCPROS 접속과 같지만 액션 클라이언트에서 취소 명령을 보내거나 서버에서 결괏값을 보내주면 접속이 종료되는 등 사용법은 조금 상이하다.



- 동작은 그림 4-12 TCP 접속 확인

## 4.3. 메세지

- message는 노드 간에 데이터를 주고받을 때 사용하는 데이터의 형태이다.

- 메시지는 단순한 자료형부터 'geometry_msgs/PoseStamped'와 같은 메시지 안에 메시지를 품고 있는 간단한 데이터 구조, 'float[] ranges' 같은 메시지들이 나열된 배열과 같은 구조도 사용할 수 있다. 더불어 ROS에서 많이 사용되는 헤더(Header, std_msgs/Header)도 메시지로 사용할 수 있다.

- 이러한 메시지는 필드타입(fieldtype)과 필드네임(fieldname)으로 구성되어 있다.

- ```
  fieldtype1 fieldname1
  fieldtype2 fieldname2
  fieldtype3 fieldname3
  ```

- fieldtype에는 ROS의 자료형을 fieldname에는 데이터를 의미하는 이름을 적어주게 되어 있다.

- ```
  int32 x
  int32 y
  ```

- 예

  - Header, std_msgs/Header.msg

    - ```
      # 시퀀스 아이디 : 연속하여 증가하는 ID로 메시지가 차례대로 +1씩 증가한다.
      uint32 seq
      # 타임스탬프 : 초단위의 stamp.sec와 나노 초단위의 stamp.nsec의 2개의 하위 속성을 갖고 있다.
      time stamp
      # 프레임 아이디를 기재한다.
      string frame_id
      ```

  - turtlesim 패키지의 teleop_turtle_key노드

    - 실행된 후 입력되는 키보드의 방향키에 따라 turtlesim_node 노드에서 병진속도(meter/sec)와 회전속도(radian/sec)를 메시지로 전달하고 있다.

    - 이 전달 받은 속도값을 이용하여 화면 속 터틀봇이 움직이게 된다.

    - 이때 사용된 메시지는 geometry_msgs 중 Twist메시지다.

      - ```
        Vector3 linear
        Vector3 angular
        ```

      - 이는 Vector3 메시지 형태로 linear와 angle 이름으로 선언해 두었다. 이는 메시지 안에 메시지 형태로 Vector3 메시지는 geometry_msgs 중의 하나이다. 다음은 Vector3의 형태이다.

      - ```
        float63 x
        float63 y
        float63 z
        ```

    - 즉 teleop_turtle_key 노드에서 퍼블리시되는 토픽은 linear.x, linear.y, linear.z, angular.x, angular.y, angular.z로 총 6개의 메시지가 있다.

    - float64 형태이다. 이를 이용하여 키보드의 화살표가 병진속도와 회전속도 메시지로 전송하여 터틀봇이 구동할 수 있게 되었던 것이다.

### 4.3.1. msg 파일

- msg파일은 토픽에 사용되는 메시지 파일로 *.msg라는 확장자를 이용한다.

- msg파일은 fieldtype과 fieldname만으로 구성되어 있다.

- geometry_msgs/Twist.msg

  - ```
    Vector3 linear
    Vector3 angular
    ```

### 4.3.2. srv 파일

- srv 파일은 서비스에서 사용되는 메시지 파일로 확장자는 *.srv이다.

- 예를 들어 sensor_msgs 중 SetCameraInfo메시지가 대표적인 srv 파일이다.

- 하이픈(---)이 구분자 역살을 하여 상위 메시지가 서비스 오청 메시지, 하위 메시지가 서비스 응답 메시지로 사용된다.

- sensor_msgs/SetCameraInfo.srv

  - ```
    sensor_msgs/CameraInfo camera_info #서비스 요청 메시지
    ---
    bool success #서비스 응답 메시지
    string status_message
    ```

### 4.3.3. action 파일

- action 메시지 파일은 액션에서 사용되는 메시지 파일로 *.action이라는 확장지를 이용한다.

- 비교적 많이 사용되는 메시지 파일이 아니라 대표적인 공식 메시지 파일은 없지만 다음 예제처럼 사용이 가능하다.

- 3개의 하이픈(---)이 구분자 역할로 2군데 사용되어 첫 번째가 goal 메시지, 두 번째가 result 메시지, 세 번째가 feedback 메시지로 사용된다.

- action 파일의 feedback 메시지는 지정된 프로세스가 수행되면서 중간 결괏값 전송 목적으로 이용한다는 것에 차이가 있다.

- 예

  - 로봇의 출발지점 start_pose와 목표지점 goal_pose의 위치와 자세를 요청값으로 전송하게 되면 로봇은 정해진 목표지점으로 이동하여 최종적으로 도달된 result_pose의 위치 자세값으로 전달한다. 더불어, 주기적으로 중간 결괏값으로 percent_complete 메시지로 목표지점까지의 도달 정도를 퍼센트로 전달하게 된다.

  - ```
    geometry_msgs/PoseStamped start_pose
    geometry_msgs/PoseStamped goal_pose
    ---
    geometry_msgs.PoseStamped result_pose
    ---
    float32 percent_complete
    ```

## 4.4. 네임(name)

- ROS는 그래프(graph)라는 추상 데이터 형태(abstract data type)를 기본 콘셉트로 가지고 있다. 이는 각 노드들의 연결 관계를 나타내고 화살표로 메시지(데이터)를 주고받는 관계를 설명하게 된다.

- 이를 위해 ROS에서 사용되는 노드, 토픽과 서비스에서 사용되는 메시지 그리고 파라미터는 모두 고유의 네임(name)을 가지도록 되어 있다.

- 토픽의 네임은 상대적인 방법과 글로벌(global), 프리베이트(private)로 나뉘어 사용한다.

- ```c++
  //7장에서 자세히
  
  int main(int argc, char **argv) 	// 노드 메인 함수
  {
  	ros::init(argc, argv, "node1"); // 노드명 초기화
      ros::NodeHandle nh;				// 노드 핸들 선언
      // 퍼블리셔 선언, 토픽명 = bar
      ros::Publisher node1_pub = nh.advertise<std_msgs::Int32>("bar", 10)
  }
  ```

  - 노드명 : /node1이 된다. 그리고 아무런 문자를 붙이지 않고 상대적 형태인 bar로 퍼블리셔를 선언하게 되면 토픽은 /bar와 같은 네임을 가지게 된다.

  - 만약에 슬래쉬(/) 문자로 글로벌로 사용하였다 하더라도 토픽 네임은 /bar가 된다.

  - ```c++
    ros::Publisher node1_pub = nh.advertise<std_msg::Int32>("/bar", 10);
    ```

  - 틸트(~) 문자를 이용하여 private로 선언하게 되면 토픽 네임은 /node1/bar가 된다.

  - ```c++
    ros::Publisher node1_pub = nh.advertise<std_msg::Int32>("~bar", 10);
    ```

  - 표 4-4 네임 규칙

  - 두 대의 카메라를 구동하려면?

    - 단순히 관련 노드를 두 번 실행하면 교유의 네임을 가져야하는 ROS의 특성상 이전에 실행한 노드가 종료하게 된다. 그렇다고 별도의 프로그램을 실행하거나 소스 코드를 변경하는 것이 아니라 노드를 실행할 때 노드의 이름을 변경하여 실행할 수 있다. 방법 : 네임스페이스(namespace)와 리맵핑(remapping)이 있다.

    - 예

      - 가상의 camera_package가 있다고 하자. 이 camera_package 패키지의 camera_node를 실행했을 때 camera 노드가 실행된다고 했을 때 이 구동 방법은 다음과 같다.

        - ```
          $ rosrun camera_package camera_node
          ```

      - 이 노드에서 카메라의 영상값을 image 토픽으로 전송한다고 했을 때, 다음과 같이 rqt_image_view를 통해서 이 image 토픽을 전송받을 수 있다.

        - ```
          $ rosrun rqt_image_view rqt_image_view
          ```

      - 이제 이 노드들의 토픽값을 리맵핑을 통해 수정해보자

      - 다음과 같이 실행하게 되면 주고받는 토픽명만 /front/image로 변경된다.

      - 여기서 image는 camera_node에서의 토픽명으로 이 토픽명과 관련된 두 노드의 실해오가 함께 옵션으로 네임을 변경하는 명령어의 예이다.

        - ```
          $ rosrun camera_package camera_node image:=front/image
          $ rosrun rqt_image_view rqt_image_view image:=front/image
          ```

      - 예를 들어 front, left, right와 같이 카메라 3대가 있을 때, 이를 동일 이름으로 노드를 복수 실행할 때 노드의 고유 네임이 중복되어 전에 실행된 노드가 중단된다. 때문에 다음과 같은 방법으로 같은 이름이지만 복수 개의 다른 노드로 실행 가능하다.

      - 여기서 name옵션에 밑줄(__)이 2개 사용되었는데 ...등의 옵션은 노드를 실행할 때 사용하는 특수 옵션이다. 그리고 토픽명의 옾션 앞에 밑줄 하나를 사용했는데 이는 private로 사용되는 네임일 경우 네임에 덧붙여 사용한다.

        - ```
          $ rosrun camera_package camera_node __name:=front _device:=/dev/video0 
          $ rosrun camera_package camera_node __name:=left _device:=/dev/video1 
          $ rosrun camera_package camera_node __name:=right _device:=/dev/video2
          $ rosrun rqt_image_view rqt_image_view
          ```

      -  만약 하나의 네임스페이스로 묶어주고 싶다면 다음과 같이 하면 된다. 

        - ```
          $ rosrun camera_package camera_node __ns:=back
          $ rosrun rqt_image_view rqt_image_view __ns:=back
          ```



## 4.5. 좌표 변환(TF)

- 로봇의 팔 자세를 설명할 때 각 관절(joint)들의 상대 좌표 변환으로 기술할 수 있다.

- 로봇은 물체를 잡기 위하여 지도상에서 자신의 자세로부터 상대적으로 물체의 위치를 계산하여 잡을 수 있게 된다.

- 이렇게 로봇 프로그래밍에서 좌표 변환을 통한 각 로봇의 관절(혹은 회전축 등을 갖는 바퀴) 및 물체의 위치는 매우 중요하며 ROS에서는 이를 TF(transform)로 표현하고 있다.

- ROS에서 좌표 변환 TF는 로봇을 구성하는 각 부분 및 장애물과 물체들을 기술할 때 매우 유용한 개념 중에 하나이다.

- 이들은 자세(pose)라 하여 위치(position)와 방향(orientation)으로 기술할 수 있다.

- 여기서 위치는 x, y, z과 같이 3개의 벡터로 설명하고 방향은 사원수라 일컫는 쿼터니언(quaternion) 형태의 x, y, z, w를 이용한다. quaternion은 흔히 우리 생활에서 사용하는 각도 표현 형태인 롤(roll), 피치(pitch), 요(yaw)와 같이 3가지 축(x, y, z)의 회전으로 기술하는게 아니다 보니 직관적이지는 않다. 

- 하지만 roll, pitch, yaw 벡터의 오일러(Euler) 방식이 갖는 짐벌락(gimbal lock) 문제나 속도 문제가 없어서 로보티긋에서는 기본적으로 쿼터니언(quaternion) 형태를 더 선호한다.

- 물론 편의성을 고려하여 오일러 값을 쿼터니언으로 변환해주는 함수도 제공해주고 있다.

- geometry_msgs/TransformStamped.msg

  - ```
    Header header
    string child_frame_id
    Transform transform
    ```

  - 변환된 시간을 기록할 목적으로 Header를 사용하며, 하위 좌표를 명시하기 위하여 child_frame_id라는 이름의 메시지를 사용한다. 그리고 상대 좌표 변환값을 알려주기 위하여 transform.translation.x / transform.translation.y / transform.translation.z / transform.rotation.x / transform.rotation.y / transform.rotation.z / transform.rotation.w 데이터 형태로 상대 위치와 방향을 기술하게 되어있다.

## 4.6. 클라이언트 라이브러리

- 특성상 다양한 목적을 갖는 로봇을 지원하는 ROS는 이들의 언어들을 목적에 맞게 골라서 사용할 수 있도록 지원하고 있다.
- 그 방법론으로 노드는 각각의 언어로 작성이 가능하고 노드 간의 메시지 통신을 통해 정보를 교환하는 방법을 이용하고 있다.
- 이중 각각의 언어로 작성 가능하게 해주는 소프트웨어 모듈이 클라이언트 라이브러리(client library)이다.
  - C++ - roscpp, Python - rospy ...

## 4.7. 이기종 디바이스 간의 통신

- 2장에서 설명한 메타 운영체제, 4장에서 설명한 메시지 통신, 메시지, 네임, 좌표 변환, 클라이언트 라이브러리 등의 콘셉트를 통해 ROS는 이기종 디바이스 간의 통신을 기본적으로 지원한다.
- ROS가 설치되어 사용하는 운영체제의 종류와도 상관없고, 사용하는 프로그래밍 언어도 상관없이 ROS가 설치되어 각 노드가 개발되었다면 각 노드들 간의 통신은 매우 쉽게 이용 가능하다.
- 예를 들어 로봇에는 리눅스의 한 배포판인 우분투가 설치되어 있더라고, 개발자가 사용하는 MacOS에서 로봇의 상태를 모니터링 할 수 있다. 이와 동시에 사용자는 안드로이드 기반의 앱(APP)에서 로봇에게 명령을 내릴 수 있다.

## 4.8. 파일 시스템

### 4.8.1. 파일 구성

- ROS에서 소프트웨어 구성을 위한 기본 단위는 package로써 ROS의 응용프로그램은 package단위로 개발된다.
- package는 ROS에서 최소 단위의 실행 프로세서인 node를 하나 이상 포함하거나 다른 노드를 실행하기 위한 설정 파일들을 포함하게 된다.
- 패키지는 메타패키지(metapackage)라는 공통된 목적을 지닌 패키지들을 모아둔 패키지들의 집합 단위로 관리되기도 한다.
- 예를 들어 Navigation 메타패키지는 AMCL, DWA, EKF, map_server 등 10여 개의 패키지로 구성되어 있다. 
- 각 패키지는 package.xml이라는 파일을 포함하고 있는데 이는 패키지의 정보를 담은 XML 파일로서 패키지 이름, 저작자, 라이선스, 의존성 패키지 등을 기술하고 있다.
- ROS의 빌드 시스템인 캐킨은 기본적으로 CMake를 이용하고 있어서 패키지 폴더에 CMakeLists.txt라는 파일에 빌드 환경을 기술하고 있다.
- 노드의 소스 코드 및 노드 간의 메시지 통신을 위한 메시지 파일 등으로 구성되어 있다.



- ROS의 파일 시스템은 설치 폴더와 사용자 작업 폴더로 구분된다.
  - ROS 설치 폴더는 ROS의 데스크톱 버전을 설치하면 /opt 폴더에 ros 이름으로 폴더가 생성되고 그 안에 roscore를 포함한 핵심 유틸리티와 rqt, RViz, 로봇 관련 라이브러리, 시뮬레이션, 내비게이션 등이 설치된다.
  -  사용자 작업 폴더는 사용자가 원하는 곳에 폴더를 생성할 수 있는데 리눅스 사용자 폴더인 '~/catkin_ws/'('~/'은 리눅스에서 '/home/사용자명/'에 해당하는 폴더를 의미)를 사용하도록 하자.

### 4.8.2. 설치 폴더

#### 파일 구성

- '/opt/ros/kinetic'의 폴더 아래에 bin, etc, include, lib, share 폴더와 몇가지 환경설정 파일들로 구성되어 있다.

#### 세부 내용

- /bin : 실행 가능한 바이너리 파일
- /etc : ROS 및 catkin 관련 설정 파일
- /include : 헤더 파일
- /lib : 라이브러리 파일
- /share : ROS 패키지 
- env.* : 환경설정 파일
- setup.* : 환경설정 파일

### 4.8.3. 작업 폴더

- 작업 폴더는 사용자가 원하는 곳에 생성할 수 있으나 이 책에서는 ~/catkin_ws/를 사용한다.

#### 파일 구성

- catkin_ws
  - build
  - devel
  - src

#### 세부 내용

- 작업 폴더는 사용자가 작성한 패키지와 공개된 다른 개발자의 패키지를 저장하고 빌드하는 공간이다.
- ROS와 관련된 대부분 작업을 이 폴더에서 수행한다.
- /bulid : 빌드 관련 파일
- /devel : msg, srv 헤더 파일과 사용자 패키지 라이브러리, 실행 파일
- /src : 사용자 패키지

#### 사용자 패키지

- '~/catkin_ws/src' 폴더는 사용자 소스 코드의 공간이다. 이 폴더에서 사용자가 개발한 ROS 패키지나 다른 개발자가 개발한 패키지를 저장하고 빌드할 수 있다.
- /include : 헤더파일
- /launch : roslaunch에 사용되는 launch 파일
- /node : rospy용 스크립트
- /msg : 메시지 파일
- /src : 코드 소스 파일
- /srv : 서비스 파일
- CMakeLists.txt : 빌드 설정 파일
- package.xml : 패키지 설정 파일

## 4.9. 빌드 시스템

- ROS의 빌드 시스템은 기본적으로 CMake(Cross Platform Make)를 사용하고 빌드 환경은 패키지 폴더의 CMakeList.txt 파일에 기술한다.
- ROS에서는 CMake를 ROS에 맞도록 수정하여 ROS에 특화된 캐킨(catkin) 빌드 시스템을 제공한다.
- ROS에서 CMake를 이용하는 이유는 ROS 패키지를 멀티 플랫폼에서 빌드할 수 있게 하기 위함이다.
- 캐킨 빌드 시스템은 ROS와 관련된 빌드, 패키지 관리, 패키지간 의존관계 등을 편리하게 사용할 수 있도록 하고 있다.

### 4.9.1 패키지 생성

- ```
  $ catkin_create_pkg [패키지 이름] [의존하는패키지1] [의존하는패키지n]
  ```

  - 'catkin_create_pkg'는 사용자가 패키지를 작성할 떄 캐킨 빌드 시스템에 꼭 필요한 CMakeLists.txt와 package.xml을 포함한 패키지 폴더를 생성한다.

### 4.9.2. 패키지 설정 파일(package.xml) 수정

- ROS의 필수 설정 파일 중 하나인 package.xml은 패키지의 정보를 담은 XML 파일로서 패키지의 이름, 저작자, 라이선스, 의존성 패키지 등을 기술하고 있다.
- <?xml> : 문서 문법을 정의하는 문구로 아래의 내용은 xml 버전 1.0을 따르고 있다는 것을 알린다.
- <package> : 이 구문부터 맨 끝의 </package>까지가 ROS 패키지 설정 부분이다.
- <name> : 패키지의 이름이다. 패키지를 생성할 때 입력한 패키지 이름이 사용된다. 다른 옵션도 마찬가지지만 이는 사용자가 원할 때 언제든지 변경할 수 있다.
- <version> : 패키지의 버전이다. 자유롭게 지정할 수 있다.
- <description> : 패키지의 간단한 설명이다. 보통 2~3 분장으로 기술한다.
- <maintainer> : 패키지 관리자의 이름과 이메일 주소를 기재한다.
- <license> : 라이선스를 기재한다. BSD, MIT, Apache, GPLv3, LGPLv3 등을 기재하면 된다.
- <url> : 패키지를 설명하는 웹 페이지 또는 버그 관리, 저장소 등의 주소를 기재한다. 이 종류에 따라 type에 website, bugtracker, repository를 대입하면 된다.
- <author> : 패키지 개발에 참여한 개발자의 이름과 이메일 주소를 적는다. 복수의 개발자가 참여한 경우에는 바로 다음 줄에 <author> 태그를 이용하여 추가로 넣어주면 된다.
- <buildtool_depend> : 빌드 시스템의 의존성을 기술한다. 지금은 캐킨 빌드 시스템을 이용하고 있으므로 catkin을 입력한다.
- <build_depend> : 패키지를 빌드할 때 의존하는 패키지 이름을 적는다.
- <run_depend> : 패키지를 실행할 때 의존한느 패키지 이름을 적는다.
- <test_depend> : 패키지를 테스트할 때 의존하는 패키지 이름을 적는다.
- <export> : ROS에서 명시하지 않은 태그명을 사용할 때 쓰인다. 제일 널리 쓰이는 것은 메타패키지일 때 <export><metapackage/X/export>와 같이 메타패키지임을 기술한다.
- <metapackage> : export 태그 안에서 사용하는 공식적인 태그로 현재의 패키지가 메타패키지이면 이를 선언한다.

- 책 83쪽에 예시가 있다.

### 4.9.3. 빌드 설정 파일(CMakeLists.txt) 수정

- ROS의 빌드 시스템인 캐킨은 기본적으로 CMake를 이용하고 있어서 패키지 폴더의 CMakeLists.txt라는 파일에 빌드 환경을 기술하고 있다. 

- 이는 실행 파일 생성, 의존성 패키지 우선 빌드, 링크 생성 등을 설정하게 되어 있다.

- ```cmake
  cmake_minimum_required(VERSION 2.8.3)
  운영 체제에 설치된 cmake의 최소 요구 버전이다.
  ```

- ```cmake
  project(my_first_ros_pkg)
  패키지의 이름이다.
  package.xml에서 입력한 패키지 이름을 그대로 사용해야 한다. 그렇지 않으면 빌드할 때 에러가 발생할 수 있다.
  ```

- ```cmake
  find_package(catkin REQUIRED COMPONENTS
    roscpp
    std_msgs
  )
  캐킨 빌드를 할 때 요구되는 구성 요소 패키지이다.
  현재 의존성 패키지로 roscpp, std_msgs가 추가되어 있다. 
  여기에 입력된 패키지가 없다면 캐킨 빌드할 때 사용자에게 에러가 표시된다. 즉 사용자가 만든 패키지가 의존하는 다른 패키지를 먼저 설치하게 만드는 옵션이다.
  ```

- ```cmake
  find_package(Boost REQUIRED COMPONENTS system)
  ROS 이외의 패키지를 사용할 때 사용되는 방법이다. 
  예를 들어 Boost를 사용할 때 system 패키지가 설치되어 있어야 한다.
  ```

- ```cmake
  catkin_python_setup()
  rospy를 사용할 때 설정하는 옵션이다.
  파이썬 설치 프로세스인 setup.py를 부르는 역할을 한다.
  ```

- ```cmake
  add_message_files(
    FILES
    Message1.msg
    Message2.msg
  )
  메시지 파일을 추가하는 옵션이다.
  FILES를 사용하면 현재 패키지 폴더의 msg 폴더 안에 .msg 파일들을 참조하여 헤더 파일(*.h)을 자동으로 생성하게 된다.
  ```

- ```cmake
  add_service_files(
   FILES
   Service1.srv
   Service2.srv
  )
  서비스 파일을 추가하는 옵션이다.
  FILES를 사용하면 패키지 폴더의 srv 폴더 안의 .srv 파일들을 참조한다.
  ```

- ```cmake
  generate_message(
    DEPENDENCIES
    std_msgs
  )
  의존하는 메시지를 설정하는 옵션이다.
  이 예제는 DEPENDENCIES 옵션에 의해 std_msgs 메시지 패키지를 사용하겠다는 설정이다.
  ```

- ```cmake
  generate_dynamic_reconfigure_options(
    cfg/DynReconf1.cfg
    cfg/DynReconf2.cfg
  )
  dynamic_reconfigure 사용할 때 참조하는 설정 파일을 불러오는 설정이다.
  ```

- ```cmake
  catkin_package(
    INCLUDE_DIRS include
    LIBRARIES my_first_ros_pkg
    CATKIN_DEPENDS roscpp std_msgs
    DEPENDS system_lib
  )
  캐킨 빌드 옵션이다.
  INCLUDE_DIRS는 뒤에 설정한 패키지 내부 폴더인 include 헤더파일을 사용하겠다는 설정이다.
  LIBRARIES는 뒤에 설정한 패키지의 라이브러리를 사용하겠다는 설정이다.
  CATKIN_DEPENDS 뒤에는 의존하는 패키지를 지정한다.
  DEPENDS는 시스템 의존 패키지를 기술하는 설정이다.
  ```

- ```cmake
  include_directories(
    ${catkin_INCLUDE_DIRS}
  )
  인클루드 폴더를 지정할 수 있는 옵션이다.
  ${catkin_INCLUDE_DIRS}라고 설정되어 있는데 이는 각 패키지 안의 include 폴더를 의미하고 이 안의 헤더 파일을 이용하겠다는 설정이다.
  사용자가 추가로 인클루드 폴더를 지정할 때는 ${catkin_INCLUDE_DIRS} 아랫줄에 기재하면 된다.
  ```

- ```cmake
  add_library(my_first_ros_pkg
    src/${PROJECT_NAME}/my_first_pkg.cpp
  )
  빌드 후 생성할 라이브러리를 선언한다.
  위 내용은 my_first_ros_pkg 패키지 src 폴더에 위치한 my_first_ros_pkg.cpp를 참조하여 my_first_ros_pkg 라이브러리를 생성하는 명령이다.
  ```

- ```cmake
  add_dependencies(my_first_ros_pkg ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
  해당 라이브러리 및 실행 파일을 빌드하기에 앞서 생성해야 할 의존성이 있는 메시지 및 dynamic rconfigure가 있으면 우선적으로 이를 수행하라는 설정이다.
  위 내용은 위에서 언급한 my_first_ros_pkg 라이브러리에 의존성이있는 메시지 및 dynamic reconfigure 생성을 우선적으로 진행하라는 옵션이다.
  ```

- ```cmake
  add_executable(my_first_ros_pkg_node src/my_first_ros_pkg_node.cpp)
  빌드 후 생성할 실행 파일에 대한 옵션을 지정한다.
  위 내용은 src/my_first_ros_pkg_node.cpp 파일을 참조하여 my_first_ros_pkg_node 실행 파일을 실행하라는 내용이다.
  만약 참조해야할 *.cpp 파일이 많은 경우 my_first_ros_pkg_node.cpp 뒤에 이어서 적어주고, 생성할 실행 파일이 2개 이상인 경우, add_executable 항목을 추가로 적어준다.
  ```
  
- ```cmake
  add_dependencies(my_first_ros_pkg_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
  앞서 설명한 add_dependencies와 마찬가지로 해당 라이브러리 및 실행 파일을 빌드하기에 앞서 생성해야 할 의존성이 있는 메시지 및 dynamic reconfigure가 있다면 우선적으로 이를 수행하라는 설정이다.
  my_first_ros_pkg_node라는 실행 파일의 의존성을 기술한다.
  흔히 실행 파일을 빌드하기 앞서 메시지 파일ㅇ르 우선 생성할 때 가장 많이 사용된다.
  ```
  
- ```cmake
  target_link_libraries(my_first_ros_pkg_node
    ${catkin_LIBRARIES}
  )
  지정 실행 파일을 생성하기에 앞서 링크해야 하는 라이브러리와 실행 파일을 링크해주는 옵션이다.
  ```
  
- ```cmake
  cmake_minimum_required(VERSION 2.8.3)
  project(my_first_ros_pkg)
  find_package(catkin REQUIRED COMPONENTS roscpp std_msgs)
  catkin_package(CATKIN_DEPENDS roscpp std_msgs)
  include_directories(${catkin_INCLUDE_DIRS})
  add_excutable(hello_world_node src/hello_world_node.cpp)
  target_link_libraries(hello_world_node ${catkin_LIBRARIES})
  ```

### 4.9.4. 소스 코드 작성

- CMakeLists.txt 파일의 실행 파일 생성 부분(add_executable)에서 다음과 같이 설정했다.

  - ```cmake
    add_excutable(hello_world_node src/hello_world_node.cpp)
    ```

- ```c++
  //hello_world_node.cpp
  
  #include <ros/ros.h>
  #include <std_msgs/String.h>
  #inlcude <sstream>
  
  int main(int argc, char **argv){
      ros::init(argc, argv, "hello_world_node");
      ros::NodeHandle nh;
      ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("say_hello_world", 1000);
      ros::Rate loop_rate(10);
      int count = 0;
      
      while(ros::ok()){
          std_msgs::String msg;
          std::stringstream ss;
          ss << "hello world" << count;
          msg.data = ss.str();
          ROS_INFO("%s", msg.data.c_str());
          chatter_pub.publish(msg);
          ros::spinOnce();
          loop_rate.sleep();
          ++count;
      }
      return 0;
  }
  ```

### 4.9.5. 패키지 빌드

- ROS 패키지의 프로파일 을 갱신한다. 앞서 제작한 패키지를 ROS 패키지 목록에 반영하는 명령어로 필수 사항은 아니지만 새로운 패키지를 생성한 후에 갱신하면 이용하기 편하다.

- ```
  $ rospack profile
  ```

- 캐킨 빌드이다. 캐킨 작업 폴더로 이동하여 캐킨 빌드를 해주자.

- ```
  $ cd ~/catkin_ws && catkin_make
  ```

### 4.9.6 노드 실행

- ```
  $ roscore
  ```

- ```
  $ rosrun my_first_ros_pkg hello_world_node
  ```



표윤석, 조한철, 정려운, 임태훈. 『ROS 로봇 프로그래밍』
https://book.naver.com/bookdb/book_detail.nhn?bid=12443870
