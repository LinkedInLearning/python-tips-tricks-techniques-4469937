class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x}, {self.y})'
    

pt_a = Point(10,12)
pt_b = Point(20,24)
lst_a = [pt_a,pt_b]
lst_b = lst_a.copy()

print(id(lst_a))
print(id(lst_b))

for pt in lst_a:
    print(id(pt))

for pt in lst_b:
    print(id(pt))

import copy

pt_a = Point(10,12)
pt_b = Point(20,24)
lst_a = [pt_a,pt_b]
lst_b = copy.copy(lst_a)

print(id(lst_a))
print(id(lst_b))

for pt in lst_a:
    print(id(pt))

for pt in lst_b:
    print(id(pt))

import copy

pt_a = Point(10,12)
pt_b = Point(20,24)
lst_a = [pt_a,pt_b]
lst_b = copy.deepcopy(lst_a)    

print(id(lst_a))
print(id(lst_b))

for pt in lst_a:
    print(id(pt))

for pt in lst_b:
    print(id(pt))

