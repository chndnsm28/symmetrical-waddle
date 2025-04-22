class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def getLength(self):
        return self.length

    def setLength(self, l):
        self.length = l

r1 = Rectangle(10, 5)
print(r1.area())
r1.setLength(15)
print(r1.area())
print(r1.getLength())
