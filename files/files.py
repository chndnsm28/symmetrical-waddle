
file = open('myfile.txt', 'r')
str = file.read(6)
str = file.read(7)
print(str)

file.close()


file = open('newfile.txt', 'a')
file.write("hello bro\n")
file.write("hello hi\n")
file.write("hello guest\n")
file.write("hello chandan\n")

file.close()


