x = 'AbcDefGh'

lower = ''
upper = ''

for i in x:
    if i.islower():
        lower = lower+i
    else:
        upper += i

str = upper + lower
print(str)
