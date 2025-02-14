friends = ['colt', 'george', 'sam', 'nick', 'stella', 'eleni']

friendsCapitalized = [friend[0].upper() + friend[1:] for friend in friends]

print(friendsCapitalized)

# >>> JAVASCRIPT EQUIVELANT <<<
# const friendsCapitalized = friends.map(friend => friend[0].toUpperCase() + friend.slice(1))

# console.log(friendsCapitalized)