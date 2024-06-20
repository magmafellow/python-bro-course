name = "Magma"

print(len(name))  # 5
print(name.find('M'))  # 0
print("magma fellow".capitalize())  # Magma fellow
print(name.upper())  # MAGMA
print("MAgmA".lower())  # magma
print(name.isdigit())  # False
print(name.isalpha())  # True # contains only letters. if a space there -> False
print(name.count("g"))  # 1
print(name.replace("a", "o"))  # .....
print(name * 9)  # MagmaMagmaMagmaMagmaMagmaMagmaMagmaMagmaMagma
