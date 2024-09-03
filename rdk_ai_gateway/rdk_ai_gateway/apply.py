import rclpy
from rclpy.node import Node
import vocano_apply

class ApplyNode(Node):
    def __init__(self):
        super().__init__('apply_node')
        logger = self.get_logger()
        vocano_apply.apply(logger)


def main(args=None):
    rclpy.init(args=args)
    node = ApplyNode()

    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
