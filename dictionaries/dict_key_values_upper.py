user = {
    'first': 'Panos',
    'last': 'Bezas',
    'age': 37,
    'ownsDog': True,
    'ownsCat': False,
}

# Iterate through every key-value pair in user, return capitalized key-versions and 
# if value is string return capitalized value-version else return the value

new_user = {key.upper() : (value.upper() if type(value) == str else value) for key, value in user.items()}

print(new_user)