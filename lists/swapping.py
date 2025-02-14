# In friends list swap every 2 names with eachother
# Expected result: ['george', 'colt', 'nick', 'sam', 'eleni', 'stella']

friends = ['colt', 'george', 'sam', 'nick', 'stella', 'eleni']

for i in range(0, len(friends), 2):
   friends[i], friends[i + 1] = friends[i + 1], friends[i]

print(friends)