from itertools import count

l1 = [1,2,3,3,4,5,4,5,6,7,5,6,8]
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)


print("----------")

l1 = [1,2,3,3,4,5,4,5,6,7,5,6,8]

i = 0
while i < len(l1):
    if l1.count(l1[i]) > 1:
        l1.remove(l1[i])
    else:
        i += 1
print(l1)

