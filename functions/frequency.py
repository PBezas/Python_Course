# frequency
# Write a function called frequency. This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.

def frequency(collection, search_term):
    return collection.count(search_term)

print(frequency([False, True, True, True, False, True, False], True))