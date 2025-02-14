friends = ['colt', 'stella', 'nick', 'eleni']


# LEN >> gives the length of a list

friends_length = len(friends) # > 4

# INDEX >> returns the index of the first instance of the given element if it exists

friends.index('nick') # > 2

# APPEND >> adds element at the end of the list

friends.append('sam') # > friends = ['colt', 'stella', 'nick', 'eleni', 'sam']

# EXTEND >> merges a list into another list

friends.extend(['maria', 'minos']) # > friends = ['colt', 'stella', 'nick', 'eleni', 'sam', 'maria', 'minos']

# INSERT >> inserts an element in a specific position inside the list

friends.insert(3, 'minos') # > friends = ['colt', 'stella', 'nick', 'minos', 'eleni', 'sam', 'maria', 'minos']

# COUNT >> returns the number of times one element is present in a list

friends.count('minos') # > 2

# POP() >> deletes the last element from the list and returns that element

friends.pop() # returns > 'minos' 
              # > friends = ['colt', 'stella', 'nick', 'minos', 'eleni', 'sam', 'maria']

# POP(i) >> deletes the element that exist on the given index and returns that element

friends.pop(1) # returns > 'stella' 
               # > friends = ['colt', 'nick', 'minos', 'eleni', 'sam', 'maria']

# REMOVE >> deletes the first instance of the given element in the list and returns None

friends.remove('eleni') # > friends = ['colt', 'nick', 'minos', 'sam', 'maria']

# REVERSE >> reverses the order of which the elements are presented in the list

friends.reverse() # > friends = ['maria', 'sam', 'minos', 'nick', 'colt']

# SORT >> sorts the list in alphabetical or numerical order

friends.sort() # > friends = ['colt', 'maria', 'minos', 'nick', 'sam']

# COPY >> returns a shallow copy of the list

friends_clone = friends.copy() # > friends_clone = ['colt', 'maria', 'minos', 'nick', 'sam']

# SLICE[start:end:step] >> returns a part of the list according to the given arguments

    ### >> returns the part from index 1 till the end

sliced_friends = friends[1:] # > sliced_friends = ['maria', 'minos', 'nick', 'sam']

    ### >> returns the part from index 1 to index 3(excluded)

sliced_friends1 = friends[1:3] # > sliced_friends1 = ['maria', 'minos']

    ### >> returns the part from index 0 to index 5(excluded) by step of 2

sliced_friends2 = friends[0:5:2] # > sliced_friends2 = ['colt', 'minos', 'sam']
      # or # 
sliced_friends2 = friends[::2]

# CLEAR >> deletes all the elements in the list and returns None

friends.clear() # > friends = []


