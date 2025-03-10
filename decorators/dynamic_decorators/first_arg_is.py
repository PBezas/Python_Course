from functools import wraps

def ensure_first_arg_is(value):
  def inner_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if args and args[0] == value:
          return fn(*args, **kwargs)
        return f'Invalid! First argument must be {value}'
    return wrapper
  return inner_decorator 

@ensure_first_arg_is('burrito')
def fav_foods(*foods):
  return foods

print(fav_foods('burrito', 'ice cream'))
print(fav_foods('ice cream', 'buritto'))
print(fav_foods())

# When fav_foods is invoked:
# 1: At first inner_decorator is returned with initial fav_foods
# 2: Then wrapper_fn is returned with fav_foods args and kwargs
# 3: wrapper logic rans:
    # a: if conditional logic passed fav_foods takes initial fav_foods with args and kwargs passed in it
    # b: else 'Invalid blah blah ...' is returned

#  !!! Basically, def inner_decorator(fn) is a decorator that is returned through another decorator (ensure_first_arg_is(val)) which takes the value as argument!!!


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
  return num1 + num2

print(add_to_ten(10, 2))
print(add_to_ten(1, 2))