# クラス変数は、あるクラスのすべてのインスタンスが共有する属性やメソッドのためにあり、
# インスタンス変数はそれぞれのインスタンスに固有のデータのためにある
class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)   #クラス変数は、全てのインスタンスに共有
print(e.kind)

print(d.name)   #インスタンス変数は、インスタンスが個別に値をもつ
print(e.name)