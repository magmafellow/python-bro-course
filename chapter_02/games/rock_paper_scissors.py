import random


while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, or scissors?: ').lower()

    if player == computer:
        print('computer: {}'.format(computer))
        print('player: {}'.format(player))
        print('Tie!')

    elif player == 'rock':
        if computer == 'paper':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You lose!')
        elif computer == 'scissors':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You won!')
    elif player == 'scissors':
        if computer == 'paper':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You won!')
        elif computer == 'rock':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You lose!')
    elif player == 'paper':
        if computer == 'scissors':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You lose!')
        elif computer == 'rock':
            print('computer: {}'.format(computer))
            print('player: {}'.format(player))
            print('You won!')

    play_again = input('Play again? (yes/no)?: ').lower()

    if play_again != 'yes':
        break


print('Bye')
