student = {}

for i in range (3):
    name = input("enter name")
    roll = input("enter roll no")
    dept = input("enter department")

    student[name] = {'roll_no':roll, 'name':name, 'department':dept }

print(student)