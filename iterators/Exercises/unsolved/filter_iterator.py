# Exercise 3: Filter Iterator
# Create a custom iterator class called FilterIterator that takes an iterable and a function. The iterator should yield only the elements for which the function returns True.

# Example usage:

# numbers = [1, 2, 3, 4, 5, 6]
# filtered = FilterIterator(numbers, lambda x: x % 2 == 0)
# for num in filtered:
#     print(num)

# Expected output:

# 2
# 4
# 6