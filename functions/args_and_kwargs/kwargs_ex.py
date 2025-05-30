# **kwargs Exercise
# Note: for this exercise, make use of **kwargs.  No default parameters allowed!

# Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!

# combine_words("child")  #'child'

# combine_words("child", prefix="man")  #'manchild'

# combine_words("child", suffix="ish")  #'childish'

# combine_words("work", suffix="er")  #'worker'

# combine_words("work", prefix="home")  #'homework'


def combine_words(word, **words):
  if 'prefix' in words:
    return f'{words['prefix']}{word}'
  elif 'suffix' in words:
    return f'{word}{words['suffix']}'
  return word

# const combine_words = (word, ...words) => {
#     if (words.prefix) {
#       return `${words[prefix]]}${word}`
#     else if (words.suffix) {
#       return `${word}${words[suffix]}`
#     }
#     return word
#   }
# }