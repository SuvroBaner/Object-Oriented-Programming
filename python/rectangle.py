class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return 2 * (self.__length + self.__width)

if __name__ == '__main__':
    r = Rectangle(2, 3)
    print(r.area())
    print(r.perimeter())