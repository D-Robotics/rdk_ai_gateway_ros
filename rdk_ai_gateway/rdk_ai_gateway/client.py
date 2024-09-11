import rclpy
from rclpy.node import Node
from rdk_ai_gateway_msg.srv import TextToText  # Adjust the import according to your service name

class InferClient(Node):

    def __init__(self):
        super().__init__('infer_client')
        self.client = self.create_client(TextToText, 'text_to_text')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.request = TextToText.Request()

        # Declare parameters
        self.declare_parameter('input_str', '晚上吃什么')
        self.declare_parameter('model', 'doubao-pro-128k')  # Default to 0, should be an integer

        # Retrieve parameters
        self.input_str = self.get_parameter('input_str').get_parameter_value().string_value
        self.model = self.get_parameter('model').get_parameter_value().string_value

    def send_request(self):
        self.request.input = self.input_str
        self.request.model = self.model
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    infer_client = InferClient()
    
    # Send the request using parameters
    response = infer_client.send_request()

    infer_client.get_logger().info(f'Result: {response.output}')

    infer_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
