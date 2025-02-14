friends = ['Colt', 'George', 'Sam', 'Nick', 'Stella', 'Eleni']

my_friends = ''

for friend in friends:
    if friends.index(friend) == len(friends) - 1:
        my_friends += f' and {friend}'
    elif friends.index(friend) == 0:
        my_friends += friend
    else:
       my_friends += f', {friend}'

print(f'My friends list is: {my_friends}')
