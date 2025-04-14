'''
vowel_count

Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(word: str):
  low_word = word.lower()
  return {i:low_word.count(i) for i in low_word if i in 'aeoui'}

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
print(vowel_count('panoutsakitronmtse'))
