# intersection
# Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.

# intersection([1,2,3], [2,3,4])    #[2,3]
# intersection(['a','b','z'], ['x','y','z']) .  # ['z']

# --------------------1st Way(my solution)------------

# def intersection(lst1, lst2):
#     intersection = set(lst1).intersection(set(lst2))

#     return list(intersection)

# --------------------2nd Way-------------------------
# doesn't return unique values because it's on passed through set

# def intersection(lst1, lst2):
#     return [val for val in lst1 if val in lst2]

# --------------------3rd Way(VERY GOOD)--------------

# def intersection(lst1:list, lst2):
#     return list(set(lst1) & set(lst2))

# --------------------4th Way(BEST & CLEANER)---------

def intersection(lst1, lst2):
    return [val for val in set(lst1) & set(lst2)]

print(intersection([1,2,3,3,5,6],[2,3,4,5,5,7]))

