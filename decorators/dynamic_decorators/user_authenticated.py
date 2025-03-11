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

def authenticate(access):
  def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      if access:
        return fn(*args, **kwargs)
      print('Access denied!')
    return wrapper
  return decorator

user_authenticate = True

@authenticate(user_authenticate)
def protected_fn():
  print('Access granted!')

protected_fn()

user_authenticate = False

@authenticate(user_authenticate)
def protected_fn():
  print('Access granted!')

protected_fn()

