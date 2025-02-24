# Tuples & Data Transformation
# Problem: Given a list of tuples, sort them by the second element in ascending order.

# data = [(1, 5), (2, 3), (4, 1), (3, 2)]
# Expected Output:

# [(4, 1), (3, 2), (2, 3), (1, 5)]

data = [(1, 5), (2, 3), (4, 1), (3, 2)]

def transform_data(datalst):
  return sorted(datalst, key=lambda pair: pair[1])

print(transform_data(data))