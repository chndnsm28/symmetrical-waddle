dict1 = {1:'Java', 2:'Selenium', 3:'Python', 4:'Pytest'}

for x in dict1:
    print(x, dict1[x])

for x in dict1:
    print(x, dict1.get(x))

print(x, dict1[4]) #gives error if key not defined

print(x, dict1.get(5, 'unknown')) # gives none if key not defined