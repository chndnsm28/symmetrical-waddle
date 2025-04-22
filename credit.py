card_no = input("enter card no")
last_digit = card_no[15::]

stars = '*'* 4 + ' '
display = stars * 3 + last_digit

print(display)