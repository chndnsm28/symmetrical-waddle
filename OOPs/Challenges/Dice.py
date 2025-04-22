from random import *

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def random(self):
        return randint(1, self.sides)

d1 = Dice(12)
print(d1.random())

s1 = 'Subtotal (1 item):'
s2 = s1.split()

print(s2[1:])
for l in s2[1:]:
    print (', '.join(map(str, l)))
