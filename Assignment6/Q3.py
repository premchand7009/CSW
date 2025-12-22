class Person:
    def __init__(self, gender):
        self.gender = gender

    def details(self):
        print("Gender:", self.gender)

class College:
    def __init__(self):
        self.p1 = Person("Male")
        self.p2 = Person("Female")

    def show(self):
        self.p1.details()
        self.p2.details()

c = College()
c.show()
