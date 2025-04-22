punct = ''' %$#@!^&*()_+{}[];/?><'''

s = "chandan&*^%re^kH&a"

s1 = ''
for x in s:
    if x not in punct:
        s1 = s1 + x

print(s1)