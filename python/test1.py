class Student:
    # defining the properties
    ID = None
    GPA = None

# creating an object of the Student class
Peter = Student()

# assigning values to properties of Peter
Peter.ID = 3789
Peter.GPA = 3.5

# create a new attribute for Peter
Peter.department = "Computer Science"


# Create another Student object
John = Student()
John.ID = 3790
John.GPA = 3.7


# Printing properties of Peter
print("ID =", Peter.ID)
print("GPA", Peter.GPA)
print("Department:", Peter.department)

# Printing properties of John
print("ID =", John.ID)
print("GPA", John.GPA)
#print("Department:", John.department)


class Student1:
    def __init__(self, ID, GPA):
        self.ID = ID
        self.__GPA = GPA

Steve = Student1(3789, 3.6)
print("ID:", Steve.ID)
#print("GPA:", Steve.__GPA)

class Book:
    def __init__(self, ID, title):
        self.ID = ID
        self.__title = title


harry_potter = Book(3789, 'Harry Potter and the Chamber of Secrets')
print(harry_potter._Book__title)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def print_area(self):
        print(3.14 * self.radius ** 2)


if __name__ == '__main__':
    c = Circle(3)
    c.print_area()