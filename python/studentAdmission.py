class Student:

    def setName(self, name):
        self.__name = name

    def setRollNumber(self, number):
        self.__RollNumber = number

    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__RollNumber

if __name__ == '__main__':
    s = Student()
    s.setName('Suvro Banerjee')
    s.setRollNumber(32)
    print('Student Name: ', s.getName())
    print('Student Roll Number: ', s.getRollNumber())