import rclpy    # ROS 2 Python モジュールのインポート
from rclpy.node import Node # rclpy.node モジュールから Node クラスをインポート
from std_msgs.msg import String # std_msgs.msg モジュールから String クラスをインポート
from zundam_ros2.srv import StringCommand # zundam_ros2.srv モジュールからカスタムメッセージ型 StringCommand をインポート

class ZundamClient(Node): 
    def __init__(self): # コンストラクタ
        super().__init__('zundam_client_node') #基底クラスコンストラクタの呼び出し
        self.client = self.create_client(StringCommand, 'command') # クライアントの生成
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')
        self.request = StringCommand.Request() # リクエストのインスタンス生成

    def send_repuest(self, order):
        self.request.command = order # リクエストに値の代入
        self.future = self.client.call_async(self.request) # サービスのリクエスト


def main(args=None): 
    rclpy.init(args=args)    # 初期化
    node = ZundamClient() # ノードの生成
    order = input('何を取ってきますか：')
    node.send_repuest(order)

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done(): # サービスの処理が終了したら
            try:
                responce = node.future.result() # サービスの結果をレスポンスに代入
            except Exception as e:
                node.get_logger().info(f'サービスの呼び出しは失敗しました．{e}')
            else:
                node.get_logger().info( # 結果の表示
                    f'\n リクエスト：{node.request.command} -> レスポンス： {response.answer}')
                break
    rclpy.shutdown()    # 終了処理
    print('プログラム終了')