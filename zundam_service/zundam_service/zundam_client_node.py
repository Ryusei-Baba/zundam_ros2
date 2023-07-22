# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import rclpy
from rclpy.node import Node
from zundam_interfaces.srv import StringCommand
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class ZundamClient(Node): 
    def __init__(self):
        super().__init__('zundam_client_node')
        self.client = self.create_client(Twist, 'cmd_vel')
        self.vel = Twist()
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')
        self.request = Twist.Request()

    def send_repuest(self, order):
        self.request.command = order 
        self.future = self.client.call_async(self.request)


def main(args=None): 
    rclpy.init(args=args)   
    node = ZundamClient() 
    order = input('cmd_velを受信中：')
    
    while rclpy.ok():
        def loop(self):
            if self.vel.linear.x > 0.1:
                node.send_repuest(order)
        rclpy.spin(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info(f'サービスの呼び出しは失敗しました．{e}')
            else:
                node.get_logger().info(
                    f'\n リクエスト：{node.request.command} -> レスポンス： {response.answer}')
                break
    rclpy.shutdown()
    print('プログラム終了')