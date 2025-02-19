# reversed() vs list.reverse()

lst = list(range(0,10))

lst.reverse() # mutates the initial list (applies only on lists)

print(lst) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

lst = list(range(0,10))

reversed_lst = list(reversed(lst)) # creates a new reversed copy of the initial list (applies on every iterable)

print(reversed_lst) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]