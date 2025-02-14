
for num in range(1,11, 2):
    space_num = 5
    while space_num >= 1:
      print(f'{space_num*" "}\U0001f600' * num)
      space_num -= 1

# num = 1
# while num <= 10 :
#   print('\U0001f600' * num)
#   num += 1   
