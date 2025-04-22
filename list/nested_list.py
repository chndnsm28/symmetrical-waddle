A = [[1, 2, 3], [4, 5, 6], [7 , 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7 , 8, 9]]
print(A)
C = []
print(len(A))
print(len(A[0]))
for i in range(len(A)):
    s = []
    for j in range(len(A[0])):
        s.append(A[i][j] + B[i][j])
    C.append(s)
print(C)