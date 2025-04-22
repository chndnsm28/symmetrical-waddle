l1 = list((1,2,3,4,5,6))
print(l1)
print(l1[2:5])
print(l1[1:6:2])
print(l1[-1:-len(l1)-1:-1]) #reverese printing
print(l1[::-1])

l1[0:2] = [10, 20,30,40]
print(l1)
print(l1)
l3 = l1.extend([100,200,300,400])
print(l3)


l4 = [10,20,30]
l4.extend([40,50,60])
print(l4)

l5 = [4, 5, 6, 7, 8]
l6 = [2, 3, 4]
l7 = []

for i in range (len(l5)):
    if len(l5) != len(l6):
        l6.append(0)
print(l6)

for j in range (len(l6)):
   l7.append(l5[j]+l6[j])

print(l7)

