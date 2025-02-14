from random import randint
choices = ['rock', 'paper', 'scissors']

print('Welcome to Rock-Paper-Scissors game!!!')

randomNumber = randint(0,2)

player = input('Make your move: >>> ').lower()

computer_choice = choices[randomNumber]

print('SHOOT!!')

print(f'Computer plays: >>> {computer_choice}')

draw_condition = (player == computer_choice)

if draw_condition:
       print('It\'s a tie!')
elif player == choices[0]:
    if computer_choice == choices[1]:
        print('Computer Wins!')
    else:
        print('You win!')
elif player == choices[1]:
    if computer_choice == choices[2]:
        print('Computer Wins!')
    else:
        print('You win!')
elif player == choices[2]:
    if computer_choice == choices[0]:
        print('Computer Wins!')
    else:
         print('You win!')
else:
     print('Please enter a valid move!')

