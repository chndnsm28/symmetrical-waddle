upper = 0
lower = 0
def Counting_U_l(str1):
    upper = 0
    lower = 0
    for i in str1:
        if i.islower():
            lower += 1
        elif i != '' and i.isupper():
            upper += 1

    print("Upper case count is: ", upper)
    print("lower case count is: ", lower)


str1 = "Chandan Is A Very Good TESTER"
Counting_U_l(str1)
