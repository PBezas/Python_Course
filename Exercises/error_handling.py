# Error Handling (Bonus)
# Problem: Write a function that safely converts a list of strings into integers. If a conversion fails, catch the error and store "Invalid" instead.

# data = ["10", "20", "abc", "30", "xyz"]
# Expected Output:

# [10, 20, 'Invalid', 30, 'Invalid']

data = ["10", "20", "abc", "30", "xyz"]


def convert_to_int(lst):
    new_lst = []
    for el in lst:
        try:
            new_lst.append(int(el))
        except ValueError:
            new_lst.append("Invalid")
    return new_lst


print(convert_to_int(data))
