class Customer:
    def __init__(self, cname, cid, bdno, bcity, bpin, sdno, scity, spin):
        self.customerName = cname
        self.cust_id = cid
        self.baddr = self.Address(bdno, bcity, bpin,)
        self.saddr = self.Address(sdno, scity, spin)

    class Address:
        def __init__(self,dno, city, pin):
            self.dno= dno
            self.city = city
            self.pin = pin

        def display(self):
            print(self.dno)
            print(self.city)
            print(self.pin)

c = Customer('chandan', 123, 'avantra', 'shimoga', 577201, 234, 'Tumkuru', 654321)

c.saddr.display()
