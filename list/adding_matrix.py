L1 = [[1, 2, 3, 4],[1, 2, 3, 4], [1, 2, 3, 4]]
L2 = [[5, 6, 7, 8],[5, 6, 7, 8], [5, 6, 7, 8]]

L3 = []

for i in range(len(L1)):
    S = []
    for j in range(len(L1[0])):
        S.append(L1[i][j] + L2[i][j])
    L3.append(S)
print(L3)
