def div(a, b):
    if b != 0:
        c = a // b
        return c

    else:
        raise Exception


a = int(input("enter the 1st no"))
b= int(input("enter the 2st no"))
try:

    result = div(a, b)
    print(result)

except:
    print("divide by zero error")
