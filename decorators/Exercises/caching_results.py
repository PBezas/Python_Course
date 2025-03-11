# Exercise 4: Caching Function Results
# Create a decorator called cache that stores function results to avoid redundant calculations.

# def multiply(a, b):
#     print("Computing...")
#     return a * b

# print(multiply(2, 5))
# print(multiply(2, 5))

# Expected Output:
# Computing...
# 10
# 10
# (The second call should not print "Computing..." because the result is cached.)

from functools import wraps

def cache(fn):
    cached = None

    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal cached
        if cached is None: # The first time cached == None so...
            cached = fn(*args, **kwargs) # ...add function is invoked ('Computing...' is printed because it is invoked inside add function) and the result of it (x + y) is returned and stored inside cached variable...
            return cached # ...then this result (x + y) is returned.
        else:
            return cached # The second time, cached variable has already a value from first call (x + y) so it's not false, so it goes straight to else block, where it just returns the stored number (x + y) and not invoking the function thus not invoking print ('Computing...') as well.

    return wrapper


@cache
def add(x, y):
    print("Computing...")
    return x + y


print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
print(add(1, 5))
