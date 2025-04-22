def decorate(func):
    def wrapper(msg):
        print("*" * 10)
        func(msg)
        print("*" * 10)

    return wrapper
@decorate
def display(msg):
    print(msg)


#d = decorate(display)
display("hello chandan")

print("--------------------")

def Depts(func):
    depts = {'hr':'HumanResource',
             'sd': "Sales",
             'mkt': 'Marketing'}
    def wraper(name):
        func(name)
    

    return dname
def dname(dept):
    return Depts[name]


d = Depts(dname)
name = input("enter the dept key name")


print(d(name))