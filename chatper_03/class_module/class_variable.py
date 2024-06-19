from car import Car


car_1 = Car('Chevy', 'Corvette', '2021', 'blue')
car_2 = Car('Ford', 'Mustang', 2022, 'red')

# car_1.wheels = 2

Car.wheels = 2  # this affects all instances of the class (Car)

print(car_2.wheels)
print(Car.wheels)
