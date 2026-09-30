import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleListener(Node):
    def __init__(self):
        super().__init__("simple_listener")
        self.subscription = self.create_subscription(
            String,
            "demo_message",
            self.on_message,
            10,
        )

    def on_message(self, message):
        self.get_logger().info(f"Received: {message.data}")


def main(args=None):
    rclpy.init(args=args)
    node = SimpleListener()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
