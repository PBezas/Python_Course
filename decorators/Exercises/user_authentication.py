# Exercise 5: Checking User Authentication
# Create a decorator called authenticate that only allows a function to run if the user is authenticated.

# user_authenticated = True

# def protected_function():
#     print("Access granted!")

# protected_function()

# user_authenticated = False
# protected_function()
# Expected Output:

# Access granted!
# Access denied!

from functools import wraps


def authenticate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if globals().get('user_authenticated'):
            return fn(*args, **kwargs)
        print("Access denied!")

    return wrapper


@authenticate
def protected_function():
    print("Access granted!")


user_authenticated = True
protected_function()

user_authenticated = False
protected_function()

user_authenticated = True
protected_function()
