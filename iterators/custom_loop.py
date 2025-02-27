def custom_loop(itterable, func):
    iterator = iter(itterable)

    while True:
        try:
            func(next(iterator))
        except StopIteration:
            break


lst = [1, 2, 3, 4, 5]
string = "PanosBezas"

custom_loop(string, print)
