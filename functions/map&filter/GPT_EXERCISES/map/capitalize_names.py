# Capitalize Names in a Dictionary
# Given a dictionary where keys are people’s IDs and values are their names:

# people = {101: "john doe", 102: "jane smith", 103: "alice cooper"}
# Use map() to capitalize each name correctly (e.g., "john doe" → "John Doe").

people = {101: "john doe", 102: "jane smith", 103: "alice cooper"}

def capitalize_names(people):
    return dict(map(lambda item: (item[0], ' '.join([word.capitalize() for word in item[1].split()])), people.items()))

print(capitalize_names(people))

# or

# def capitalize_names(people):
#     return dict(map(lambda item: (item[0], item[1].title()), people.items()))  # .title() capitalizes both first and last names without manually splitting/joining.

# print(capitalize_names(people))