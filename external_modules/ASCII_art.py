
from pyfiglet import figlet_format
from termcolor import colored, COLORS as valid_colors

def print_art():
  user_text = input('What do you want to print?: ')
  user_color = input('Choose your print color: ')

  if user_color not in valid_colors:
    user_color = 'magenta'

  figlet_text = figlet_format(user_text)
    
  print(colored(figlet_text, color=user_color ,attrs=['blink']))

print_art()
