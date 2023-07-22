# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import time
import rclpy
import os
from rclpy.node import Node
from zundam_interfaces.srv import StringCommand
from playsound import playsound

class ZundamService(Node):
    def __init__(self):
        super().__init__('zundam_service')
        # サービスの生成（サービス型，サービス名，コールバック関数）
        self.service = self.create_service(StringCommand, 'command', self.callback)
        self.food = ['apple', 'banana', 'candy']

    def callback(self, request, response):
        playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_ros2/zundam_service/voice/001_ずんだもん（ノーマル）_ロボットが動くのだ.wav"))
        return response
    
    
def main():
    rclpy.init()
    node = ZundamService()
    try:
        rclpy.spin(node) 
    except KeyboardInterrupt:
        print("Ctrl+C が押されました．")
    finally:
        rclpy.shutdown()
        print('プログラム終了')