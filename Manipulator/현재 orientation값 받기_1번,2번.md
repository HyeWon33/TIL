1. getCurrentState() 출력

   > 0x55a44e7049b0
   - https://github.com/ros-planning/moveit_tutorials/blob/melodic-devel/doc/move_group_interface/src/move_group_interface_tutorial.cpp#L170

   - 이거 따라서 해봤는데 joint1 잘 돌아간다. 오마이굿니스

   - ```
     const robot_state::JointModelGroup* joint_model_group =
           arm.getCurrentState()->getJointModelGroup(PLANNING_GROUP);
     
         moveit::core::RobotStatePtr current_state = arm.getCurrentState();
     
         std::vector<double> joint_group_positions;
         current_state->copyJointGroupPositions(joint_model_group, joint_group_positions);
         
         joint_group_positions[0] = -1.0;  // radians
         arm.setJointValueTarget(joint_group_positions);
     
         arm.move();
     ```

   - <img src="https://user-images.githubusercontent.com/52944554/171343266-fc08ed41-146b-425c-847a-dd9f33804d1a.png" alt="2번" style="zoom:50%;" />

2. getCurrentState자리에 getCurrentPose를 넣어보고 출력해보자

   - 넣었더니 arm에 빨간 줄
   - "geometry_msgs::PoseStamped"에서 "moveit::core::RobotStatePtr"(으)로의 사용자 정의 변환이 적절하지 않습니다.C/C++(312)
   - 형이 안 맞나보다..



현재 orientation값 받기는 조금 더 고민해보자.