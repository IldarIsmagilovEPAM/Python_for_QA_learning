#class with init
class Test1:
    def __init__(self, testNumber: int):
        self.testNumber = testNumber

    def show(self):
        print(self.testNumber)

#inheritor
class Inheritor(Test1):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def calc(self):
        return self.number1 + self.number2

#try/except/finally
try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide by zero!!!')
finally:
    pass

#decorator
def printer(func):
    def wrapper(*args, **kwargs):
        print(args)
    return wrapper

@printer
def decorated_func(str1:str, str2:str):
    str1 = str1.capitalize()
    str2 = str2.capitalize()

#@property
class TestingPropertyDecorator:
    def __init__(self, str01, str02):
        self.str01 = str01
        self.str02 = str02

    @property
    def data(self):
        return self.str01 + self.str02

#generator
testGenerator = (i+1 for i in range(0,10))

#collections.namedtuple
from collections import namedtuple
Point = namedtuple('Point', 'x y z')
testPoint = Point(10, 20 , 30)
print(testPoint)

