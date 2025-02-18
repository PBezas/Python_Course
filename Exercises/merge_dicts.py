# Merging Dictionaries
# Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If there are duplicate keys, sum the values associated with those keys.

# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_dicts(dict1, dict2))

# # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1:dict, dict2:dict):
  # dict1_keys = []
  # dict2_keys = []

  # for key in dict1.keys():
  #   dict1_keys.append(key)

  # for key in dict2.keys():
  #   dict2_keys.append(key)

  # dict1_keys.extend(dict2_keys)

  # both_dict_keys = set(dict1_keys)

  return [[key for key in dict1.keys()].extend([key for key in dict2.keys()])]


    

print(merge_dicts(dict1,dict2))

