# List Manipulation
# Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).

# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list

def list_manipulation(numbers, command, location, value = 4):
    if command == 'remove':
        if location == 'end':
            return numbers.pop()
        elif location == 'beginning':
            return numbers.pop(0)
    elif command == 'add':
        if location == 'end':
            numbers.append(value)
            return numbers
        elif location == 'beginning':
            numbers.insert(0, value)
            return numbers