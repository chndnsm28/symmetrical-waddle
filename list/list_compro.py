a = 'chan3634384d%%a@!!n'
l1 = [x for x in a if x.isalpha() ]
print(l1)


# create a list from 1 to 20 only if it is div by 3

l2= [x for x in range(1, 20) if x % 3 == 0]
print(l2)

l3 = [x**3 for x in range (1, 5)]
print(l3)

l4 = [x.upper() for x in "chanDan" ]
print(l4)

l5 = [x for x in range(10)]
print(l5)