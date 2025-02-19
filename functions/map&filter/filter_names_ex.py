names = ['anthony', 'austin', 'margaret', 'aurelia', 'entropia']

def filter_names (names): return list(filter(lambda name: name[0] == 'a' , names))

print(filter_names(names))