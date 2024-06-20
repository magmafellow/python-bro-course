

class Car:

    color = None


class Motorcycle:

    color = None


def print_car_colors(l):
    for c in l:
        print(c.color)


def change_color(car, color):

    car.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()

my_cars = [car_1, car_2, car_3]
print_car_colors(my_cars)

change_color(car_1, 'pink')
change_color(car_2, 'blue')
change_color(car_3, 'purple')
change_color(bike_1, 'black')

print_car_colors(my_cars)
print(bike_1.color)
