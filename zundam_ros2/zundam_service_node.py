import rclpy    # ROS 2 Python モジュールのインポート
from rclpy.node import Node # rclpy.node モジュールから Node クラスをインポート
from zundam_ros2.srv import StringCommand

class ZundamService(Node): # Zundam サービスクラス
    def __init__(self): # コンストラクタ
        super().__init__('zundam_service') #基底クラスコンストラクタの呼び出し
        # サービスの生成（サービス型，サービス名，コールバック）
        self.service = self.create_service(StringCommand, 'command', self.callback)
        self.food = ['apple', 'banana', 'candy']

    def callback(self, request, response): # コールバック
        time.sleep(10)
        for item in self.food:
            if item in request.command:
                response.answer = 'はい，これです．'
                return response
        response.answer = '見つけることができませんでした．'
        return response