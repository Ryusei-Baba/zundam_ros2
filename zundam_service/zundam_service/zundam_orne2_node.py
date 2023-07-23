# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import rclpy
import time
import os
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from playsound import playsound


class ZundamSubscriber(Node): 
    def __init__(self):
        super().__init__('zundam_subscriber_node') 
        self.subscription = self.create_subscription(Twist,'cmd_vel', self.callback, 10)
        self.vel = Twist()
               
    def callback(self, Twist): 
        if Twist.linear.x > 0.2:
            playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_ros2/zundam_service/voice/001_ずんだもん（ノーマル）_ロボットが動くのだ.wav"))
        return response
        # self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z)) 
   
   
def main(args=None):
    rclpy.init(args=args)          # rclpyモジュールの初期化
    node = ZundamSubscriber() # ノードの作成
    rclpy.spin(node)      # コールバック関数が呼び出し
    node.destory_node()   # ノードの破壊
    rclpy.shutdown()               # rclpyモジュールの終了処理

# if __name__ == '__main__':
#     main()