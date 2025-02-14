# Return 'odd' for odd numbers, 'even' for even numbers and 'UNLUCKY' for 4 and 13 in a range of numbers from 1 to 20(inclusive)

#  ----------------------1st way----------------------

# (with loop)

for i in range(1, 21):
  if i == 4 or i == 13:
    state = 'UNLUCKY!'
  elif i % 2 == 0:
    state = 'even'
  else:
    state = 'odd'
  print(f'(with loop) >> {i} is {state}')

#  ----------------------2nd way----------------------

#  (with List Comprehension)

numbers = [f'{num} is UNLUCKY' if num == 4 or num == 13 else f'{num} is even' if num % 2 == 0 else f'{num} is odd' for num in range(1,21)]

for val in numbers:
  print(f'(with LC) >> {val}')