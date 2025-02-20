# capitalize
# Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.  You may want to use slices to help you out. Apply error handling

# EXPECTED RESULT
# capitalize("jamaica") # "Jamaica"
# capitalize("chicken") # "Chicken"

def capitalize(param):
  try:
      if type(param) == str:
        result = f'{param[0].upper()}{param[1:]}'
  except:
       print('You should pass a string. Any other type is not accepted!')
  else:
       print('Well done!')
       return f'the result is {result}'

print(capitalize(['a', 'b']))