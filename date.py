date = input("enter the date in dd/mm/y format")

s = date.split('/')
print(s)

print("date is:", s[0])
print("month is", s[1])
print("year is:", s[2])