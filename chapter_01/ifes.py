# if statement = a block of code that will execute if its condition is ture

age = int(input('How old are you?: '))

if age == 100:
    print('You are a century old!')
elif age >= 18:
    print('you are allowed')
elif age < 0:
    print('you have not been born yet!')
else:
    print('get away. live more')
