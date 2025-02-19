# Given a dictionary of employees with their salaries:

employee_list = [
  {"name": "Alice", "salary": 50000},
  {"name": "Bob", "salary": 60000},
  {"name": "Charlie", "salary": 55000}
  ]

# increase each salary by 10%

def increase_salaries(employees: list, multiplier: float):
  return list(map(lambda e: {'name': e['name'], 'salary': (round(e['salary'] * multiplier))}, employees))

employee_list = increase_salaries(employee_list, 1.1)

print(employee_list)