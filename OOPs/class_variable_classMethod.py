from itertools import count


class Cuboid:
    count = 0
    def __init__(self, l, b, h):
        print(id(self))
        self.length = l
        self.breadth = b
        self.height = h
        Cuboid.count += 1

    def lidarea(self):
        return self.height * self.breadth

    def volume(self):
        return self.length * self.breadth * self.height
    @classmethod
    def countCuboid(cls):
        print(cls.count)



c1 = Cuboid(10, 5, 8)
print(Cuboid.count)

c2 = Cuboid(1, 2,3)
Cuboid.countCuboid()
