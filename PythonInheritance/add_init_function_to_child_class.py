class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Developer(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Developer("Dennis", "Chiira")
x.printname()