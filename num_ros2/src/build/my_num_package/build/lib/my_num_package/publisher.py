#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class NumPublisher(Node):
    def __init__(self):
        super().__init__("num_publisher")
        self.publisher_ = self.create_publisher(Int32MultiArray, "num_topic", 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [10, 20]  # 发两个数：10 和 20
        self.publisher_.publish(msg)
        self.get_logger().info(f"发布：{msg.data[0]}, {msg.data[1]}")

def main(args=None):
    rclpy.init(args=args)
    node = NumPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
