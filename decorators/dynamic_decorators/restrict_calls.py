# Exercise 3: Restrict Function Calls
# Create a decorator called restrict_calls that restricts a function to be called only a limited number of times (e.g., 3 times). After that, it should print "Function call limit reached!".

# def limited_function():
#     print("Function is running!")

# limited_function()
# limited_function()
# limited_function()
# limited_function()
# Expected Output:

# Function is running!
# Function is running!
# Function is running!
# Function call limit reached!

from functools import wraps


def restrict_calls(limit):
    def decorator(fn):
        calls = 0
        @wraps(fn)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < limit:
                calls += 1
                return fn(*args, **kwargs)
            else:
              print("Function call limit reached!")

        return wrapper

    return decorator


@restrict_calls(3)
def limited_function():
    print("Function is running!")


limited_function()
limited_function()
limited_function()
limited_function()
