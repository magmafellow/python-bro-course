# slicing = create a substring by extracting elements from another string

# indexing
name = 'arlexio mogét'

first_name = name[:7]  # [0:7] -> [:7]
last_name = name[8:]  # [8:13] -> [8:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


# slice()
website = 'https://yandex.ru'
website2 = 'https://pink.about-me.ru'

ch2slice = slice(8, -3)
print(website[ch2slice])
print(website2[ch2slice])
