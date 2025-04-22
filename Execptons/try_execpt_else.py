print("this is before try")

try:
    a = int(input("enter 1st no"))
    b = int(input("enter 2nd no"))
    c = a // b
    print("try executed successfully")

except ZeroDivisionError as e:
    print(e)

else:
    print("try executed without raising execption")

print("outside of try and execpt")

