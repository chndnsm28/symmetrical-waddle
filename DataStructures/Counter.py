from collections import Counter

L = ['Ram', 'Ram', 'sham', 'jhon', 'Rock', 'sham', 'Bheem']
c = Counter(L)
print(c)
print(c.get('Ram'))
print(c['sham'])
print(c.keys())
print(c.values())
c.update({'Chanda':4})
print(c)
print(c.most_common(2))
c.pop('Rock')
print(c)
c.popitem()
print(c)
print(c.elements())
for i in c.elements():
    print(i)
a = c.copy()
print(a)
b = list(a)
print(b)