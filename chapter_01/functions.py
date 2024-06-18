# function = a block of code which is executed only when it is called

maq = 'maquiwin'


def hello(fn, ln, age):
    print('Hello '+fn + ' ' + ln)
    print('Have a nice day')
    print('You will be ' + str(age + 1) + ' in a year')


hello(maq, 'light', 19)
