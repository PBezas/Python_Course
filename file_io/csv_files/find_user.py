# find_user
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. If the user is found, find_user  returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found.

from csv import reader

def find_user(first, last):
  with open('./users.csv') as file:
    csv_reader = reader(file)
    for (i,row) in enumerate(csv_reader):
      if (row[0] == first) and (row[1] == last):
        return i
    return 'Not Here not found.'
      
print(find_user('Colt', 'Steele'))
print(find_user('Grace', 'Hopper'))
print(find_user('Alan', 'Turing'))