'''
sum_pairs

Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function.

sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

# def sum_pairs(lst: list, sum_val: int):
#   return [(lst[i],lst[i+1]) for i in range(len(lst) - 1) if lst[i] + lst[i+1] == sum_val]

def sum_pairs(lst:list, sum_val: int):
  pairs = []
  for i in range(len(lst) - 1):
    num1 = lst[i]
    num2 = lst[i+1]
    if num1 + num2 == sum_val:
      pairs.append(num1)
      pairs.append(num2)
      return pairs
  return pairs

    
print(sum_pairs([2,3,3,5,1], 6))





