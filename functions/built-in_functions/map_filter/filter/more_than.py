# Filter Employees Earning Above 55,000

# Using the:

# salaries = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
# use filter() to get only the employees earning more than $55,000.

salaries = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}

# def get_rich_employees(employees):
#   return dict(filter(lambda e: e[1] > 55000, employees.items()))


# print(get_rich_employees(salaries))

# get only the employees names, earning more than $55,000.

def get_rich_emloyees_names(employees):
   return list(map(lambda e: e[0], filter(lambda e: e[1] > 55000, employees.items())))

print(get_rich_emloyees_names(salaries))