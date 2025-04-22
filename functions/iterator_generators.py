l = [1, 2, 3, 4, 5] #works similarly for tuple, set

itr = iter(l)

print(next(itr))
print(next(itr))
print(next(itr))


def Day():
    L = ['sun', 'mon', 'Tue', 'wed', 'thurs', 'Fri', 'sat']
    i = 0

    while True:
        x = L[i]
        i = (i+1) % 7
        yield x

d = Day()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))


