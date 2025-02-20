# partition
# Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ). 

# The function should iterate over each element in the list and invoke the callback function at each iteration. 

# If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# When it's finished, partition should return both lists inside of one larger list, like so:

# [truthy_list, falsy_list]

lst_ex = range(0, 10)

def isEven(num):
    return num % 2 == 0

# ---------traditional way (my solution)---------------

# def partition(lst, callback_fn):
#   truthy_list = []
#   falsy_list = []

#   final_list = []

#   for num in lst:
#      if callback_fn(num):
#         truthy_list.append(num)
#      else:
#         falsy_list.append(num)
  
#   final_list.append(truthy_list)
#   final_list.append(falsy_list)
#   return final_list


#  -------- with list comprehension-----------------
def partition(lst, fn):

 return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


print(partition(lst_ex, isEven))
    
    