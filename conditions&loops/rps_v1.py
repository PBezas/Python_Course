print('Welcome to Rock-Paper-Scissors game!!!')

player1 = input('Player 1, enter your choice: ')

player2 = input('Player 2, enter your choice: ')

print('SHOOT!!')

p1_win_condition1 = (player2 == 'Rock') and (player1 == 'Paper')

p1_win_condition2 = (player2 == 'Paper') and (player1 == 'Scissors')

p1_win_condition3 = (player2 == 'Scissors') and (player1 == 'Rock')

p2_win_condition1 = (player1 == 'Rock') and (player2 == 'Paper')

p2_win_condition2 = (player1 == 'Paper') and (player2 == 'Scissors')

p2_win_condition3 = (player1 == 'Scissors') and (player2 == 'Rock')

draw_condition = (player1 == player2)

if (draw_condition):
   print('It\'s a tie!')
elif p2_win_condition1 or p2_win_condition2 or p2_win_condition3:
      print('Player 2 Wins!')
elif p1_win_condition1 or p1_win_condition2 or p1_win_condition3:
    print('Player 1 Wins!')
else:
    print('Something went wrong!')

