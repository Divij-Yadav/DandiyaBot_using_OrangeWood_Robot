#!/usr/bin/env python3


import time
import sys
import signal

from owl_robot_sdk import OwlSimClient

#MoveIt Config Group name

class TestOwlSimClient:
    def __init__(self,group_name,gripper_group):
        self.group_name = group_name

        signal.signal(signal.SIGINT, self.signal_handler)

        print("Application is running. Press Ctrl+C to exit.")

        self.client = OwlSimClient(self.group_name,gripper_group,5,True)



        self.get_sdk_api()
        self.set_sdk_api()



    def signal_handler(self,sig, frame):
        print("Interrupt received, closing application.")
        sys.exit(0)

    #Testing Get APIs of SDK
    def get_sdk_api(self):

        #Robot Running Status
        status = self.client.is_running()
        print ("Robot Running Status:= ",status)

        #Robot Version
        version = self.client.get_version()
        print ("Robot Motion Group:= ", version)


        #Get Value of TCP 
        tcp_pose = self.client.get_tcp()
        print ("Robot TCP position:= ", tcp_pose)


        #Get Value of Joints
        joint_val = self.client.get_joint()
        print ("Robot Joint position:= ", joint_val)


        #Get TCP Position
        tcp_position = self.client.get_tcp_position()
        print ("Robot TCP Position: ", tcp_position)


        #Get TCP Orientation Quaternion
        tcp_orient_quat = self.client.get_tcp_orientation("quat")
        print("Robot Orientation Quaternion:= ", tcp_orient_quat)


        #Get TCP Orientation Euler angle
        tcp_orient_euler = self.client.get_tcp_orientation("euler")
        print("Robot Orientation in Euler:= ", tcp_orient_euler)

    def set_home(self):

        self.client.set_home()

        #self.client.set_gripper("open",1,"state")
        #get_gripper = self.client.get_gripper_val()

        time.sleep(1)



    def move_block_1(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] - 0  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] + 0.209  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 0.431 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] + 0.005  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] - 0.598  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 3.1 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)

    def move_block_2(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] - 0  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)
        
        current_joint_pose_goal[1] = current_joint_pose_goal[1] - 0  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] - 1.813 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] + 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] -0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] - 3.138 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)
        
    def move_block_3(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] + 1.102  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)
        
        current_joint_pose_goal[1] = current_joint_pose_goal[1] + 0.722  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 0.928 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] - 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] -0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 0  # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)


    def move_block_4(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] - 1.937  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] - 0  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 0 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] + 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] - 0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 0 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)



        
    def move_block_5(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] - 1.092  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] - 1.848  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 0.994 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] - 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] - 0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] - 0 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)


    def move_block_6(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] + 4.216  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] - 0  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 0 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] - 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] - 0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 0 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)


    def move_block_7(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] + 1.032 # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] + 0.728  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] + 1.206 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] - 0.012  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] - 0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 0.024 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)


    def move_block_8(self):

        current_joint_pose = self.client.get_joint()
        current_joint_pose_goal = current_joint_pose

        current_joint_pose_goal[0] = current_joint_pose_goal[0] + 0  # change required in base joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[1] = current_joint_pose_goal[1] - 0.015  # change required in shoulder joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[2] = current_joint_pose_goal[2] - 0.639 # change required in elbow joint
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[3] = current_joint_pose_goal[3] - 0  # change required in wrist joint 1
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[4] = current_joint_pose_goal[4] + 0  # change required in wrist joint 2
        status=self.client.move_to_joint(current_joint_pose)

        current_joint_pose_goal[5] = current_joint_pose_goal[5] + 0 # change required in wrist joint 3
        status=self.client.move_to_joint(current_joint_pose)



        self.client.close()


    #Set SDK APIs
    def set_sdk_api(self):
     
     self.set_home()
     self.move_block_1()
     self.move_block_2()
     self.move_block_3()
     self.move_block_4()
     self.move_block_5()
     self.move_block_6()
     self.move_block_7()
     self.move_block_8()
     self.move_block_9()
     self.move_block_10()
     self.move_block_11()
     self.move_block_12()



        


if __name__ == "__main__":
    testowl = TestOwlSimClient("arm","gripper")


