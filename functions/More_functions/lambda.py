def miles2km(miles):
    kms = 1.6 * miles
    return kms


d = miles2km(10)

print("km of the miles given is: ", d)


print(" --------- ")

k = lambda miles: 1.6* miles

print(k(10))

result = lambda a, b:a if a > b else b
print(result(10, 20))