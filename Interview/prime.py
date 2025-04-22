














start = 100
end = 200

for num in range(start, end+1):
    for i in range(2, end+1):
        if num % i == 0:
            break
    if num == i:
        print(i, end=' ')









