def Clouser():
    msg = "hello"

    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)

    return display

d = Clouser()
d()
print("__________________________________")
def Depts():
    depts = {'hr':'HumanResource',
             'sd': "Sales",
             'mkt': 'Marketing'}

    def dname(dept):
        return depts[dept]

    return dname
d = Depts()
name = input("enter the dept key name")
print(d(name))

