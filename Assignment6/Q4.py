
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model
c1=Car("Toyota","Camry")
c2=Car(None,None)
print("Car 1 Make:",c1.get_make())
print("Car 1 Model:",c1.get_model())
print("Car 2 Make:",c2.get_make())
print("Car 2 Model:",c2.get_model())
c2.set_make("Honda")
c2.set_model("Civic")
print("Updated Car 2 Make:",c2.get_make())
print("Updated Car 2 Model:",c2.get_model())
