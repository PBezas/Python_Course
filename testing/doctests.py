def contains_purple(*args):
    """checks if args contains purple
    >>> contains_purple('purple')
    True
    """
    return "purple" in args


def capitalize(string):
    """capitalizes the first letter in the given string
    >>> capitalize('dog')
    'Dog'
    """
    return f"{string[0].upper()}{string[1:]}"


def compact(lst):
    """returns a list of all truthy elements from a list
    >>> compact([0, 1, 'a', True, False, 'b', None])
    [1, 'a', True, 'b']
    """
    return [el for el in lst if el]
