'''
list_check
Write a function called list_check, which accepts a list and returns True if each value in the list is a list. Otherwise the function should return False.

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(lst: list):
   for i in lst:
      if not isinstance(i, list):
         return False
   return True
  
print(list_check([1, True, [],[1],[2,3]]))
print(list_check([[],[1],[2,3]]))
print(list_check([[],[1],[2,3],(1,2)]))