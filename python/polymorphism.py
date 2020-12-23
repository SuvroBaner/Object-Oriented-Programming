class Rectangle:

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)

class Circle:

    def __init__(self, radius = 0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return (self.radius**2 * 3.142)

shapes = [Rectangle(6, 10), Circle(7)]
print('Sides of rectangle are ', str(shapes[0].sides))
print('Area of rectangle is ', str(shapes[0].getArea()))

print('Sides of the circle are ', str(shapes[1].sides))
print('Area of the cicrle is: ', str(shapes[1].getArea()))


print('------------------------------')
################### Inheritence with Polymorphism #########

class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

class Rectangle(Shape):

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)

class Circle(Shape):

    def __init__(self, radius = 0):
        self.radius = radius

    def getArea(self):
        return (self.radius**2 * 3.142)

shapes = [Rectangle(6, 10), Circle(7)]
print('Area of the rectangle is ', str(shapes[0].getArea()))
print('Area of the circle is ', str(shapes[1].getArea()))

################## Operator Overloading #########################
print('-----------------------------------')

class Com:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __add__(self, other): # overloading the '+' operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):
        temp = Com(self.real - other.real,self.imag - other.imag)
        return temp

obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3: ", obj3.real)
print("imag of obj3: ", obj3.imag)
print("real of obj4: ", obj4.real)
print("imag of obj4: ", obj4.imag)

######################## Duck Typing #######################
print("======================")

class Dog:
    def Speak(self):
        print('Woof Woof')

class Cat:
    def Speak(self):
        print('Meow meow')

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)

######################## Abstract Base Classes #########################
class Shape: # shape is a child class of Abstact Base Class
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

shape = Shape()
square = Square(4)

###################################
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

square = Square(5)
print('Area of the square : ', square.area())
print('Perimeter of the square : ', square.perimeter())

