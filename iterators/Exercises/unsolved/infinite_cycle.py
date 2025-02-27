# Exercise 2: Infinite Iterator
# Create an infinite iterator called Cycle that cycles through a given list indefinitely.

# Example usage:

# cycler = Cycle([1, 2, 3])
# for i, num in enumerate(cycler):
#     print(num)
#     if i == 5:
#         break
# Expected output:

# 1
# 2
# 3
# 1
# 2
# 3


class Cycle:
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        return iter(self.nums)

    def __next__(self):
        i = 0
        cycle = 0
        while True:
            if i >= len(self.nums):
                i = 0
                cycle += 1
            yield cycle
            i += 1


cycler = Cycle((1, 2, 3))
for i in cycler:
  print(i)
    # if i == 5:
    #     break
