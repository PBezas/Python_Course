# from random import random
from random import randint


def coin_toss(): 
  rand_num = randint(0,2)
  if (rand_num == 0):
    return 'Heads'
  else:
    return 'Tails'

print(coin_toss())



