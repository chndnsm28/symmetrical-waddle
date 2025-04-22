import os
import csv

f= open("C:\\Users\\user\\Desktop\\MyPython\\Book1.csv", 'r')
csv_reader = csv.reader(f)
next(csv_reader)
sals = []

for row in csv_reader:
    sals.append(int(row[2]))
print(sals)

print('max', max(sals))
print('min', min(sals))

f.close()