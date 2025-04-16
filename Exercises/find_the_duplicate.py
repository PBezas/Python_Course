'''
find_the_duplicate

Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. The function returns the number which is a duplicate or None if there are no duplicates.

find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(lst:list) -> int | None:
  dup = None
  for i in lst:
    count = lst.count(i)
    if count > 1:
      dup = i
  return dup
  
print(find_the_duplicate([1,2,1,4,3,12]))
print(find_the_duplicate([6,1,9,5,3,4,9]))
print(find_the_duplicate([2,1,3,4]))
print(find_the_duplicate([2,1,3,4, 12, 5, 5,]))