# yes_or_no
# Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.

# Expected use:
# gen = yes_or_no()
"""
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
"""


def yes_or_no():
    results = ("yes", "no")

    while True:
        for res in results:
            yield res


gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
