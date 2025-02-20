# Interleaving Strings (kind of tough!)
# This challenge is a bit more involved than the others in this section.  Do not worry if you can't get it!

# Write a function interleave  that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. For example:

# interleave('hi','ha')    # 'hhia'

# interleave('aaa', 'zzz')  # 'azazaz'

# interleave('lzr','iad') #  'lizard'

# This might seem like an easy task using zip , but in fact there are a couple intermediate steps to go from zip back to a single string.


# def interleave(string1, string2):
#   final_string = ''
#   for pair in list(zip(string1, string2)):
#     for i in pair:
#       final_string += i
#   print(final_string)

def interleave(string1, string2):  
                                                           
  return ''.join([''.join(pair) for pair in list(zip(string1, string2))])


print(interleave('lzr','iad'))




