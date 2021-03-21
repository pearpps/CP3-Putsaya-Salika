class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnonAirConditioner(self):
        print("Turn On :Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass


car1 = Car()
car1.turnonAirConditioner()
car1.sayHello()

car2 = PickUp()
car2.turnonAirConditioner()

car3 = Van()
car3.turnonAirConditioner()

car4 = EstateCar()
car4.turnonAirConditioner()

