class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x}, {self.y})'

pt_a = Point(10,12)
pt_b = pt_a
pt_b.x = 20
print(pt_a)
print(pt_b)
print(id(pt_a))
print(id(pt_b))

#Pointオブジェクトにはリストのようなcopyメソッドはない
import copy

pt_a = Point(10,12)
pt_b = copy.copy(pt_a)
pt_b.x = 20
print(pt_a)
print(pt_b)
print(id(pt_a))
print(id(pt_b))