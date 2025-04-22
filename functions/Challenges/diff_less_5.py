def dif(a, b):
    if abs(a - b) <= 5:
        return True
    else:
        return False

x = int(input("enter the first number"))
y = int(input("enter the second number"))

print(dif(x, y))


