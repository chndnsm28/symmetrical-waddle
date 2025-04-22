
codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

text = "deface"
r_code = " "

for i in text:
    r_txt = ord(i) - ord('a')
    r_code = r_code + codes[r_txt]
print(r_code)
