def max(a, b, c):
    if a > b and a > c:
        print(a, "is greater than ",b, "and ", c)
    elif b > a and b > c:
        print(b, "is greater than ", a, "and ", c)
    else:
        print(c, "is greater than ", a, "and ", b)

max(10,7,11)