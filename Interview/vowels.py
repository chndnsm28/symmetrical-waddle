from decorator import append

from list.Occrance_of_element import count


def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

s = "chandan"
vowels = "aeiouAEIOU"
cnt = {i: s.count(i) for i in vowels if i in s}
print(cnt)





