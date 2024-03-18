# ROS-Enabled Recycling Bin Sorting System

## Overview
The ROS-Enabled Recycling Bin Sorting System project aims to optimize recycling processes by integrating ROS (Robot Operating System). Through this integration, we seek to develop a sophisticated system capable of efficiently sorting recyclable materials using sensors, image processing, and robotic control.

## Description
This project involves rewriting existing Python scripts from a senior capstone project into ROS-enabled modules. These modules will form the backbone of a recycling bin sorting system, facilitating seamless communication between sensors, image processing algorithms, and robotic actuators. Leveraging ROS ensures scalability and interoperability for future enhancements and integration with other ROS packages.

## Functionality
- **Sensor Data Acquisition:** ROS nodes will interface with sensors such as cameras, motion sensors, and break beam sensors to acquire raw data from the recycling bin.
- **Image Processing:** A dedicated ROS node will handle image processing tasks to classify recyclable materials based on the acquired sensor data.
- **Servo Control:** Another ROS node will control the servo mechanism responsible for sorting items into respective bins based on classification results.
- **Integration with ROS Ecosystem:** All ROS nodes will integrate with existing and future ROS packages, ensuring broader functionality and interoperability within the ROS ecosystem.

## Team Members and Responsibilities
- **Individual Project:** The proposer leads the project, responsible for rewriting Python scripts into ROS-enabled modules, system integration, testing, documentation, and project management.

## Grading Rubric
- **ROS Nodes without functionality:** 30 points
- **Sensor Data Processing:** 10 points
- **Servo Control:** 10 points
- **Documentation and Code Quality:** 10 points

## Conclusion
The ROS-Enabled Recycling Bin Sorting System offers an exciting opportunity to optimize recycling processes through ROS integration. By enhancing functionality and scalability, we aim to create a more efficient and sustainable solution for waste management. Should this proposal not align with project requirements, exploring alternative options to further develop ROS skills remains viable.

## Accomplishments
- **Development of ROS Nodes:** Initial ROS nodes have been developed for sensor data, classifying, and servo control.
- **ROS Environment Setup:** A ROS package has been created, and nodes have been set up within the environment.
- **Sensor Data & Image Processing Progress:** Framework for all sensor data and decisions of image processing have been established. All correct data and behavior has been implemented and is ready to be testted in a physical prototype.

---

# Setup & Structure

## Cloning into ROS Environment and Creating ROS Package

To clone the project into your ROS environment and set up a ROS package, follow these steps:

1. Navigate to your desired directory where you want to clone the project.

2. Open a terminal window and run the following command to clone the project repository:
   ```
   git clone <repository_URL>
   ```
   Replace `<repository_URL>` with the URL of the GitHub repository.

3. Once the repository is cloned, navigate into the project directory:
   ```
   cd <project_directory>
   ```
   Replace `<project_directory>` with the name of the directory where the project was cloned.

4. Next, create a ROS package within the project directory. Assuming you have ROS installed and set up properly on your system, run the following command:
   ```
   catkin_create_pkg <package_name> rospy roscpp
   ```
   Replace `<package_name>` with the desired name for your ROS package. You can add additional dependencies as needed.

5. After creating the ROS package, move all relevant files and directories from the cloned project into the newly created package directory.

6. Ensure that the package dependencies are properly set in the `package.xml` file within your ROS package directory.

7. Build your ROS workspace to compile the package:
   ```
   catkin_make
   ```

8. Source the newly created workspace to make the ROS package available in your environment:
   ```
   source devel/setup.bash
   ```

Now, your ROS package should be set up and ready to use within your ROS environment.
```
