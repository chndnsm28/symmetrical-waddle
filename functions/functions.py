def add(item, L=[]):
    L.append(item)
    return L

l1 = [5, 10, 15]

print(add(3,l1))

print(add(9))
print(add(8))

print("-------------------")

def add(a,b,/,c,d, *, e,f):
    return a+b+c+d


print(add(1,2,3,d= 3,e=2,f=3))