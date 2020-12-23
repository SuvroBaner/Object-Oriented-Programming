################## Aggregation ########################
# People and country of their origin. Each person is associated with a country, but the country can exist without that person -

class Country:
    def __init__(self, name = None, population = 0):
        self.name = name
        self.population = population

    def printDetails(self):
        print('Country Name: ', self.name)
        print('Country Population: ', self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print('Person Name: ', self.name)
        self.country.printDetails()

c = Country("India", 1.5)
p = Person("Suvro", c)
p.printDetails()

# deletes the object p
del p
print("")
c.printDetails()

#################### Composition ######################
# A car is composed of an engine, tires, and doors. In this case a Car owned these objects, so a Car is an Owner class and tires, doors and, engine classes are Owned classes.

class Engine:
    def __init__(self, capacity = 0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details: ", self.capacity)

class Tires:
    def __init__(self, tires = 0):
        self.tires = tires

    def printDetails(self):
        print("Number of Tires: ", self.tires)

class Doors:
    def __init__(self, doors = 0):
        self.doors = doors

    def printDetails(self):
        print("Number of Doors: ", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car Color: ", self.color)

print("\n")
car = Car(1500, 4, 4, 'Fiery Red')
car.printDetails()

print("\n")

######################## Inheritence, composition and aggregation #####################

class Car:
    def __init__(self, model = None, color = None):
        self.model = model
        self.color = color

    def printDetails(self):
        print('Model of the car: ', self.model)
        print('Color of the car: ', self.color)

class SedanEngine:
    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")

class Sedan(Car):
    def __init__(self, model = None, color = None):
        super().__init__(model, color)
        self.engine = SedanEngine()

    def setStart(self):
        self.engine.start()

    def setStop(self):
        self.engine.stop()

car1 = Sedan("Grand i10 Asta", "Fiery Red")
car1.setStart()
car1.printDetails()
car1.setStop()

print("\n")

##########################################################################

##### Implementing a sports team ################

# Implement a School class containing a list of Team objects, and a Team class comprising of a list of Player objects.

class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)

class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        c = 0
        for team in self.teams:
            c = c + (team.getNumberOfPlayers())
        return c

p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p3)
blue_team.addPlayer(p4)

my_school = School("UB")
my_school.addTeam(blue_team)
my_school.addTeam(red_team)

print("Total players in my school : ", my_school.getTotalPlayersInSchool())
