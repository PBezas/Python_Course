from functools import wraps

def enforce_types(*types):
  def decorator_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      # args by default are not mutable because it's a list of tupples so we should first convert this list to something mutable
      new_args = []
      for (a,t) in zip(args,types):
        new_args.append(t(a))
      return fn(*new_args, **kwargs)
    return wrapper
  return decorator_fn

@enforce_types(str, int)
def repeat_msg(msg, times):
  for time in range(times):
    print(msg)

repeat_msg('hello', '3')
repeat_msg(19, '5')

@enforce_types(float, float)
def divide(a, b):
  print(a/b)

divide(10, 2) # 5.0
divide('5', '2') # 2.5
