# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import rclpy
from rclpy.node import Node
from zundam_interfaces.srv import StringCommand


class ZundamClient(Node): 
    def __init__(self):
        super().__init__('zundam_client_node')
        self.client = self.create_client(StringCommand, 'command')
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')
        self.request = StringCommand.Request()

    def send_repuest(self, order):
        self.request.command = order 
        self.future = self.client.call_async(self.request)


def main(args=None): 
    rclpy.init(args=args)   
    node = ZundamClient() 
    order = input('何を取ってきますか：')
    node.send_repuest(order)

    while rclpy.ok():
        rclpy.spin_once(node)
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