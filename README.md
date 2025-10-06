# DandiyaBot_using_OrangeWood_Robot 

# Overview

<br>

In this project for our Introduction to Robotics course, we worked with the OrangeWood robot to perform a traditional Dandiya dance, integrating concepts of robotic motion, control, and safety. The goal was to design and simulate the robot’s movements in a way that would replicate the rhythmic and coordinated actions of the dance, which involves using sticks (called *dandiyas*) in sync with the music.

Our approach began with simulating the dance steps in the **Gazebo** simulation environment. In this environment, we defined and validated the movement trajectory by calculating the coordinates for the robot’s joints. This allowed us to visually test the robot’s motions before applying them to the physical hardware. The simulation helped us identify the appropriate angles and joint movements required for the dance.

To enable the robot to hold the *dandiya*, we designed a custom gripper and mounted it onto the robot's arm. The gripper was designed to securely hold the stick, while allowing the robot to mimic the gestures involved in the dance. After testing the movement in simulation, we transitioned to the physical robot.

For safety reasons, we initially set the robot's speed to a lower value to ensure smooth operation and avoid any risk of accidents. As we validated the robot’s performance, we gradually increased the speed to 50 degrees per second, which allowed the robot to move more fluidly while maintaining control. Throughout the project, we ensured that we stayed outside of the robot's workspace to maintain a safe distance while operating the robot and performing the dance.

This project not only gave us hands-on experience with robotic control, motion planning, and trajectory design but also highlighted the potential for robots to perform complex, creative tasks. By combining technology with cultural expression, we explored how robotics can be used in innovative and entertaining ways, blending tradition with modern technology.

<br>

# System Requirements

Ubuntu 20.04.6 LTS 

ROS Noetic

<br>

# Hardware Requirements

Orange Wood Labs Robot

<br>

# Installation Procedures

<br>

### Procedure to be followed to setup package in your PC 

The package created here is used to run simulations of the orange wood labs robot. This workspace is called orangewood_ws
   
1. Steps to setup a ROS workspace to build sim packages

   1.1 `mkdir -p ~/orangewood_ws/src`

   1.2 `cd ~/orangewood_ws/src`

   1.3 `git clone https://github.com/orangewood-co/orangewood_sim_stack.git`

   1.4 `cd ~/orangewood_ws`

2. Steps to Install depdencies 

   2.1 `rosdep install --from-paths src --ignore-src -r -y`

3. Steps to be followed to Build packages

   3.1 `catkin_make -j1`

   3.2 `echo "source ~/orangewood_ws/devel/setup.bash" >> /home/$USER/.bashrc`

   3.3 `source /home/$USER/.bashrc`  

<br>

### Procedure to install and setup OWL Robot SDK


Give the following command in the terminal to setup the OWL SDK

`pip install owl-robot-sdk`

<br>

### Procedure to setup workspace

Next we have created a new workspace named owl_ws which has the python program which executes the dandiya motion (We have assumed that you have installed ROS Noetic on your System)

1. Clone the `ITR-OWL` repository in the home directory using the command

   `git clone https://github.com/Debojit-D/ITR-OWL.git`

2. Create the workspace `owl_ws` using the following commands

   2.1 `mkdir -p ~/owl_ws/src`

   2.2 `cd ~/owl_ws/`

   2.3 `catkin_make`

   2.4 `source devel/setup.bash`

3. Copy the `owl_robot_description` package from `ITR-OWL` workspace and paste it in the source folder of `owl_ws`

4. Update your package using the comand 

   `catkin_make`

5. Next navigate to the source folder and create the scripts folder using the commands

   5.1 `cd src`

   5.2 `mkdir scripts`

6. Next open the scripts folder on VS code and create a program file named `Dandiya_moves.py` and remeber to make the file executeable.

<br>

# Tutorial

### Launching the RViz and Gazebo simulation environment 

Follow the steps listed below to launch the simulation environment in RViz and Gazebo

1. Navigate to the `orangewood_ws` workspace using the command

   `cd orangewood_ws`

2. Use the command below to launch 

   `roslaunch owl_bringup bringup.launch gripper:=robotiq2f85 world:=table  camera:=on sim:=on time:=5`

3. Refer to the `Orange wood labs sim_stack github repository` in references for more information on options availible in gripper, world, camera etc when launching

<br>

### Collecting data for joint states at different positions

1. Using the launched environment in RViz, go to the `joints` panel to change values of different joint angles at different positions

2. Check the feasibility of achieving new joint states from older ones using the `planning` option

3. Save the collected data as per your convinience (we have collected the data in the attached google sheet `Dandiya_Bot_ITR_Project_Data_for_positions`)

<br>

###  Simulating collected data

1. Use the API to create the program named `Dandiya_position_planning.py` in the `owl_robot_sdk_examples` folder (refer to attached `orangewood_ws` for complete workspace structure). Remeber to make the program executable.

2. Follow the instructions given for `Launching the RViz and Gazebo simulation environment` 

3. open the program named `Dandiya_position_planning.py` in VS Code and execute it.

<br>

### Steps to connect to hardware and launch program

1. Turn off all wifi connections 

2. Connect LAN cable

3. Open the wired connections settings

4. Go to the `IPv4` and select `Manual`

5. Enter address value `10.42.0.52` 

6. Enter Netmask value `255.255.255.0`

7. Enter Gateway value `10.42.0.1`

8. Check connection using the command 

   `ping 10.42.0.54`

9. Once connected to the hardware make sure that the OWL robot is in home position before starting

10. open your `Dandiya_moves.py` program and play

11. Be careful and follow all safety precautions when using the hardware


<br>

# Results

<br>

Successfully implemented individual joint control on our OWL robot in order to perform dandiya playing with human user (video attached). 

<br>

# Future Work

In this work motion is achieved by individual joint control, in future `Toppra` and `Moveit` packages can be integrated for better and more versatile motion planning  

# References

<br>

Orange wood labs sim_stack github repository

https://github.com/orangewood-co/orangewood_sim_stack

Orange Wood labs client bucket

https://owldoc.bitbucket.io/ 

Orange wood Labs repositories 

https://github.com/orangewood-co?tab=repositories

Orange wood labs repository for Introduction to Robotics 

https://github.com/Debojit-D/ITR-OWL 

Google sheet 'Dandiya_Bot_ITR_Project_Data_for_positions' 

https://docs.google.com/spreadsheets/d/1T_5XsdnaZXGy_VT5wqy3l2dDrPLoJrrXBZsJNx3ytBE/edit?usp=sharing 

<br>

# CONTRIBUTORS

<br>

Divij Yadav (M.Tech Mechanical Engineering student, IIT Gandhinagar)

Chetan Sharma (PhD Mechanical Engineering scholar, IIT Gandhinagar)   

Dharmesh Makvana   
