class Str:
    def __init__(self, a,  b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.a + '/' + self.b

a = Str("chandan", "rekha")

print(a)