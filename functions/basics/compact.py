# compact
# Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

# compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]

def compact(lst):
  return [el for el  in lst if el]

print(compact([0, 2, False, 'Yo', None, 'Hello!', '']))