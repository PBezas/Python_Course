# === Data Processing with Comprehensions & Functions
# Write a function process_data that takes a list of dictionaries representing student records. Each dictionary has "name", "scores" (a list of integers), and "passed" (a boolean).

# Your function should:

# Use list comprehension to filter students who passed.
# Use dictionary comprehension to create a new dictionary mapping names to their average scores.
# Use *args in a helper function to calculate the average score.

# === Example Input:
# students = [
#     {"name": "Alice", "scores": [85, 90, 88], "passed": True},
#     {"name": "Bob", "scores": [60, 50, 55], "passed": False},
#     {"name": "Charlie", "scores": [78, 82, 80], "passed": True}
# ]

# === Expected Output:
# {'Alice': 87.67, 'Charlie': 80.0}

students = [
    {"name": "Alice", "scores": [85, 90, 88], "passed": True},
    {"name": "Bob", "scores": [60, 50, 55], "passed": False},
    {"name": "Charlie", "scores": [78, 82, 80], "passed": True}
]

def count_avg_score(*scores):
  return round(sum(scores)/len(scores),2)
   

def get_students_passed(students):
  students_passed = {student['name']:count_avg_score(*student['scores']) for student in students if student['passed']}

  return students_passed

print(get_students_passed(students))