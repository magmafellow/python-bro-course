from chatper_03.class_module.car import Car


car_1 = Car('Chevy', 'Corvette', '2021', 'blue')
car_2 = Car('Ford', 'Mustang', 2022, 'red')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.colour)

car_1.drive()
car_1.stop()

print('-' * 10)

# print(car_2.colour)
car_2.drive()
