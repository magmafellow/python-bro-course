# nested loop = The "inner loop" will finish all of its iterations before
#               finishing one iteration of the "outer" loop

rows = int(input('How many rows?: '))
cols = int(input('How many columns?: '))
symbol = input('Symbol to use: ')

for i in range(rows):
    for j in range(cols):
        print(symbol, end='')
    print()
