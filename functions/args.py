def fun(a,b, *args):
    return a+b, args



print(fun(2,3, "I love you"))

def fun1(a, b, c=0):
    return a, b, c

L1 = [10, 20, 30]
t1= list(fun1(L1[0], L1[1]))
print(t1)
