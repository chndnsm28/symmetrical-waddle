class Arith:
    def sum(self, a, b):
        return a + b

a = Arith()
print(a.sum('Chandan ', 'Rekha'))
print(a.sum(3, 2))
print(a.sum(3.3, 2.3))
#print(a.sum(3, 2, 19))  to solve this

print("--------------------")
class Arith1:
    def sum(self, a, b, c=None):
        s = a + b
        if c is None:
            return s
        else:
            return s+c

a = Arith1()
print(a.sum(2, 9, 10))
print(a.sum(2, 9))