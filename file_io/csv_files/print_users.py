# print_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# print_users : prints out all of the first and last names in the users.csv file

from csv import reader

def print_users():
  with open('./users.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
      print(f'{row[0]} {row[1]}')

print_users()