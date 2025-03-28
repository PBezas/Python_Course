from random import choice
from get_author_details import get_author_details


def get_random_quote(all_quotes):
    random_quote = choice(all_quotes)
    details = get_author_details(random_quote)

    return {
        "quote": random_quote["quote"],
        "author": random_quote["author"],
        "birthdate": details["birthdate"],
        "birthplace": details["birthplace"],
    }
