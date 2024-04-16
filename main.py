import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player=None
while player not in choices:
    player = input('Enter rock, paper, or scissors: ').lower()

if player == computer:
    print('Player:',player)
    print('Computer',computer)
    print('Draw')
elif player == 'rock':
    if computer == 'scissors':
        print('Player:', player)
        print('Computer', computer)
        print('You win')
    if computer == 'paper':
        print('Player:', player)
        print('Computer', computer)
        print('You lose')
elif player == 'scissors':
    if computer == 'paper':
        print('Player:', player)
        print('Computer', computer)
        print('You win')
    if computer == 'rock':
        print('Player:', player)
        print('Computer', computer)
        print('You lose')
elif player == 'paper':
    if computer == 'rock':
        print('Player:', player)
        print('Computer', computer)
        print('You win')
    if computer == 'scissors':
        print('Player:', player)
        print('Computer', computer)
        print('You lose')