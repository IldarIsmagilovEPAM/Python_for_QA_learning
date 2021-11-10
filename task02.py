# list
listOfThings = [0, True, 'hello']

# dict
myDict = {'first': 'Mike', 'second': 'Helene', 'third': 'Alex'}

# set
mySet = {1, 3, None}

# working with list
print(listOfThings[1])

# if
if 4 > 5:
    print('Спасибо!')
elif 4 == 5:
    print('Thank you!')
elif 4 <= 5:
    print('Muchas gracias!')
else:
    print('Grand merci!')

# while
tempParamForWhile = 10
while tempParamForWhile > 0:
    print('Foobar!')
    tempParamForWhile -= 1

# printing a list with for
for i in range(len(listOfThings)):
    print(listOfThings[i])

# printing number 0-6
for i in range(6):
    print(i)

# if in 'TEST'
testString = 'TEST'
for char in testString:
    if char == 'E':
        print('pass')

###
# input
inputFromUser = input('Please, input smth: ')
print('This is "{0}" a message from you.'.format(inputFromUser))

# printing from file
with open('testForPrint.txt') as f:
    print(f.read())

# func with 2 arguments
def testSum(x, y):
    return x + y

# func with args
def printThis(*args):
    for arg in args:
        print(arg)
