
import turtle
# ttributeError: 'Kame' object has no attribute 'screen'やられた！！　親クラスの__init__のすべてを子クラスの__init__が上書きしてしまう。
class Kame(turtle.Turtle):
    def __init__(self):
        super().__init__()  # 親クラスの__init__()をすべて呼び出してからshape()を書き換える super()は、親クラス
        self.shape('turtle')

kame_test = Kame()
kame_test.forward(100)
kame_test.left(120)
kame_test.forward(150)
