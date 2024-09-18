import os
import rclpy
from rclpy.node import Node

from decode import api_infer
from rdk_ai_gateway_msg.srv import TextToText

class InferService(Node):
    
    def __init__(self):
        super().__init__('infer_service')
        self.srv = self.create_service(TextToText, "text_to_text", self.api_infer_cb)
        self.declare_parameter('bin_file', '/root/.ros/rdk_ai_gateway/auth.bin')
        self.bin_file = self.get_parameter('bin_file').get_parameter_value().string_value
        self.get_logger().info('bin_file is: ' + self.bin_file)
        # Check if the file exists
        if not os.path.exists(self.bin_file):
            self.get_logger().error(f"File '{self.bin_file}' does not exist. Shutting down.")
            return
        else:
            self.get_logger().info("Found auth.bin, the server if ready. Please pass in request.")
        self.shift = 99
        
    def api_infer_cb(self, request, response):
        self.get_logger().info("Receive request..")
        self.get_logger().info("The requested model is: " + request.model)
        self.get_logger().info("The requested input is: " + request.input)
        response.output = api_infer(self.bin_file, self.shift, request.input, request.model, self.get_logger())
        return response
    
def main():
    rclpy.init()
    infer_service = InferService()
    rclpy.spin(infer_service)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()