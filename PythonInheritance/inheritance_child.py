class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Developer(Person):
    pass

x = Developer("Dennis", "Chiira")
x.printname()
