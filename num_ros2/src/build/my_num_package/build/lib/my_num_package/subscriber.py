#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class NumSubscriber(Node):
    def __init__(self):
        super().__init__("num_subscriber")
        self.subscription = self.create_subscription(
            Int32MultiArray,
            "num_topic",
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        a = msg.data[0]
        b = msg.data[1]
        sum_ab = a + b
        self.get_logger().info(f"收到：{a} + {b} = {sum_ab}")

def main(args=None):
    rclpy.init(args=args)
    node = NumSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
