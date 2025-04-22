from tkinter import E

s = 'x=10\ny=20\nprint(x+y)'
exec(s)

a = eval('3*5+13/2')
print(a)




def even(x):
        if x % 2 == 0:
            return True
        else:
            return False

L = [3,2,7,6,8,9]
f = filter(even,L)
for i in f:
    print(i)
print("_____________")

m = filter(lambda x: x > 4, L)
for i in m:
    print(i)

print("-----------")

n =12.4567
print(format(n, E))

L1 = [10, 20, 30]
L2 = [11, 22, 33, 44, 55]

m = map(lambda x,y: x+y, L1,L2)

print(list(m))
