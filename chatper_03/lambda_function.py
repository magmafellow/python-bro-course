# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# def double(x):
#     return x * 2
# print(double(10))


# double = lambda x: x * 2
# print(double(19))


# multiply = lambda x, y: x * y
# add = lambda a, b, c: a + b + c
# print(multiply(10, 5))
# print(add(1, 5, 19))
# print(multiply(10, 5) / add(1, 5, 19))


# full_name = lambda fn, ln: '{} {}'.format(fn, ln)
# print(full_name('alex', 'romanov'))


check_age = lambda age: print('allowed') if age >= 18 else print('forbidden')
check_age(19)
