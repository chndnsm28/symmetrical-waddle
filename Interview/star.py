def pyramid(n):

    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(1, i*2):
            print("*", end="")
        print()
pyramid(6)


print("--half--")
n= 5
for i in range(1, n+1):
    for j in range(1, i+1): # for j in range(n-i): inverted half
        print("*", end="")
    print()