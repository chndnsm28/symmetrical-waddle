class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth


class Cuboid(Rectangle):
    def __init__(self, h, l, b):
        self.height = h
        super().__init__(l, b)

    


    def volume(self):
        return self.length * self.breadth * self.height

c1 = Cuboid(15, 10, 5)
print(c1.volume())
c2 = Cuboid(10,20, 5)
print(c2.area())
