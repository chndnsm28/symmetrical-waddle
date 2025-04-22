import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = int(input("enter the radius of the circle: "))

c1 = Circle(radius)
print(f'Area of Circle for radius = {radius}, is  {c1.area()}')
print(f'Perimeter of the circle for radius =  {radius}, is {c1.perimeter()} ')

