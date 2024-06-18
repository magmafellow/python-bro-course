# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "Magma Fellow@"

# if name[0].islower():
#     print('That is lower')
#     name = name.capitalize()

first_name = name[:5].upper()  # [0:5] == [:5]
print(first_name)

last_name = name[6:-1].lower()
print(last_name)

last_character = name[-1]
print(last_character)
