# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}


########################################
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_F.items() = dict_items([('New York', 32), ('Boston', 75), ('Los Angeles', 100), ('Chicago', 50)])
#
# cities_in_C = {key: (round((value-32)*(5/9), 1)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

########################################
# weather = {'New York': 'snowing', 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
#
# cloudy_weather = {key: value for (key, value) in weather.items() if value == 'cloudy'}
# print(cloudy_weather)

########################################
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ('WARM' if value > 50 else 'COLD') for (key, value) in cities_in_F.items()}
# print(desc_cities)

########################################
# def check_temp(value):
#     if value >= 70:
#         return 'HOT'
#     elif 69 >= value >= 40:
#         return 'WARM'
#     else:
#         return 'COLD'
#
#
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}
#
# print(desc_cities)

################################################### # standalone implementation
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
def check_temp_unpacking(value):
    value = value[1]
    if value >= 70:
        return 'HOT'
    elif 69 >= value >= 40:
        return 'WARM'
    else:
        return 'COLD'


desc_cities = list(map(check_temp_unpacking, cities_in_F.items()))
print(desc_cities)
