# make_song
# Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song about a the beverage. The number of verses in the song is determined by the count.

# Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples for details on the structure of the lyrics.)

# The default count should be 99, and the default beverage should be soda.

# Expected use:
"""
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
"""


def make_song(num=99, bev="soda"):
    while num >= 0:
        if num == 1:
            yield f"Only {num} bottle of {bev} left!"  # STOP: when num reaches 1 yields this and stops
            num -= 1  # NEXT(): when next() is called again loop starts from here with num = 1
        elif not num:
            yield f"No more {bev}!"  # STOP: when num reaches 0 yields this and stops
            num -= 1  # NEXT(): when next() is called again loop starts from here with num = 0
        else:
            yield f"{num} bottles of {bev} on the wall."  # STOP: unless num !=0 or !=1 every iteration stops here
            num -= 1  # NEXT(): when next() is called again, function is called, starts from here,
            # reduces num by 1 and starts while loop   again

    # raise StopIteration  # NEXT(): when function is called again with next() num which is 0 becomes -1,
    # # starts loop again, checks if -1 >= 0, it's not so it raises the StopIteration error


default_song = make_song(10, "soda")

print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
