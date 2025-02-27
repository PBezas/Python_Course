# get_multiples
# Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the first count multiples of the number.

# The default number should be 1, and the default count should be 10.

# Expected output:
"""
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def get_multiples(num=1, count=10):
    for num in range(num, (num * count) + 1, num):
        yield num


def_multiples = get_multiples()
print(list(def_multiples))

evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
