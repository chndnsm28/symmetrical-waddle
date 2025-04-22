class Iphone6:
    def home(self):
        print("home is pressed")

class Iphonex(Iphone6):
    def home(self):
        print("home is touched")
        #super().home()  to get parents home method


i6 = Iphone6()
i6.home()

ix = Iphonex()
ix.home()