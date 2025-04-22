email = input("enter the email")

s = email.partition('@')
print("the username is ", s[0], "domain name is ", s[2])


atrate = email.find('@')

print("user name is: ", email[:atrate])
print("domain name is:", email[atrate+1:])