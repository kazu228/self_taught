import math

# 1
class Apple:
    def __init__(self, w, c, s, a):
        self.weight = w
        self.color = c
        self.sweat = s
        self.area = a

x = Apple(100, "red", 10, "Japan")      
print(x.weight)
print(x.color)
print(x.sweat)
print(x.area)

# 2
class Circle:
    def __init__(self,  r):
        self. radius = r

    def area(self):
        result = self.radius * self.radius * math.pi
        return result

en = Circle(10)
print(en.area())

# 3

class Triangle:
    def __init__(self, te, ta):
        self.teihen = te
        self.takasa = ta

    def area(self):
        result = self.teihen * self.takasa / 2
        return result

san = Triangle(4, 8)
print(san.area())

# 6
class Hexagon:
    def __init__(self, ip):
        self.ippen = ip
    def calculate_perimeter(self):
        result = self.ippen * 6
        return result

ro = Hexagon(10)
print(ro.calculate_perimeter())

# class Hexagon():

#     def __init__(self, s1, s2, s3, s4, s5, s6):

#         self.s1 = s1

#         self.s2 = s2

#         self.s3 = s3

#         self.s4 = s4

#         self.s5 = s5

#         self.s6 = s6



#     def calculate_perimeter(self):

#         return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6



# a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)

# print(a_hexagon.calculate_perimeter())





