age = input('How old are you?: ')
if age:
    age = int(age)
    if (age >=18 and age <21) :
      print('You have to wear a wristband!')
    elif age >= 21 :
      print('Normal entry. You can drink!')
    else :
      print('Sorry! Too young!')
else:
   print('Please type in your age')