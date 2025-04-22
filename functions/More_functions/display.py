def display():
    print("hello")

d = display
d()


print("--------------------------")

def outer():
    def inner():
        print("i am inner function")

    inner()

outer()