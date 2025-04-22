


class Cuboid:
    def __init__(self, l, b, h):
        print(id(self))
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.height * self.breadth

    def volume(self):
        return self.length * self.breadth * self.height


c1 = Cuboid(10, 5, 8)
print(id(c1))
area = c1.lidarea()
print("area of the cuboid is :", area)
print("volume of cuboid is: ", c1.volume())
