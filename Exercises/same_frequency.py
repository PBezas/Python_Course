'''
same_frequency

Write a function called same_frequency which accepts two numbers and returns True if they contain the same frequency of digits. Otherwise, it returns False.

same_frequency(5231122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(freq1: int, freq2: int):
  iter1 = str(freq1)
  iter2 = str(freq2)

  counter_dict1 = {i:iter1.count(i) for i in iter1}
  counter_dict2 = {i:iter2.count(i) for i in iter2}

# in python two dicts are equal if and only if they have the exact same keys and the exact same value for each key (and not necessarily in the same order)
  return counter_dict1 == counter_dict2

 
 
print(same_frequency(551122,221515))
print(same_frequency(321142,3212215))
print(same_frequency(1212, 2112))