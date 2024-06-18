# *args =    parameter that will pack all arguments into a tuple
#            useful so that a function can accept a varying amount of arguments

def add(*stuff):
    summa = 0
    for i in stuff:
        summa += i
    return summa


print(add(1, 2, 3, 4, 5, 10))
