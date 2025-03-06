# Time Validating
# Write a function called is_valid_time  that accepts a single string argument.  It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  Note that times can start with a single number (2:30) or two (11:18).  

# is_valid_time("10:45")       #True
# is_valid_time("1:23")        #True
# is_valid_time("10.45")       #False
# is_valid_time("1999")        #False
# is_valid_time("145:23")      #False
# In order to return True, the string should ONLY contain the time, and no other characters

# is_valid_time("it is 12:15") #False
# is_valid_time("12:15")       #True
# Don't worry about impossible times like 88:76, just focus on the formatting!

# is_valid_time("34:55") #True

import re

def is_valid_time(str):
  time_pattern = re.compile(r'\d{1,2}:\d{2}')
  if time_pattern.fullmatch(str):
    return True
  return False

print(is_valid_time("10:45")) # True
print(is_valid_time("1:45")) # True
print(is_valid_time("10:4")) # False
print(is_valid_time("112:45")) # False
print(is_valid_time("11:4523")) # False
print(is_valid_time("1a:45")) # False
print(is_valid_time("10:ag")) # False
print(is_valid_time("it is 12:15")) # False