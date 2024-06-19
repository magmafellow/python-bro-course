# method chaining = calling multiple methods sequentially
#        each call performs an action on the same object and returns self
import time


class Car:

    def turn_on(self):
        print('You start the engine')
        return self

    def drive(self):
        print('You drive the car')
        return self

    def brake(self):
        print('You step on the brakes')
        return self

    def turn_off(self):
        print('You turn off the engine')
        return self


car = Car()

# car.turn_on()
# car.drive()

# car.turn_on().drive()
# print('We are going...')
# time.sleep(2)
# car.brake().turn_off()

# all methods in place
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
