with open('abc.txt', 'rb')as f:
    print(f.read(1).decode())
    f.seek(3,0)
    print(f.read(1).decode())
    f.seek(-2,2)
    print(f.read(1).decode())
    print(f.tell())