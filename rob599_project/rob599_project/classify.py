import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
# from tflite_support.task import core
# from tflite_support.task import processor
# from tflite_support.task import vision
import cv2
from cv_bridge import CvBridge
import random
import time

class ImageProcessingNode(Node):
    def __init__(self):
        super().__init__('image_processing_node')
        # Bin Parameters
        self._UNLOCK_THRESHOLD = 0.6
        self.get_logger().info(f'Thresold for recycling must be over {self._UNLOCK_THRESHOLD}')
        self.get_logger().info('-----')
        # Classification Model Parameters
        _MAX_RESULTS = 3
        _SCORE_THRESHOLD = 0.20
        _NUM_THREADS = 4
        
    
        # model_path = f'./models/{model}'
        # # Initialize the image classification model
        # base_options = core.BaseOptions(
        #     file_name=model_path, use_coral=False, num_threads=_NUM_THREADS)
        # # Enable Coral by this setting
        # classification_options = processor.ClassificationOptions(
        #     max_results=_MAX_RESULTS, score_threshold=_SCORE_THRESHOLD)
        # options = vision.ImageClassifierOptions(
        #     base_options=base_options, classification_options=classification_options)
        
        # self.classifier = vision.ImageClassifier.create_from_options(options)
        self.bridge = CvBridge()


        self.current = time.time()
        self.sub1 = self.create_subscription(
            Image,
            'camera_image',
            self.image_callback,
            10)
        self.pub1 = self.create_publisher(Bool, 'sort_item', 10)


    def image_callback(self, msg):
        rgb_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")
        self.get_logger().info('Motion triggered')
        self.current = time.time()
        flag = False
        while flag is not True:
            if time.time() > (self.current + 1):
                # Create TensorImage from the RGB image
                # tensor_image = vision.TensorImage.create_from_array(rgb_image)
                # # List classification results
                # categories = self.classifier.classify(tensor_image)

                # best_guess = max(categories.classifications[0].categories, key=lambda x:x.score)
                # category_name = best_guess.category_name
                # score = best_guess.score
                category_name = random.choice(['nonRecyclable', 'Plastic', 'Glass', 'Aluminum'])
                score = random.random()

                # Decide to unlock or not
                # Change based on classificationn
                sort_item = Bool()
                
                if("nonRecyclable" not in category_name and score > self._UNLOCK_THRESHOLD):
                    sort_item.data = True
                    self.get_logger().info('%s (%.3f)' %(category_name, score))
                else:
                    sort_item.data = False
                    self.get_logger().info('%s (%.3f)' %(category_name, score))

                self.pub1.publish(sort_item)
                flag = True

def main(args=None):
    try: 
        rclpy.init(args=args)
        image_processing_node = ImageProcessingNode()
        rclpy.spin(image_processing_node)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
