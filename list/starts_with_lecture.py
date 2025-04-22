food = ["pizza", "nugget", "hotdog", "noodles", "pasta", "burger"]
letter = input("enter the starting letter ")
for x in food:
    if x.startswith(letter):
        print(x)