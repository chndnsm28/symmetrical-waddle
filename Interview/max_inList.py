#How can you find the largest number in a list
#factorial

def fact(n):
    if n == 0:
        return 1
    else:
        res  = n * fact(n-1)
        return res
print(fact(0))



