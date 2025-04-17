'''
two_oldest_ages

Write a function called two_oldest_ages. The function should take a list of numbers as its argument and return the two highest numbers within the list. The returned value should be a list in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order.

two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

from typing import List

# def two_oldest_ages(lst: List[int]) -> List[int]:
#   lst_copy = lst[0:]

#   two_max = []

#   two_max.append(max(lst_copy))
#   lst_copy.remove(max(lst_copy))

#   two_max.insert(0, max(lst_copy))

#   print(two_max)

def two_oldest_ages(lst: List[int]) -> List[int]:
  print(sorted(lst)[-2:])

two_oldest_ages( [1, 2, 10, 8])
two_oldest_ages( [6,1,9,10,4])
two_oldest_ages( [4,25,3,20,19,5] )
  
