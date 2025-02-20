# extract_full_name
# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

# expected output:
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}, {'first': 'Panos', 'last': 'Bezas'}]

def extract_full_names(names):
  return list(map(lambda name: f"{name['first']} {name['last']}", names))

print(extract_full_names(names))