import time
import rclpy    # ROS 2 Python モジュールのインポート
import os
from rclpy.node import Node # rclpy.node モジュールから Node クラスをインポート
from zundam_interfaces.srv import StringCommand # zundam_interfaces.srv モジュールからカスタムメッセージ型 StringCommand をインポート
from playsound import playsound

class ZundamService(Node): # Zundam サービスクラス
    def __init__(self): # コンストラクタ
        super().__init__('zundam_service') #基底クラスコンストラクタの呼び出し
        # サービスの生成（サービス型，サービス名，コールバック関数）
        self.service = self.create_service(StringCommand, 'command', self.callback)
        self.food = ['apple', 'banana', 'candy']

    def callback(self, request, response): # コールバック
        #time.sleep(5)
        # for item in self.food:
        #     if item in request.command:
        #         response.answer = 'はい，これです．'
        #         return response
        # response.answer = '見つけることができませんでした．'
        #playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../zundam_ros2/zundam_service/voice/001_ずんだもん（ノーマル）_僕の名前はずんだも….wav'))
        playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_ros2/zundam_service/voice/001_ずんだもん（ノーマル）_僕の名前はずんだも….wav")
)
        return response
    
    
def main():  # main関数
    rclpy.init() # 初期化
    node = ZundamService() # ノードの生成
    try: # 例外処理．美しく終わるため
        rclpy.spin(node) # ノードの処理．コールバックを繰り返し呼び出す
    except KeyboardInterrupt:
        print("Ctrl+C が押されました．")
    finally:
        rclpy.shutdown() # 終了処理
        print('プログラム終了')