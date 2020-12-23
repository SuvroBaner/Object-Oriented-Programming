# defining a class

class Employee:
    # definig the properties of the class and assigning the values
    ID = 3789
    salary = 2500
    department = 'Human Resources'

# create an object of the Employee class
Steve = Employee()

# printing the properties of Steve which is an object of the Employee class

print('ID = ', Steve.ID)
print('Salary = ', Steve.salary)
print('Department = ', Steve.department)

# Assigning in the main method
class Employee2:
    ID = None
    salary = None
    department = None

Steve2 = Employee2()
Steve2.ID = 3789
Steve2.salary = 2500
Steve2.department = 'Human Resources'

# Adding a property outside the class -
Steve2.title = 'Manager'

# Printing the properties of Steve2
print('-----------------------')
print('ID = ', Steve2.ID)
print('Salary = ', Steve2.salary)
print('Department = ', Steve2.department)
print('Title = ', Steve2.title)

###########################
class Employee3:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

Steve3 = Employee3(3789, 2500, "Human Resources")

print("-------------3 ------------")
print('ID = ', Steve2.ID)
print('Salary = ', Steve2.salary)
print('Department = ', Steve2.department)


###############################
class Employee4:
    def __init__(self, ID = None, salary = 0, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department

Steve4 = Employee4()
Mark = Employee4(3789, 2500, "Human Resources")

print('----------------- 4 -------------')
print("Steve4")
print("ID : ", Steve4.ID)
print("Salary : ", Steve4.salary)
print("Department : ", Steve4.department)

print("Mark")
print("ID :", Mark.ID)
print("Salary : ", Mark.salary)
print("Department : ", Mark.department)