from csv import excel


class NegativeAge(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def stage(age):
    if age < 0:
        raise NegativeAge("invalid age")
    elif age <= 13:
        print("You are a kid")
    elif 13 < age <= 18:
        print("you are teen")
    elif 18 < age <=50:
        print("you are young")
    else:
        print("you are old")


age = int(input("enter the age"))
try:
    stage(age)
except NegativeAge as msg:
    print(msg)

finally:
    print("age verification is done")
