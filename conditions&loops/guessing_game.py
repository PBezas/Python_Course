from random import randint

replay = 'y'

while replay == 'y':
  
  rand_num = randint(1,10)
  guess = int(input('Guess a number between 1 and 10: '))

  while guess != rand_num:
        if (guess < 1 or guess > 10):
           guess = int(input('Please fill in a valid number\n'))
        elif (guess < rand_num):
          print('Too low. Try again!')
          guess = int(input())
        else:
          print('Too high. Try again!')
          guess = int(input())
      
  print('You guessed correct! You won!')
  
  replay = input('Do you want to play again? (y/n): ')

  if (replay == 'n'):
    print('Thanks for playing!\nBye!')
    break

