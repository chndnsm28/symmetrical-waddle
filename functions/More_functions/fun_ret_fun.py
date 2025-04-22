def outer():

    def display():
        print("hello world")

    return display

d = outer()
d()