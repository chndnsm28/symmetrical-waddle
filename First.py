x = 10
y = 20
print("sum is", x+y)
x = "Chandan"
print(x[1])


s1 = 'hello'
s2 = s1 + " chandan"
print(s2)

for i in range(len(s1)-1, -1, -1):
    print(s1[i], end= '')
print()

print(s1[0:len(s1):1])

print(s1[::2])
print(s1[::])
print(s1[::-1])
print(s1[-1:-len(s1)-1:-1])

print(s1[-1: -len(s1)-1: -1])

print(s1[0:len(s1):1])

print('x' not in s1)

s2 = "chandan"
print(s1>s2)


print(s2.find('h'))
print(s2.count('a'))

s3 = "chandan loves rekha"
s4 = s3.partition(' ')
print(s4[2])

s5 = 'Subtotal (2 items)'
s6 = s5.partition(' ')
print(s6[2])





