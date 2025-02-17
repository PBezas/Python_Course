
# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]

# print(answer)

# answer2 = [name.lower()[::-1] for name in ['Elie', 'Tim', 'Matt']]

# print(answer2)

# answer3 =  [num for num in range(1,101) if num % 12 == 0]

# print(answer3)

# answer4 = [[i for i in range(0,3)] for i in range(1,4)]

# print(answer4)

lst1 = [1, 2 ,3 ,5]
lst2 = [1, 3 ,6 ,7]

lst3 = list(lst1).append(lst2)


print(lst3)