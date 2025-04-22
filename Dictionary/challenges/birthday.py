birthdays = {
        'Sachin': '03/14/2003',
        'Carl': '01/17/2001',
        'Khan': '12/10/2006',
        'Donald': '06/14/2010',
        'Rohan': '01/6/2005' }
name = input("enter the name of the preson")

if name in birthdays:
    print("The person {} was born on {}" .format(name, birthdays.get(name)))
else:
    print("name not found")


