'''
Titleize

Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.

titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

# def titleize(string:str):
#     splitted = string.split(' ')
#     titleized = []
#     for word in splitted:
#         titleized.append(f'{word[0].upper()}{word[1:]}')
#     return ' '.join(titleized)

# def titleize(string:str):
#   splitted = string.split(' ')
#   titleized = [f'{word[0].upper()}{word[1:]}' for word in splitted]
#   return ' '.join(titleized)

def titleize(string:str):
  return ' '.join([f'{word[0].upper()}{word[1:]}' for word in string.split(' ')])

print(titleize('this is awesome'))
