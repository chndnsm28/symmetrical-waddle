dict1 = {101:'Production', 102:'sales', 103:'marketing', 104:'services'}

dict1.pop(105, 'None') #throws error if key not found, works fine if none is defined

print(dict1.popitem()) # rmoves last item

dict1.clear() #removes all items

D = dict()

for x in enumerate(range(2)):

    D[x[0]] = x[1]

    D[x[1]+7] = x[0]

print(D)