from get_random_quote import get_random_quote
from read_quotes_from_csv import read_quotes_from_csv

all_quotes = read_quotes_from_csv()
random_quote = get_random_quote(all_quotes)

print(random_quote["quote"])


guesses = 6
i = 1


while i < guesses:
    answer = input("Who is the author? ")
    if answer != random_quote["author"]:
        if i == 1:
            print(
                f"Remaining guesses: {guesses - (i + 1)}\n Hint{i}: Born on {random_quote['birthdate']}"
            )
            i += 1
        elif i == 2:
            print(
                f"Remaining guesses: {guesses - (i + 1)}\n Hint{i}: Born {random_quote['birthplace']}"
            )
            i += 1
        elif i == 3:
            name_first = random_quote["author"].split(" ")[0][0]
            print(
                f"Remaining guesses: {guesses - (i + 1)}\n Hint{i}: First name starts with: {name_first}"
            )
            i += 1
        elif i == 4:
            lastname_first = random_quote["author"].split(" ")[1][0]
            print(
                f"Remaining guesses: {guesses - (i + 1)}\n Hint{i}: Last name starts with {lastname_first}"
            )
            i += 1
        else:
            print(f"You lose! The author was {random_quote['author']}")
            start_again = input("Do you want to play again?(y/n): ")
            if start_again.lower() in ("y", "yes"):
                i = 1
                random_quote = get_random_quote(all_quotes)
                print(random_quote["quote"])
            else:
                print("Thank you for playing. See you next time!")
                break
    else:
        print("Congrats! You got it right!")
        start_again = input("Do you want to play again?(y/n): ")
        if start_again.lower() in ("y", "yes"):
            i = 1
            random_quote = get_random_quote(all_quotes)
            print(random_quote["quote"])
        else:
            print("Thank you for playing. See you next time!")
            break
