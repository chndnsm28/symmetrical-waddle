s1 = input("enter the string 1")
s2 = input("enter the string 2")
print(s1)
print(s2)

if len(s1) != len(s2):
    print("not a anagram")
else:
    for x in s1:
        if x not in s2:
            print("not a anagram")
            break
    else:
        print("anagram")





