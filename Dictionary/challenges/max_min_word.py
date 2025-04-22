from operator import index

words = {
        'Sachin': 'woderfoul, person in world',
        'Carl': 'he is good in some',
        'Khan': 'ok for some',
        'Donald': 'bad for u',
        'Rohan': 'good' }

keys = list(words.keys())
print(keys)
values = list(words.values())
print(values)
lens = [len(x) for x in values]
print(lens)

max_len = max(lens)
min_len = min(lens)

max_index = lens.index(max_len)

print("max key is", keys[max_index], "sentence is", values[max_index] )
