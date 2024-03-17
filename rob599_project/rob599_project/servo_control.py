#!/usr/bin/env python3

# Serevo Control for Recycling Bin
#
# servo_control.py
#
# Timothy Drury
#
# This is starter code for the servo control thats subscribes to classification 
# to determine behavior. 

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from std_msgs.msg import Bool
from gpiozero import Servo
import time
from rpi_ws281x import PixelStrip, Color


class ServoControlNode(Node):
    def __init__(self):
        super().__init__('servo_control_node')
        self.sub1 = self.create_subscription(
            Bool,
            'sort_item',
            self.sort_item_callback,
            10)
        self.sub2 = self.create_subscription(
            Bool,
            'break_beam_triggered',
            self.lock_callback,
            10)
        
        buff = 0.60
        maxPW = (1.0 + buff) / 1000
        minPW = (1.0 - buff) / 1000
        # self.chooseServo = Servo(17, min_pulse_width=minPW, max_pulse_width=maxPW)
        # self.chooseServo.mid()
        # self.lockServo = Servo(27, min_pulse_width=minPW, max_pulse_width=maxPW)
        # self.lockServo.min()
        # self.chooseServo.value = None
        # self.lockServo.value = None

        self.curent = time.time()
        self.LED_PIN = 18
        # LED strip configuration:
        LED_COUNT = 16        # Number of LED pixels.
        LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA = 10          # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        # Create NeoPixel object with appropriate configuration.
        # self.LED = PixelStrip(LED_COUNT, self.LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        # self.LED.begin()

        self.total = 0
        self.Rec = 0
        self.nonRec = self.total - self.Rec

        self.sorted_items = {
            True: 'Recyclable',
            False: 'Non-recyclable',
            None:  None
        }

    def fill_color1(self, color):
        #for i in range(self.LED.numPixels()/2):
            # self.LED.setPixelColor(i, color)
            pass
        # self.LED.show()

    def fill_color2(self, color):
        #for i in range(self.LED.numPixels()/2, self.LED.numPixels()):
           # self.LED.setPixelColor(i, color)
           pass
        # self.LED.show()

    def clearLEDs(self):
        # self.fill_color1(Color(0,0,0))
        # self.fill_color2(Color(0,0,0))
        pass

    def sort_item_callback(self, msg):
        sort_recyclable = msg.data
        if sort_recyclable:
            self.sort_item(True)
        else:
            self.sort_item(False)

    def lock(self):
        # self.lockServo.max()
        self.fill_color2(Color(255,0,0)) # Full sign to Red
        self.get_logger().info('Bin Locked')
        # self.lockServo.value = None

    def sort_item(self, recyclable):
        flag = False
        self.current = time.time()
        while flag is not True:
            if time.time() > (self.current + 1):
                # Control the servo to sort the item
                if recyclable is None:
                    return
                elif recyclable:
                    # Rotate servo to deposit recyclable item into the respective bin
                    # self.chooseServo.max()
                    # duration = Duration(seconds=1) # Adjust the duration as needed
                    # rclpy.spin_until_future_complete(self, self.get_clock().now() + duration)  
                    # self.chooseServo.value = None  # Release servo to stop rotation
                    self.Rec += 1
                    self.total +=1
                    self.get_logger().info(f'Sorted into Recycling\n -----')
                    flag = True
                else:
                    # Rotate servo to deposit non-recyclable item into the respective bin
                    # self.chooseServo.min()
                    # duration = Duration(seconds=1) # Adjust the duration as needed
                    # rclpy.spin_until_future_complete(self, self.get_clock().now() + duration)
                    # self.chooseServo.value = None  # Release servo to stop rotation
                    self.total +=1
                    self.get_logger().info(f'Sorted into Waste\n -----')
                    flag = True
                # self.chooseServo.mid()
                # self.chooseServo.value = None  # Release servo to stop rotation
                    

    def lock_callback(self, msg):
        break_beam_state = msg.data
        if break_beam_state:
            self.lock()
        else:
            return

def main(args=None):
    try:
        rclpy.init(args=args)
        servo_node = ServoControlNode()
        rclpy.spin(servo_node)
        
    except KeyboardInterrupt:
        servo_node.get_logger().info(f'{servo_node.Rec} out of {servo_node.total} items were recycling')

if __name__ == '__main__':
    main()