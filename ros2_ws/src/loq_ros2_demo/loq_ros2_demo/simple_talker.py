import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleTalker(Node):
    def __init__(self):
        super().__init__("simple_talker")
        self.publisher = self.create_publisher(String, "demo_message", 10)
        self.counter = 0
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        message = String()
        message.data = f"Hello ROS 2 Jazzy #{self.counter}"
        self.publisher.publish(message)
        self.get_logger().info(f"Published: {message.data}")
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = SimpleTalker()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
