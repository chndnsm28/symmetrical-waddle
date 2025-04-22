from collections import deque

l = [1, 2, 3, 4,5,5]
d = deque(l)
print(d)

d.append(6)
print(d)
d.appendleft(7)
print(d)
print(d.count(5))
d.extend([8, 9])
print(d)
d.extendleft([0, 11])
print(d)
d.pop()
d.popleft()
print(d)
d.rotate(2)
print(d)
d.reverse()
print(d)