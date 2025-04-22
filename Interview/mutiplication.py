#Write a Python code to display a multiplication table using for loop
n=[5]
table = list(map(lambda x,y: x*y, list(range(1,11)), n*10))
print(table)

#swap two variables

a =10
b= 20

temp = 0

temp = a
a = b
b = temp
print(a , b)