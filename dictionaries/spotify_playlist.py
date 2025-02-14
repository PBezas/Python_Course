playlist = {
  'title': 'Playlist',
  'playlist_name' : 'Patagonia Bus',
  'created_by' : 'Colt Steele',
  'songs': [
  {
    'name': 'Turn it off', 
    'artist': ['Culture Abuse'], 
    'album': 'Peach', 
    'duration': 3.37},
    {
      'name' : 'Eating hooks',
      'artist' : ['Moderat', 'Siriusmo', 'Solomun'],
      'album' : 'Eating hooks',
      'duration': 7.02  
    },
    {
      'name' : 'Night off',
      'artist' : ['Siriusmo'],
      'album' : 'Mosaik',
      'duration' : 4.08
    },
    {
      'name' : 'Don\'t stop',
      'artist' : ['Knightlife'],
      'album' : 'Cat Copy',
      'duration' : 6.13
    }
  ]
}

total_duration = 0
for song in playlist['songs']:
  total_duration += song['duration']

playlist['num_of_songs'] = len(playlist['songs'])
playlist['total_duration'] = total_duration

print(playlist)