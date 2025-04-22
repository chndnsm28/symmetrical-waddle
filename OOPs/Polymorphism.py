def petlover(pet):
    pet.talk()
    pet.walk()


class Duck:
    def talk(self):
        print("Duck Talks")

    def walk(self):
        print("Duck walks")

class Dog:
    def talk(self):
        print("Dog Talks")

    def walk(self):
        print("Dog walks")

d = Dog()
petlover(d)