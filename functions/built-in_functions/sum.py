import math

# sum_even_values
# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!

# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0

def sum_even_values(*nums):
  return sum(num if num % 2 == 0 else 0 for num in nums)

# print(sum_even_values(3,5,1,11))

# sum_floats
# Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

def sum_floats(*nums):
  return math.fsum(num if type(num) == float else 0 for num in nums)

print(sum_floats(3,2,1,))