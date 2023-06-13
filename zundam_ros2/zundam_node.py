import rclpy    # ROS 2 Python モジュールのインポート
from rclpy.node import Node # rclpy.node モジュールから Node クラスをインポート

class ZundamNode(Node): # ZundamNode クラス
    def __init__(self): # コンストラクタ
        super().__init__('zundam_node') #基底クラスコンストラクタの呼び出し
        #self.

def main(): # main() 関数
    rclpy.init()    # 初期化
    node = ZundamNode() # ノードの生成
    try:    # 例外処理．美しく終わるため
        rclpy.spin(node)    # ノードの処理
    except keyboardInterrupt:
        print('Ctrl+C が押されました．')
    rclpy.shutdown()    # 終了処理
    print('プログラム終了')