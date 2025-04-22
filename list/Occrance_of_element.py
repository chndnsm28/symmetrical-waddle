from itertools import count

L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']
result = []

for i in range (len(L1)):
    if L1[i] not in result:
        result.append(L1[i])
        count = L1.count(L1[i])
        result.append(count)
print(result)







