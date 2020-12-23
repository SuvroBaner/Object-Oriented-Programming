class Student:

    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def Percentage(self):
        total = 300
        score = self.totalObtained()
        return 100*score/total

if __name__ == '__main__':
    s = Student('Suvro', 90, 85, 87)
    print(s.totalObtained())
    print(s.Percentage())