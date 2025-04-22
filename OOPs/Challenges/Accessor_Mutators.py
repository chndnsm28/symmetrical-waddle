class Customer:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno

    def getname(self):
        return self.name

    def setphno(self, no):
        self.phno = no
        return self.phno
    def display(self):
        return self.name, self.phno


a = Customer("Chandan", "8431111029")
print(a.getname())
#a.setphno("9343746712")
print(a.display())
