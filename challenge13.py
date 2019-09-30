
# 3
class Shape:
    def what_am_i(self):
        string = "I am a shape."
        return string

# 1
class Rectangle(Shape):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3

class Square(Shape):
    def __init__(self, hen):
        self.hen = hen
    def calculate_perimeter(self):
        return self.hen * 4
    def change_size(self, num):  # 2
        self.hen = self.hen + num
        return self.hen 

re = Rectangle(1, 2, 3)
print(re.calculate_perimeter())

sq = Square(5)
print(sq.calculate_perimeter())
print(sq.change_size(-2))


rec = Rectangle(1, 2, 3)
print(rec.what_am_i())
sh = Square(10)
print(sh.what_am_i())

# 5
class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
    
class Rider:
    def __init__(self, name):
        self.name = name

r = Rider("Kazu")
print(r.name)
h = Horse("kei", r)
print(h.owner.name)  #コンポジション