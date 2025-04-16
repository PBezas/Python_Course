'''
two_list_dictionary

Write a function called two_list_dictionary which accepts two lists of varying lengths.The first list consists of keys and the second one consists of values. Your function should return a dictionary created from the keys and values. If there are not enough values, the remaining keys should have a value of null. If there not enough keys, just ignore the remaining values.

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

from typing import Dict

# def two_list_dictionary(keys: list, values: list) -> Dict[str, int]:
#    result_dict = {}
#    for index, key in enumerate(keys):
#       if index < len(values):
#         result_dict[key] = values[index]
#       else:
#         result_dict[key] = None
#    return result_dict 

def two_list_dictionary(keys: list, values: list) -> Dict[str, int]:
  return {k:values[i] if i < len(values) else None for i, k in enumerate(keys)}

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))