names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# return the name based on length

def get_longest(lst):
  longest_name = max(lst, key=lambda name: len(name))
  return f'The longest name in the list is {longest_name}'

# print(get_longest(names))

def get_shortest(lst):
  shortest_name = min(lst, key=lambda name: len(name))
  return f'The shortest name in the list is {shortest_name}'

# print(get_shortest(names))

# -------------------------------------------------------------

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

def get_most_played(lst):
  most_played = max(lst, key=lambda song: song['playcount'])['title']
  return f'The most played song in the list is "{most_played}"'

# print(get_most_played(songs))

def get_least_played(lst):
  least_played = min(lst, key=lambda song: song['playcount'])['title']
  return f'The least played song in the list is "{least_played}"'

# print(get_least_played(songs))

nums = [1, 5, 2, 102, -1, 12, 45]

def extremes(lst):
  return (min(lst), max(lst))

# print(extremes(nums))

# for x in list(range(0,10)).reverse():
#   print(x)