# Exercise 1: Timing a Function
# Create a decorator called timer that calculates and prints the execution time of the decorated function.

# import time

# def slow_function():
#     time.sleep(2)
#     print("Function finished!")

# slow_function()

# Expected Output:
# Execution time: ~2.00 seconds
# Function finished!

from functools import wraps
from time import time, sleep


def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time() - start_time
        print(f"Execution time: ~{round(end_time, 2)}")
        return result
    return wrapper


@timer
def slow_fn():
    sleep(2)
    print("Function finished!")


slow_fn()
