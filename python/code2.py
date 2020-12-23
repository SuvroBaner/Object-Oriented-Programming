# Defining the class and instance variables -
class Player:
    teamName = 'Liverpool' # class variables, i.e. all these players right now play in Liverpool

    def __init__(self, name):
        self.name = name # instance variable # name of the player
        self.formerTeam = [] # instance variable # name of the former team

p1 = Player('Mark')
p1.formerTeam.append('Barcelona')

p2 = Player('Steve')
p2.formerTeam.append('Chelsea')

print('Name: ', p1.name)
print('Team Name: ', p1.teamName)
print(p1.formerTeam)
print('Name: ', p2.name)
print('Team Name: ', p2.teamName)
print(p2.formerTeam)


print("=======================================")

# Defining the class smartly -

class Player2:
    teamName = 'Liverpool' # class variable
    teamMates = []

    def __init__(self, name):
        self.name = name # all these variables are instance variables
        self.formerTeams = []
        self.teamMates.append(self.name)

    @classmethod
    def getTeamName(cls):
        return cls.teamName

p1 = Player2('Henry')
p1.formerTeams.append('Arsenal')

p2 = Player2('Rooney')
p2.formerTeams.append('Manchester United')
p2.formerTeams.append('Everton')

print('Playing Team : ', Player2.getTeamName())

print('Name: ', p1.name)
print('Playing Team: ', p1.teamName)
print('Former Teams: ', p1.formerTeams)
print('Team Mates: ', p1.teamMates)

print("---------------------")

print('Name: ', p2.name)
print('Playing Team: ', p2.teamName)
print('Former Teams: ', p2.formerTeams)
print('Team Mates: ', p2.teamMates)

print("========================================")

###########################

class Employee:
    def __init__(self, ID = None, name = None, salary = None):
        self.ID = ID
        self.name = name
        self.salary = salary

    def tax(self):
        return 0.3*self.salary

    def salaryPerDay(self):
        return self.salary/30

    # method overloading
    def demo(self, a, b, c, d = 5, e = None):
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)
        print("d = ", d)
        print("e = ", e)

e1 = Employee(1234, 'Mark', 10000)

print('Name: ', e1.name)
print('Emp ID: ', e1.ID)
print('Salary: ', e1.salary)
print('Tax paid by {}: '.format(e1.name), e1.tax())
print('Salary per day of {} : '.format(e1.name), e1.salaryPerDay())
print('\n')

print('Demo-1')
e1.demo(1, 2, 3)
print('\n')

print('Demo-2')
e1.demo(1, 2, 3, 4)
print('\n')

print('Demo-3')
e1.demo(1, 2, 3, 4, 5)

########################### Class and Static Method ################
class Player3:
    teamName = 'Liverpool'

    def __init__(self, name):
        self.name = name

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @staticmethod
    def demo():
        print('I am a static method')

suvro = Player3('Suvro')
suvro.demo()
Player3.demo()
print(Player3.getTeamName())

################################################################
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height ** 2)

weight = 65
height = 1.74
print(BodyInfo.bmi(weight, height))
print('\n')

############## Private Properties ############
class Employee2:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # it is a private property
        #print(self.__salary)

Steve = Employee2(3789, 2500)
print('ID: ', Steve.ID)
#print('Salary: ', Steve.__salary) # as salary is a private property so it will not be accessed outside the class

##### Private Methods ###############
class Employee3:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # salary is the private property

    def displaySalary(self):  # it is a public method
        print('Salary: ', self.__salary)

    def __displayID(self): # it is a private method
        print("ID: ", self.ID)

Steve2 = Employee3(1234, 10000)
Steve2.displaySalary()
#Steve2.__displayID() # this will generate an error as it is a private method
print('\n')
print("----------------")

#### Accessing Private Attributes in the Main Code #############
class Employee4:
    def __init__(self, ID = None, name = None, salary = None):
        self.ID = ID
        self.name = name
        self.__salary = salary # private property

suvro1 = Employee4(1234, 'Suvro', 10000)
print('ID: ', suvro1.ID)
print('name: ', suvro1.name)
print('salary: ', suvro1._Employee4__salary)