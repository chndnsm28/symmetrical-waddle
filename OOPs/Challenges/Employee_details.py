class Employee:
    emp_count = 101
    def __init__(self, name, des, sal):
        self.name = name
        self.des = des
        self.sal = sal
        self.eid = 'e' + str(Employee.emp_count)
        Employee.emp_count += 1

    def show_details(self):
        print('Emp_id: ', self.eid)
        print("Emp_Name: ", self.name)
        print("Emp_desg: ",self.des)
        print("Emp_salary:", self.sal)
    @classmethod
    def total_emp(cls):
        return Employee.emp_count - 101

e1 = Employee("chandan", "tester", "8 LPA")
e2 = Employee("Ashish", "SAP consultant", "15 LPA")
e3 = Employee("Rekha", "tester", "6 LPA")
e4 = Employee("Kiran", "SAP Dev", "14 LPA")
e5 = Employee("Spoorthy", "tester", "14 LPA")
e1.show_details()

print("")
e2.show_details()
print("")
e3.show_details()
print("")
e4.show_details()
print("")
e5.show_details()
print("")
print("Total employee are", e5.total_emp())





