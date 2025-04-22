


def invert(Before):
    After = {}
    for k, v in Before.items():
        After[v] = k
    return After


Before = {'a':10, 'b':20, 'c':30, 'd':40}
t1 = invert(Before)
print(t1)

print("================")

