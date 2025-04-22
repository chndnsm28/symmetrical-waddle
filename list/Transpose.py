L1 = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

L2 = []

for i in range(len(L1[0])):
    S = []
    for j in range(len(L1)):
        S.append(L1[j][i])
    L2.append(S)
print(L2)
