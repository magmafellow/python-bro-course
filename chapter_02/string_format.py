# str.format() =    optional method that gives users
#                   more control when displaying output

animal = 'cow'
item = 'moon'

# print('The ' + animal + ' jumped over the ' + item)
# print('The {} jumped over the {}'.format('cow', 'moon'))
# print('The {0} jumped over the {1}'.format(animal, item))  # {} = format field
# print('The {1} jumped over the {0}'.format(item, animal))  # works great
# print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))  # keyword argument
# print('The {item} jumped over the {animal}'.format(animal='cow', item='moon'))  # keyword argument

# text = 'The {} jumped over the {}'
# print(text.format(animal, item))


# name = 'Pushkin'
#
# print('Hello, my name is {name}'.format(name=name))
# print('Hello, my name is {name:>10}. Nice to meet you'.format(name=name))
# print('Hello, my name is {name:<10}. Nice to meet you'.format(name=name))
# print('Hello, my name is {name:^10}. Nice to meet you'.format(name=name))


number = 3.14159
large = 1001

print('The number PI is {0:.3f}'.format(number))
print('The large is {:b}'.format(large))
print('The large is {:o}'.format(large))
print('The large is {:x}'.format(large))
print('The large is {:e}'.format(large))  # scientific notation
