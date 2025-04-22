import csv

covid = [('Country', 'Doses', 'People', 'percentage'), ('India', '336Cr', '450Cr', '77'),
         ('China', '331Cr', '200Cr', '57'), ('Peru', '36Cr', '20Cr', '97')]

f = open("covid.csv", 'w',newline= "")
wrtr = csv.writer(f)

for t in covid:
    wrtr.writerow(t)
f.close()



