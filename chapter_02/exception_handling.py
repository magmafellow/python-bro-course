# exception =    events detected during execution that interrupt the flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print('You cannot divide by zero')
    print(e)
except ValueError as e:
    print('Enter only numbers, please')
    print(e)
except Exception as e:
    print('something went wrong :(')
    print(e)
else:
    print(result)
finally:
    print('I am always here')
