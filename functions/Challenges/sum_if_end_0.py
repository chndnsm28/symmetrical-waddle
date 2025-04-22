def add(L):
    sums = 0
    for i in range (len(L)):
        if L[i] % 10 == 0:
            sums = sums+L[i]
    return sums

L = [100, 123, 200, 234, 300]
result = add(L)
print(result)

