def pangram(words):

    letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    print(len(letters))
    fetched = set(words)
    print(fetched)
    print(len(fetched))
    if (len(fetched)) == len(letters)+1:
        return print("yes its an pangram")
    else:
        return False



sentence = "the quick brown fox jumps over the lazy dog"
result = pangram(sentence)
print(result)
