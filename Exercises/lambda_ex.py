# Functions & Lambda Expressions
# Problem: Write a lambda function to compute the square of a number and use it with map() to square all elements in a list.

# nums = [1, 2, 3, 4, 5]
# Expected Output:

# [1, 4, 9, 16, 25]

nums = [1, 2, 3, 4, 5]

def square_nums(nums):
  return list(map(lambda n: n**2, nums))

print(square_nums(nums))