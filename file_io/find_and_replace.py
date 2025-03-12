# find_and_replace
# Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.

# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

def find_and_replace(file_name, search_term, replacement):
  with open(file_name) as f:
    lines = f.readlines()
  
  new_lines = [line.replace(search_term, replacement) for line in lines]

  with open(file_name, 'w') as f:
    f.write(''.join(new_lines))

print(find_and_replace('file_io/story.txt', 'Alice', 'Panos'))


  