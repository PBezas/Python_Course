'''
repeat

Write a function called repeat, which accepts a string and a number and returns a new string with the string passed to the function repeated the number amount of times. Do not use the built in repeat method!

repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(string: str, num: int):
    if not num:
       return ''
    i = 0
    new_string = ''
    while i < num:
      new_string += string
      i += 1
    return new_string

# def repeat(string: str, num: int):
#   return string * num

print(repeat('abc', 3))