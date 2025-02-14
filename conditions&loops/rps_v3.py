from random import randint



choices = ['rock', 'paper', 'scissors']

pc_win_msg = 'You lose! \U0001F641'
player_win_msg = 'You win! \U0001f600'

replay = 'y'

while replay == 'y':

  print('Welcome to Rock-Paper-Scissors game!!!')

  winning_score = int(input('Please set the winning score: '))

  player_wins = 0
  computer_wins = 0

  while (player_wins <= winning_score) or (computer_wins <= winning_score):

    randomNumber = randint(0,2)

    if computer_wins == winning_score:
        print ('Oh no you lost!!\nBetter luck next time! \U0001F622')
        break
    elif player_wins == winning_score:
        print ('Congratulations!\nEnjoy your victory! \U0001F60A')
        break
    else:

      print(f'>>> Computer Score: {computer_wins}\n>>> Yours Score: {player_wins}')

      player = input('Make your move: >>> ').lower()

      computer_choice = choices[randomNumber]

      print('SHOOT!!')

      print(f'Computer plays: >>> {computer_choice}')

      draw_condition = (player == computer_choice)

      if draw_condition:
            print('It\'s a tie!')
      elif player == choices[0]:
          if computer_choice == choices[1]:
              computer_wins += 1
              print(pc_win_msg)
           
          else:
              player_wins += 1
              print(player_win_msg)
      elif player == choices[1]:
          if computer_choice == choices[2]:
              computer_wins += 1
              print(pc_win_msg)
          else:
              player_wins += 1
              print(player_win_msg)
      elif player == choices[2]:
          if computer_choice == choices[0]:
              computer_wins += 1
              print(pc_win_msg)
          else:
              player_wins += 1
              print(player_win_msg)
      else:
          print('Please enter a valid move!')
  
  replay = input('Do you want to play again? (y/n): ') 

  if (replay == 'n'):
    print('Thanks for playing!\nBye!')
    break

