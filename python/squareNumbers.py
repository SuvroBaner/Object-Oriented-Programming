class Point:

    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

if __name__ == '__main__':
    p = Point(2, 3, 4)
    print(p.sqSum())