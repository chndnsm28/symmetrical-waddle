def flattning(L):
    for e in L:
        if hasattr(e, '__iter__'):
            yield from flattning(e)
        else:

            yield e



L= [1,[2,3],4,5]
f = flattning(L)
print(next(f))
print(next(f))
print(next(f))
print(next(f))