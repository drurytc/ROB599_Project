import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
import time
# import RPi.GPIO as GPIO
import cv2
from cv_bridge import CvBridge
import random
import numpy as np
import os
from ament_index_python.packages import get_package_share_directory
from std_srvs.srv import SetBool



class SensorDataAcquisitionNode(Node):
    def __init__(self):
        super().__init__('sensor_data_acquisition_node')

        # GPIO.setmode(GPIO.BCM)
        # # GPIO Sensor Pins
        # self.MOTION_PIN = 4
        # self.BEAM_PIN1 = 5
        # self.BEAM_PIN2 = 6
        # self.BEAM_PIN3 = 13
        # self.BEAM_PIN4 = 16

        # # Initialize sensor pins
        # GPIO.setup(self.MOTION_PIN, GPIO.IN)
        # GPIO.setup(self.BEAM_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.BEAM_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.BEAM_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.BEAM_PIN4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Visualization parameters
        _FRAME_WIDTH = 800
        _FRAME_HEIGHT = 800
        _CAMERA_ID = 0
        self.motion_detected = Bool()
        # Start capturing video input from the camera
        self.bridge = CvBridge()
        self.current = time.time()
        # self.cap = cv2.VideoCapture(_CAMERA_ID)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, _FRAME_WIDTH)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, _FRAME_HEIGHT)

        self.camera_publisher = self.create_publisher(Image, 'camera_image', 10)
        self.motion_publisher = self.create_publisher(Bool, 'motion_detected', 10)
        self.motion_subscriber = self.create_subscription(
            Bool,
            'motion_detected',
            self.acquire_camera_data,
            10)
        self.break_beam_publisher = self.create_publisher(Bool, 'break_beam_triggered', 10)
        self.motion_data = True
        self.service = self.create_service(SetBool, 'set_motion_data', self.set_motion_data_callback)


    def acquire_camera_data(self, msg):
        if not msg.data:
            return
        else: 
            
            # success, image = self.cap.read()
            # if not success:
            #     self.get_logger().info(
            #         'ERROR: Unable to read from webcam. Please verify your webcam settings.')
                
            # image = cv2.flip(image, 1)
            # # Convert the image from BGR to RGB as required by the TFLite model.
            # rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Simulated camera capture
            # Get the path to the package's share directory
            package_share_directory = get_package_share_directory('rob599_project')
            image_relative_path = 'resource/test.png'
            im_path = os.path.join(package_share_directory, image_relative_path)
            rgb_image = cv2.imread(im_path)

            if rgb_image is None:
                self.get_logger().info('ERROR: Unable to load image from file.')
                return

            # Convert the image from BGR to RGB as required by the TFLite model
            rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

            # Convert the numpy array to ROS image message
            camera_image = self.bridge.cv2_to_imgmsg(rgb_image, encoding="rgb8")

            # Publish the image message
            if self.camera_publisher is not None:
                self.camera_publisher.publish(camera_image)
            else:
                self.get_logger().info('ERROR: Camera publisher not initialized.')

    def acquire_motion_data(self):
        # Simulated motion detection
        #<Place holder>
        self.motion_detected.data = self.motion_data # actual: GPIO.input(self.MOTION_PIN)
        #</Place holder>
        self.motion_publisher.publish(self.motion_detected)

    def acquire_break_beam_data(self, pin):
        # Simulated break beam sensor data
        break_beam_triggered = Bool()
        #<Place holder>
        break_beam_triggered.data = False  # actual: GPIO.input(pin)
        #<Place holder>
        self.break_beam_publisher.publish(break_beam_triggered)
    
    def set_motion_data_callback(self, request, response):
        self.motion_data = request.data
        response.success = True  # Assuming the motion data was successfully updated
        return response

    def main_loop(self):
    # Main loop for continuous sensor data acquisition
        timer_period = 5  # Set the timer period to 15 second
        self.create_timer(timer_period, self.timer_callback)  # Register the timer callback

    def timer_callback(self):
        # Timer callback function to acquire sensor data at regular intervals
        self.acquire_motion_data()
        pins = [5, 6, 13, 16]
        for pin in pins:
            self.acquire_break_beam_data(pin)

def main(args=None):
    try: 
        rclpy.init(args=args)
        sensor_node = SensorDataAcquisitionNode()
        sensor_node.main_loop()
        rclpy.spin(sensor_node)  # Start spinning the node
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
