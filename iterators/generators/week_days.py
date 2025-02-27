# Week Generator Exercise
# Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.

# Expected use:

# days = week()

# next(days)  # 'Monday'
# next(days)  # 'Tuesday'
# next(days)  # 'Wednesday'
# next(days)  # 'Thursday'
# next(days)  # 'Friday'
# next(days)  # 'Saturday'
# next(days)  # 'Sunday'
# next(days)  # StopIteration


def week():
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day = 0

    while day < len(weekdays):
        yield weekdays[day]
        day += 1


weekdays = week()

# for day in weekdays:
#     print(day)

# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
# print(next(weekdays))
