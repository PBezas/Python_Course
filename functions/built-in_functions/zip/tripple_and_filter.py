# triple_and_filter
# Write a function called triple_and_filter. This function should accept a list of numbers, filter out every number that is not evenly divisible by 4 (i.e., filter out numbers that do not divide by 4 with a remainder of zero), and return a new list where every remaining number is tripled.

# expected outputs:
#     triple_and_filter([1,2,3,4]) # [12]
#     triple_and_filter([6,8,10,12]) # [24,36]

def triple_and_filter(nums):
  return list(map(lambda num: num*3, filter(lambda num: num % 4 == 0, nums)))

print(triple_and_filter([4, 8 , 2 , 5]))