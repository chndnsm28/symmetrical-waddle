str1 ="i.like.this.program.very.much"
str2 ="much.very.program.this.like.i"

str3 = str1.split(".")

str4= str3[::-1]
print(str4)
res = ".".join(str4)
print(res)

print("___________________")

def reverse_words(str):
    # Split the input string by '.' while
    # ignoring multiple consecutive dots
    words = [word for word in str.split('.') if word]

    # Reverse the words
    words.reverse()

    # Join the reversed words back into a string
    return '.'.join(words)


if __name__ == "__main__":
    str = "i.like.this.program.very.much"
    print(reverse_words(str))