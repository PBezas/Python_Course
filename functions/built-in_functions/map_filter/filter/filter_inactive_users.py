users = [
      {'name': 'Sam', 'tweets': ['I love dogs', 'I have a horse']},
      {'name': 'Panos', 'tweets': []},
      {'name': 'Stella', 'tweets': ['Night out with friends']},
      {'name': 'Kostas', 'tweets': []},
      {'name': 'Olia', 'tweets': ['I\'m pregnant!!!']}
      ]


# inactive_users = list(filter(lambda user: not user['tweets'], users)) # empty list [] in python is a falsy value


# print(inactive_users)

inactive_user_names = list(map(lambda u: u['name'], filter(lambda u: not u['tweets'], users)))

print(inactive_user_names)