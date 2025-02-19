# You have a dictionary of students and their scores:

# students = {"Alice": 85, "Bob": 42, "Charlie": 78, "David": 90, "Eve": 55}
# Use filter() to keep only the students who scored 60 or above.

students = {"Alice": 85, "Bob": 42, "Charlie": 78, "David": 90, "Eve": 55}

def get_suceeded_students(students):
  return dict(filter(lambda s: s[1]>=60, students.items()))

print(get_suceeded_students(students))

# get only students names with map-filter and with list-comprehension

def get_students_names(students):

  return list(map(lambda s: s[0], filter(lambda s: s[1]>=60, students.items())))

def get_students_names(students):
  return [name for name,score in students.items() if score >= 60]

print(get_students_names(students))



