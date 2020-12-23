class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer: ", self.make)
        print('Color: ', self.color)
        print('Model: ', self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the contructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors: ", self.doors)

obj1 = Car("Hyundai", "Fiery Red", "Grand i10", 4)
obj1.printCarDetails()

#######################################################
class Vehicle1: # defining the parent class
    fuelCap = 90

class Car1(Vehicle1): # defining the child class
    fuelCap = 50

    def display(self):
        # accessing the fuel cap from the parent class
        print('Fuel Cap from Vehicle class: ', super().fuelCap)

        # accessing the fuel cap from the child class
        print('Fuel Cap from Car class: ', self.fuelCap)

obj1 = Car1()
obj1.display()

########################################################
class Vehicle2:
    def display(self):
        print('Display method from the Vehicle class')

class Car2(Vehicle2):
    def display(self):
        super().display()
        print("I am from the Car class")

obj2 = Car2()
obj2.display()

#########################################################
class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)

###################################

# Single Inheritence -

class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("The top speed is set to : ", self.topSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print('Trunk is now open ...')

corolla = Car()
corolla.setTopSpeed(220)
corolla.openTrunk()

# Multilevel-Inheritence -
# A "car" is a "vehicle" and a "hybrid" is a "car".

class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("The top speed is set to: ", self.topSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print('Trunk is now open ...')

class Hybrid(Car):
    def turnOnHybrid(self):
        print('The hybrid mode is turned on...')

tesla = Hybrid()
tesla.setTopSpeed(220)
tesla.openTrunk()
tesla.turnOnHybrid()

#### Hierarchical Inheritence -
# A "car" is a "vehicle", a "truck" is a "vehicle".

class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("The top speed is set to: ", self.topSpeed)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

corolla = Car()
corolla.setTopSpeed(220)

volvo = Truck()
volvo.setTopSpeed(180)

# Multiple Inheritence -
# "Hybrid Engine" is a "Electric Engine" ... "Hybrid Engine" is a "Combustion Engine".

class CombustionEngine:
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine:
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inheriting from both parent classes
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print('Tank Capacity: ', self.tankCapacity)
        print('Charge Capacity: ', self.chargeCapacity)

car = HybridEngine()
car.setTankCapacity("38 litres")
car.setChargeCapacity("250 W")
car.printDetails()

############################
# CombustionEngine is a engine
# ElectricEngine is a engine
# HybridEngine is a ElectricEngine and a CombustionEngine

class Engine:
    def setPower(self, power):
        self.power = power

class CombustionEngine(Engine):
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(Engine):
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print('Power: ', self.power)
        print('Tank Capacity: ', self.tankCapacity)
        print('Charge Capacity: ', self.chargeCapacity)

car = HybridEngine()
car.setPower("2000 cc")
car.setChargeCapacity("250 W")
car.setTankCapacity("32 litres")
car.printDetails()