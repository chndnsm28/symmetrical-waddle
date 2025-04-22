#count no of digits

n =int(input("enter the digit"))
count = 0
while n > 0:
    n = n // 10
    count = count+1
print(count)

n = input("eter string")
vowels = "aeiou"
l1 = []

for i in n:
    count = 0
    if i in vowels:
        print(i, i.count(i)) #https://www.geeksforgeeks.org/python-count-display-vowels-string/



#find sum of digits

m = 123
sums = 0
while m > 0:
    r = m % 10
    sums = sums+ r
    m = m // 10

print(sums)

#reverse a number
num = 121
cp_num = num
rev = 0
while num > 0:
    r = num % 10
    num = num // 10
    rev = rev * 10 + r
print(rev)
if rev == cp_num:
    print("palindrome")
else:
    print("not a palindrome")



