dict1 = {101:'Production', 102:'sales', 103:'marketing', 104:'services'}

dict2 = dict1.copy()

print(dict2)

print(id(dict1[101]))
print(id(dict2[101]))

dict3 = {105:'after_sales', 106:'Resale'}

dict1.update(dict3)
print(dict1)

print(dict1.get(107))
print(dict1.setdefault(110))