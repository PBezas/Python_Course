# ensure_fewer_than_three_args
# Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too many arguments!"

from functools import wraps

def ensure_fewer_than_3(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            return "Too many arguments!"
        return fn(*args, **kwargs)

    return wrapper


@ensure_fewer_than_3
def add(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    return result


print(add())  # 0
print(add(2, 3))  # 5
print(add(2, 3, 5))  # Too many arguments
print(add(2, 3, 5, 10))  # Too many arguments
