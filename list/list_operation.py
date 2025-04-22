l1 = [10,20,30,40,40]

print(l1[::-1])

for i in range (-1,-(len(l1)+1), -1):
    print(l1[i])


#extending a list
l1[len(l1):] = [50, 60]
print(l1)
print(l1.index(20,0,5))
print("----------------")
print(l1)
l2 = l1.reverse()
print("----------------")
print(l2)