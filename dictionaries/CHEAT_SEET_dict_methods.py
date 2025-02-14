user = {
    'first': 'Panos',
    'last': 'Bezas',
    'age': 37,
    'ownsDog': True,
    'ownsCat': False,
}

# GET >> gets the value of the given key

user_age = user.get('age') # > 37
        # or #   
user_age2 = user['age'] # > 37

# COPY >> returns a shallow copy of the dictionary

user_clone = user.copy() # > user_clone = {'first': 'Panos', 'last': 'Bezas', 'age': 37, 'ownsDog': True, 'ownsCat': False}

# UPDATE >> merges the second dictionary to the first, overwiting any values in matching keys

user2 = {
   'age' : 23,
   'faveLang' : 'Python'
 }

user.update(user2) # > user = {'first': 'Panos', 'last': 'Bezas', 'age': 23, 'ownsDog': True, 'ownsCat': False, 'faveLang': 'Python'}

# FROMKEYS >> creates a new dictionary iterating through the first argument in order to create the keys and every key takes as value the second argument

default_user = {}.fromkeys(['first_name', 'last_name', 'favColor'], 'uknown') # > default_user = {'first_name': 'uknown', 'last_name': 'uknown', 'favColor': 'uknown'}

# KEYS >>  creates a list of all the keys inside the dictionary

dict_keys = user.keys() # > dict_keys = ['first', 'last', 'age', 'ownsDog', 'ownsCat', 'faveLang']

# VALUES >> creates a list of all the values inside the dictionary

dict_values = user.values() # > dict_values = ['Panos', 'Bezas', 23, True, False, 'Python']

# ITEMS >> creates a list of tupples of all the key-value pairs inside the dictionary

dict_items = user.items() # > dict_items = [('first', 'Panos'), ('last', 'Bezas'), ('age', 23), ('ownsDog', True), ('ownsCat', False), ('faveLang', 'Python')]

# POP >> deletes the key-value pair of the given key and returns it's value

user_clone.pop('ownsCat') # returns > False
                          # > user_clone = {'first': 'Panos', 'last': 'Bezas', 'age': 37, 'ownsDog': True}

# POPITEM >> deletes a random key-value pair from the dictionary and returns a tupple of the removed key-value pair

user_clone.popitem() # > returns > (removed_key, removed_value)

# CLEAR >> deletes everything inside the dictionary leaving an empty shell

user_clone.clear() # > user_clone = {}