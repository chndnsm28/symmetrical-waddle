dict1 = {}

dict1[1] = "Chandan"
print(dict1)

for i in range(1, 6):
    dict1[i] = i*2
print(dict1)

l1 = ["age", "height", "weight"]
l2 = [32, 6.1, 95.3]

dict2 = dict(zip(l1, l2))
print(dict2)

s1 = {7, 8, 10}
s2 = "ABC"

dict3 = dict(zip(s1, s2))
print(dict3)

dict4 = dict(zip([1,2,3], (10, 20, 30, 40, 50)))
print(dict4)

l1 = [10,20,20,10,30,40]
l2 = set(l1)
print(l2)
l3 = sorted(l2)
print(l3)
