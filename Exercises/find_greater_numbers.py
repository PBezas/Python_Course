'''
find_greater_numbers

Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger number across the entire list. 

Take the example find_greater_numbers([6,1,2,7]) # 4 , there are 4 times where a number is followed by a greater number:  

2 > 1
7 > 6
7 > 1
7 > 2   
Here are some other examples:

find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''



from typing import List

def find_greater_numbers(lst: List[int]) -> int:
    current = 0
    count = 0
    for i,num in enumerate(lst):
      current = num
      for n in lst[i:]:
         if n > current:
            count += 1
    return count

find_greater_numbers([6, 1 ,2 ,7])
find_greater_numbers([1,2,3])
find_greater_numbers([5,4,3,2,1])
find_greater_numbers([])
find_greater_numbers([1,5,3,4])