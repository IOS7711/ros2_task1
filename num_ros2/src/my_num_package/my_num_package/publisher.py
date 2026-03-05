#!/usr/bin/env python3
import rclpy #导入库
from rclpy.node import #Node 提供节点基类
from std_msgs.msg import Int32MultiArray #导入整数集

class NumPublisher(Node):
    def __init__(self):
        super().__init__("num_publisher")
        self.publisher_ = self.create_publisher(Int32MultiArray, "num_topic", 10)#创建一个发布者
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = Int32MultiArray()#创建一个空的消息对象。
        msg.data = [10, 20]  # 发两个数：[0]10 和 [1]20
        self.publisher_.publish(msg)
        self.get_logger().info(f"发布：{msg.data[0]}, {msg.data[1]}")#打印

def main(args=None):
    rclpy.init(args=args) #初始化
    node = NumPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
