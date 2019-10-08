
class A:
    def spam(self):
       print('A')

class B(A):
    def spam(self):
       print('B')
       super().spam()  #super()が基底クラスになってる。

B().spam()  