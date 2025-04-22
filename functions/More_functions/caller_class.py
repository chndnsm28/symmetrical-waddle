class Dept:
    def __init__(self):
        self.depts = { 'hr': "human resource",
                       'acc': "accounts",
                       'sd' : "service domain",
                       'mkt':'marketing'

        }
    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
s = d('hr')
print(s)