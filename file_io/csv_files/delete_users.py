# delete_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# delete_users : Takes in a first name and a last name. Updates the users.csv file so that any user whose first and last names match the inputs are removed. The function should return a count of how many users were removed

import csv

def delete_users(first, last):
  with open('./users.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    rows = list(csv_reader)

  count = 0
  with open('./users.csv', 'w') as csvfile:
     csv_writer = csv.writer(csvfile)
     for row in rows:
      if row[0] == first and row[1] == last:
          count += 1
      else:
        csv_writer.writerow(row)
  print(f'Users removed {count}')

delete_users('Panos', 'Bezas')