from owl_client import OwlClient, Joint
import time


client = OwlClient("10.42.0.54")
jointSpeed = 50 #degrees/sec

# Wait for robot to be available
while not client.is_running():
    time.sleep(0.2)


#create joint goals for robot

position_1 =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # in radians
position_2 =[0.0, 0.21, 0.43, 0.01, 2.3, 3.1] # in radians
position_3 =[0.0, 0.21, -1.38, 0.01, 2.3, -0.04] # in radians
position_4 =[0.9, 1.23, -0.05, 0.01, 2.3, -0.4] # in radians
position_5 =[-1.04, 1.23, -0.05, 0.01, 2.3, -0.04] # in radians
position_6 =[-2.13, -0.62, 0.94, 0.01, 2.3, -0.04] # in radians
position_7 =[2.09, -0.62, 0.94, 0.01, 2.3, -0.04] # in radians
position_8 =[3.12, 0.11, 2.15, -0.01, 2.3, -0.06] # in radians
position_9 =[3.12, 0.1, 1.51, -0.01, 2.3, -0.06] # in radians

pos_arr = [position_1, position_2, position_3, position_4, position_5, position_6, position_7, position_8, position_9]

for pose in pos_arr:
    #valid configuration
    valid_position = Joint()
    valid_position.Base     = pose[0]
    valid_position.Shoulder = pose[1]
    valid_position.Elbow    = pose[2]  #(-90)
    valid_position.Wrist1   = pose[3]
    valid_position.Wrist2   = pose[4]
    valid_position.Wrist3   = pose[5]

    client.move_to_joint(valid_position, jointSpeed)
    time.sleep(1)

