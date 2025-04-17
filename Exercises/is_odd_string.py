'''
is_odd_string

Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is in the first position, "b" is in the second position, and so on. If the sum is even, return false.  NOTE: INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.

is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

alphabet = {chr(i + 97): i + 1 for i in range(26)}

def is_odd_string(word:str) -> bool:
  sum_val = 0
  for ch in word.lower():
    sum_val += alphabet[ch]
  print(sum_val % 2 != 0)

is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('VERyFUnnY') # False