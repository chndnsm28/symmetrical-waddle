country = {}

for i in range (4):
    name = input("enter name ")
    if name[0].upper() not in country:
        country[name[0].upper()] = [name.capitalize()]
    else:
        country[name[0].upper()].append(name.capitalize())
print(country)