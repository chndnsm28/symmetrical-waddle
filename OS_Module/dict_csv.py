import csv

f = open("C:\\Users\\user\\Desktop\\MyPython\\Book1.csv")

csv_dict = csv.DictReader(f)


dict1 = {}
for row in csv_dict:
    dict1[row['Name']] = row

#print(dict1)


print("Chandan details: ", dict1['Chandan'])