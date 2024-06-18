# while loop = a statement that will execute its block of code,
#            as long as its condition remains true

# while 1 == 1:
#     print('Hahaho')

# vers 1
# name = ''
# while len(name) == 0:
#     name = input('Enter your name: ')
#
# print('Hello ' + name)

# vers 2
name = None
while not name:
    name = input('Enter your name: ')

print('Hello ' + name)
