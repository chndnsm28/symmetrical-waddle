from typing import Callable, Any, Generator

l1 = [x for x in range(10)]
print(l1)

l2 = [x**2 for x in range(1, 6)]
print(l2)

l3 = [x for x in (1,2,3,4,5,6,7,8,9,10) if x%2 == 0]
print(l3)

l4 = [x.lower() for x in "PYthon"]
print(l4)


l5 = [x for x in 'ch#$a%4nd%a$n' if x.isalpha()]
print(l5)

r = ''.join(l5)
print(r)

