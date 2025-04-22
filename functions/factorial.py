def fact(n):
    if n == 0:
        return 1
    else:
        res = n * fact(n-1)
        return res
r = fact(3)
print(r)