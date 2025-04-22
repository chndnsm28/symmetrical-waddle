import csv

covid = [{'Country':'India', 'Doses':'221Cr', 'Vaccinated':'88' },
        {'Country':'Brazil', 'Doses':'21Cr', 'Vaccinated':'48' },
        {'Country':'China', 'Doses':'521Cr', 'Vaccinated':'42' }]


f = open('CSVDict.csv', 'w', newline='')
field = ['Country', 'Doses', 'Vaccinated']
wrtr = csv.DictWriter(f,field)

wrtr.writeheader()
for d in covid:
    wrtr.writerow(d)

f.close()

