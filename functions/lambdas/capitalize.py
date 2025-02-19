names = ['stella', 'giorgios', 'minos', 'eleni']

capitalized = map(lambda name: name[0].upper() + name[1:], names)

print(list(capitalized))