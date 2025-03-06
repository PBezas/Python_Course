# Exercise 5: Chunk Iterator
# Create an iterator class called ChunkIterator that takes an iterable and a chunk size. The iterator should yield chunks of the given size as lists.

# Example usage:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# chunker = ChunkIterator(numbers, 3)
# for chunk in chunker:
#     print(chunk)

# Expected output:

# [1, 2, 3]
# [4, 5, 6]
# [7, 8]


class ChunkIterator:
    def __init__(self, lst, size):
        self.lst = lst
        self.size = size
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        start = 0
        while self.size < len(self.lst):
            end = self.size

            yield numbers[start:end]
            start = end
            self.size += self.size


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(numbers[0:self_size])
# print(numbers[self_size: self_size * 2])
# print(numbers[s])

chunkIt = ChunkIterator(numbers, 3)

for chunk in chunkIt:
    print(chunk)
