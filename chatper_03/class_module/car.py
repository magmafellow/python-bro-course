

class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, colour):
        self.make = make      # instance variable
        self.model = model    # instance variable
        self.year = year
        self.colour = colour

    def drive(self):
        print('This {} is driving'.format(self.model))

    def stop(self):
        print('This {} is stopped'.format(self.model))
