users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# sort users

def sort_by_username(users, order):
  print(f'In {order}ending order...')
  is_reverse = order == 'desc'
  return sorted(users, key=lambda user: user['username'], reverse=is_reverse)

# print(sort_by_username(users, 'desc'))

def sort_by_tweets_num(users, order):
  print(f'In {order}ending order...')
  is_reverse = order == 'desc'
  return sorted(users, key=lambda user: len(user['tweets']), reverse=is_reverse)
 
# print(sort_by_tweets_num(users, 'desc'))

# ------------------------------------------------------------------------------

# sort songs

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

def sort_by_plays(lst, order):
   print(f'In {order}ending order...')
   is_reverse = order == 'desc'
   return sorted(lst, key=lambda song: song['playcount'], reverse=is_reverse)

# print(sort_by_plays(songs, 'asc'))

def sort_by_title(lst, order):
    print(f'In {order}ending order...')
    is_reverse = order == 'desc'
    return sorted(lst, key=lambda song: song['title'].lower(), reverse=is_reverse)

print(sort_by_title(songs, 'desc'))
