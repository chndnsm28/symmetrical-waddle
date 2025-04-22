class Students:
    def __init__(self,roll,name,dept):
        self.roll = roll
        self.name = name
        self.dept = dept

    def display(self):
        print(f'Roll:{self.roll}, Name:{self.name}, Dept:{self.dept}')


