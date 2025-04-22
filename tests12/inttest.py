n = 1234
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
print(rev)

n = 1234
sums = 0
while n > 0:
    r = n % 10
    n = n // 10
    sums = sums + r
print(sums)

n = 1234
counts = 0
while n > 0:
    n = n // 10
    counts += 1
print(counts)

n = 1234
esum = 0
osum = 0
while n > 0:
    r = n % 10
    n = n // 10
    if r % 2 == 0:
        esum = esum + r
    else:
        osum = osum + r


print(esum, osum)

for i in range(0, 5):
    for j in range(0, 5):
        if i >= j:
            print("*", end="")
    print(" ")

