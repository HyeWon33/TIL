# 현재 orientation값 받기

팔을 작동시키는데 회전 각은 그대로 하고싶다. 내가 넣은 값이라면 계산해서 넣을 수 있겠지만 만약 받아온 값을 그대로 하고싶다면? 

아 근데 생각해보니까 orientation값은 base 기준으로 계산한건데? orientation을 그래로 하고 position만 바꾸고 싶은데… 그럼 어떻게 해야 할까?

moveit tutorials에 **move_group_interface_tutorial.cpp**

[https://github.com/ros-planning/moveit_tutorials/blob/melodic-devel/doc/move_group_interface/src/move_group_interface_tutorial.cpp#L170](https://github.com/ros-planning/moveit_tutorials/blob/melodic-devel/doc/move_group_interface/src/move_group_interface_tutorial.cpp#L170)

```jsx
// To start, we'll create an pointer that references the current robot's state.
// RobotState is the object that contains all the current position/velocity/acceleration data.
moveit::core::RobotStatePtr current_state = move_group.getCurrentState();
//
// Next get the current set of joint values for the group.
std::vector<double> joint_group_positions;
current_state->copyJointGroupPositions(joint_model_group, joint_group_positions);

// Now, let's modify one of the joints, plan to the new joint space goal and visualize the plan.
joint_group_positions[0] = -1.0;  // radians
move_group.setJointValueTarget(joint_group_positions);
```

보면 getCurrentState()함수가 현재 position을 받아오는 것 같다.

만약 getCurrentState()가 진짜 현재 position을 받아온다면…

**moveit::planning_interface::MoveGroupInterface Class Reference**을 더 봐보니까.. getCurrentPose()가 있어. 근데 나는 이걸 단순히 현재 pose를 출력하는데 사용했는데 위의 방식처럼 사용해보면?

근데 getCurrent~()위에 설명에 Query current robot state라는데 Query가 데이터베이스에 정보를 요청하는 것이라고 한다. 그리고 데이터베이스에게 특정한 데이터를 보여달라는 사용자의 요청을 말하기도 한다.

setPoseTarget()함수가 3개 있는데

1. [Eigen](https://sunggoo.tistory.com/36) : 선형 대수 관련 알고리즘들을 해결해주는 C++ 기반의 템플릿 라이브러리
2. Pose
3. PoseStamped : header, pose

- a PoseTarget (Position, Orientation, or Pose) specifies the pose of one or more end effectors (and the planner can use any ***joint values*** that reaches the pose(s)).
    - a PoseTarget(위치, 방향 또는 자세)은 하나 이상의 엔드 이펙터의 자세를 지정합니다(그리고 설계자는 포즈에 도달하는 모든 결합 값을 사용할 수 있습니다).
    

Only one or the other is used for planning. 

Calling any of the set*JointValueTarget() functions sets the current goal target to the JointValueTarget. 

Calling any of the **[setPoseTarget()](http://docs.ros.org/en/melodic/api/moveit_ros_planning_interface/html/classmoveit_1_1planning__interface_1_1MoveGroupInterface.html#a28a6cebdb01f4f8cadc829b36855182a)**, **[setOrientationTarget()](http://docs.ros.org/en/melodic/api/moveit_ros_planning_interface/html/classmoveit_1_1planning__interface_1_1MoveGroupInterface.html#a718268743cb7a60268803c8840d63a75)**, **[setRPYTarget()](http://docs.ros.org/en/melodic/api/moveit_ros_planning_interface/html/classmoveit_1_1planning__interface_1_1MoveGroupInterface.html#a7f43684b3ccf3788d758c2aafa887353)**, **[setPositionTarget()](http://docs.ros.org/en/melodic/api/moveit_ros_planning_interface/html/classmoveit_1_1planning__interface_1_1MoveGroupInterface.html#a417e37154a0f276de9ab70bae2fcad32)** functions sets the current goal target to the Pose target.

둘 중 하나만 계획에 사용됩니다.

set*JointValueTarget() 함수를 호출하면 현재 목표 목표가 JointValueTarget으로 설정됩니다.

중 하나를 호출한다. 함수는 current goal target을 Pose target으로 설정합니다.

**setOrientationTarget()**은 쿼터니언 값을 넣는다.

그래서 5월 30일에

1. getCurrentState를 출력해보자
2. getCurrentState자리에 getCurrentPose를 넣어보고 출력해보자
3. JointValue Target 해보기 (실제)
4. Pose Target해보기 (실제)
5. Gripper 해보기 (실제)
6. 손 끝 제어 해보기 (실제)