class Animal(object):
    def bark(self):
        print('bark something')

class Dog(Animal):
    def bark(self):
        print('bow bow')
        super().bark()  #親クラスのメソッド

dog = Dog()
dog.bark()
