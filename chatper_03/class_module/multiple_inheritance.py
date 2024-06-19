# multiple inheritance = when a child class is derived from more than one parent class


class Prey:

    def flee(self):  # flee = run away
        print('This animal flees')


class Predator:

    def hunt(self):
        print('This animal is hunting')


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()
hawk.hunt()
# rabbit.hunt()  # there is not a such method in rabbit

# all is good
fish.flee()
fish.hunt()
