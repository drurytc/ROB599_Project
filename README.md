# ROS-Enabled Recycling Bin Sorting System

[![Video Thumbnail](https://github.com/drurytc/ROB599_Project/blob/main/Video_thumbnail.png)](https://youtu.be/Z1QdZv_cf8U)

## Overview
This ROS-Enabled Recycling Bin Sorting System project aims to integrate ROS (Robot Operating System). In this project, the goal is to develop a system capable of sorting recyclable materials using sensors, image processing, and robotic control. This project will focus on behavior and simulated data.

## Description
This project involves rewriting existing Python scripts from a [senior capstone project](https://github.com/drurytc/SmartBin_Prototype.git) into ROS nodes. These nodes will define the behavior of of a recycling bin sorting system, facilitating  communication between sensors, image processing algorithms, and servos. Leveraging ROS ensures scalability and interoperability for future enhancements and integration with other ROS packages.

## Functionality
- **Sensor Data Acquisition:** ROS nodes will interface with sensors such as cameras, motion sensors, and break beam sensors to acquire raw data from the recycling bin.
- **Image Processing:** A dedicated ROS node will handle image processing tasks to classify recyclable materials based on the acquired sensor data.
- **Servo Control:** Another ROS node will control the servo mechanism responsible for sorting items into respective bins based on classification results.

## Team Members and Responsibilities
- **Individual Project:** The proposer leads the project, responsible for rewriting Python scripts into ROS and documentation.

## Grading Rubric
- **ROS Nodes without functionality:** 30 points
- **Sensor Data Processing:** 10 points
- **Servo Control:** 10 points
- **Documentation and Code Quality:** 10 points

## Conclusion
The ROS-Enabled Recycling Bin Sorting System offers an exciting opportunity to continue working on a senior project through ROS integration. I found I was not able to actaully try the code within the prototype due to time constraints of the capstone project goals and sponsor needs. However, all behavior is implmented and ready to be deployed and tested within the recycling prototype with some removal of comments and placeholders. With this in mind, I believe that I fulfilled most of the proposed goals. Enough to recieve the following break down of grading--- ROS Nodes: 30/30, Sensor Data Processing: 7/10, Servo Control: 7/10, and Documnetation: 7/10, due to the lack ability to test with real sensors.   

## Accomplishments
- **Development of ROS Nodes:** Initial ROS nodes have been developed for sensor data, classifying, and servo control.
- **ROS Environment Setup:** A ROS package has been created, and nodes have been set up within the environment.
- **Sensor Data & Image Processing Progress:** Framework for all sensor data and decisions of image processing have been established. All correct data and behavior has been implemented and is ready to be testted in a physical prototype.

---

# Setup & Structure

## Package Structure Overview

```
rob599_project/
│
├── build/                        # Contains build artifacts (generated during compilation)
│   └── ...
│
├── install/                      # Contains installed files (generated after compilation)
│   └── ...
│
├── log/                         
│   └── ...
│
├── resource/
│   ├── test.jpg            # Contains test image file
│   └── ...                     
│
├── src/                      # Contains ROS node scripts
│   ├── sensor_data.py
│   ├── classify.py
│   └── servo_control.py
│
├── launch/                       # Contains launch files for running nodes
│   └── classify_launch.py
│
├── test/                         
│   └── ...
│
├── package.xml                   # Package manifest
├── setup.cfg                     # Setup configuration file
└── setup.py                      # Setup script
```

## Cloning into ROS Environment and Creating ROS Package

To clone the project into your ROS environment and set up a ROS package, follow these steps:

1. Navigate to your desired directory where you want to clone the project.

2. Open a terminal window and run the following command to clone the project repository:
   ```
   git clone https://github.com/drurytc/ROB599_Project.git
   ```

3. Build your ROS workspace to compile the package:
   ```
   colcon build --symlink-install
   ```

4. Source the newly created workspace to make the ROS package available in your environment:
   ```
   source install/setup.bash
   ```
5. Once the repository is cloned, navigate into the project directory:
   ```
   cd rob599_project
   ```
6. Ensure that the package dependencies are properly set in the `package.xml` file within your ROS package directory.

7. Now, your ROS package should be set up and ready to use within your ROS environment. You should be able to launch all three nodes by calling the launch file.
   ```
   ros2 launch rob599_project classify_launch.py
   ```
8. Service call to simulate motion.
   ```
   ros2 service call /set_motion_data std_srvs/SetBool '{data: true}'
   ```
