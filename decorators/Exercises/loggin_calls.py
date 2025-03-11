# Exercise 2: Logging Function Calls
# Create a decorator called logger that prints the name of the function being called and its arguments.

# def add(a, b):
#     return a + b

# print(add(3, 4))

# Expected Output:
# Calling function: add with arguments: (3, 4)
# 7

from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {fn.__name__} with arguments: {args}, {kwargs}")
        return fn(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


add(2, 3)
