# Exercise 2: Set Operations & Tuples in a Loop
# Write a function unique_pairs that takes two lists and returns a set of unique tuples (pairs) where:

# The first element comes from the first list.
# The second element comes from the second list.
# The pair is only included if the sum of both numbers is even.

# Example Input:
# list1 = [1, 2, 3, 4]
# list2 = [10, 11, 12, 13]

# Expected Output:
# {(1, 11), (2, 10), (3, 13), (4, 12)}
# (Explanation: Only pairs where sum is even are included.)

list1 = [1, 2, 3, 4, 5]
list2 = [19, 11, 11, 13, 15]

def unique_pairs(lst1, lst2):
  return set((lst1[i], lst2[i]) for i in range(len(lst1)) if (lst1[i]+lst2[i]) % 2 == 0)

print(unique_pairs(list1, list2))




