class Currency:
    def __init__(self,fcr,ic):
        self.fcr = fcr
        self.ic = ic

    def set_fc(self,fcr):
        self.fcr = fcr

    def get_fc(self):
        return self.fcr

    def converter(self):
        return self.fcr * self.ic

icv = float(input("enter forign currency :"))

icr = Currency(70, icv)
icr.set_fc(100)
converted_val = icr.converter()
print("indian currency equvivalent is:", converted_val)