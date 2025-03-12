# add_user
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# add_user : Takes in a first name and a last name and adds a new user to the users.csv file.

from csv import writer


def add_user(first, last):
    with open("./users.csv", 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])


add_user("Panos", "Bezas")
