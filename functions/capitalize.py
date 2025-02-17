# capitalize
# Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.  You may want to use slices to help you out.

# EXPECTED RESULT
# capitalize("jamaica") # "Jamaica"
# capitalize("chicken") # "Chicken"

def capitalize(string):
    return f'{string[0].upper()}{string[1:]}'

print(capitalize([1,2, 3]))