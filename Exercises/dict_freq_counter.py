#  Dictionary Frequency Counter with a Twist
# Write a function word_counter that takes a string and returns a dictionary where:

# Keys are unique words.
# Values are their frequencies in the string.
# Use dictionary comprehension to build the dictionary.
# Ignore punctuation and consider case-insensitivity.

# Example Input:
# text = "Python is fun! Python is powerful. Fun is Python!"

# Expected Output:
# {'python': 3, 'is': 3, 'fun': 2, 'powerful': 1}

text = "Python is fun! Python is powerful. Fun is Python!"

def word_counter(string):
  words = [word.lower().replace('!', '').replace('.', '') for word in string.split()]
  final_dict = {word:words.count(word) for word in set(words)}
  
  return final_dict


print(word_counter(text))