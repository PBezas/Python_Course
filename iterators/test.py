def get_beat(tpl):
    while True:
        yield from (tpl)


new_beat = get_beat((1, 2, 3, 4))

print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
print(next(new_beat))
