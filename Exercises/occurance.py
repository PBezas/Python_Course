# Problem: Write a program that counts the occurrences of each word in a given sentence and stores the results in a dictionary.

# input: 
# sentence = "this is a test this is only a test"

# output:
# {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

sentence = "this is a test this is only a test"

def count_occurance(phrase):
  return {word:phrase.count(word) for word in phrase.split()}

print(count_occurance(sentence))