def decorator_fn(original_fn):
    def wrapper_fn():  # 2: decorator_fn when invoked, invokes wrapper_fn
        return original_fn()

    return wrapper_fn  # 3: decorator returns wrapper_fn without invoking it


def display():
    print("decorated_fn ran!")


decorated_fn = decorator_fn(
    display
)  # 1: decorator_fn invoked with display fn as an argument
# 4: decorated_fn now holds the wrapper_fn and waits to be invoked

print(decorated_fn())  # 5: when decorated_fn is invoked:
                          # a: wrapper_fn is invoked behind the scenes:
                            # i: wrapper_fn invokes original_fn (which is display fn here)
                              # 1: original_fn (display fn) prints 'decorated_fn ran!'
                            # ii: wrapper_fn returns original_fn's (display fn) result
                          # b: prints 'decorated_fn ran!

# ---------------------------------------------------------------------------------------------

def decorator_fn(original_fn):
    def wrapper_fn(): 
        return original_fn()

    return wrapper_fn

@decorator_fn # 1: when @decorator_fn is added before the display, actually creates a new display fn in which wrapper_fn
              #    is assigned that takes initial display fn as an argument
              # basically this happens: display = decorator_fn(display)
def display():
    print("decorated_fn ran!")

display() # 2: So when new display fn is invoked, it invokes wrapper_fn from decorator_fn and so on....
