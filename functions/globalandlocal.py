
g=100
def fun(a = 10, b = 20):
    global g
    print(locals())
    g = g + 10
    print(g)

fun()
print(globals())
print(g)