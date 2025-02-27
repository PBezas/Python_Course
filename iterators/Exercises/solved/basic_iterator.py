# Exercise 1: Basic Iterator
# Create a custom iterator class called CountUp that takes a starting integer and an ending integer. The iterator should yield numbers starting from the starting integer up to (but not including) the ending integer.

# Example usage:

# counter = CountUp(3, 7)
# for num in counter:
#     print(num)

# Expected output:

# 3
# 4
# 5
# 6


class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        raise StopIteration


counter = CountUp(3, 7)

for num in counter:
    print(num)
