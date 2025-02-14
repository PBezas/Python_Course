person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# expected result: answer = {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# ------------1st way--------------------

answer = {i[0]:i[1] for i in person}

# ------------2nd way--------------------

# answer = {key:value  for key, value in person}

# ------------3rd way--------------------

# answer = dict(person)

print(answer)