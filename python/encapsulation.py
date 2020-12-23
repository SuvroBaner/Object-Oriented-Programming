class User:

    def __init__(self, username = None):
        self.__username = username # defined username as a private property

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return self.__username

Steve = User('steve1')
print('Before Setting: ', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting: ', Steve.getUsername())

class User1:

    def __init__(self, username = None, password = None):
        self.__username = username
        self.__password = password

    def login(self, uname, pswd):
        if ((self.__username.lower() == uname.lower()) and (self.__password == pswd)):
            print('Access granted against username: ', self
                  .__username.lower(), 'and password: ', self.__password)
        else:
            print("Invalid Credentials")

print("------------------------------------------")
Steve = User1("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("mehta", "1234")
# Steve.__password ### this will give an error