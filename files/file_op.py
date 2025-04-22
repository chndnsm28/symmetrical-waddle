file = open("prop.txt", 'r')
print(file.name)
print(file.mode)
print(file.closed)
lines = file.readlines()
print(lines)
for line in lines:
    print(line, end='')
l = file.readline()
print(l)
file.close()

file = open("writedemo.txt", 'w')

str1 = ['I am a programmer\n', 'with python language\n', 'good one\n']
file.writelines(str1)