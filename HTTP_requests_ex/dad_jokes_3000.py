from requests import get
from termcolor import colored
from pyfiglet import figlet_format

# DAD JOKES 3000 app

def filter_jokes(search_term):
    url = "https://icanhazdadjoke.com/search"

    response = get(
        url, headers={"Accept": "application/json"}, params={"term": search_term}
    )

    data = response.json()

    try:
        i = 0

        total = data["total_jokes"]

        while i < total + 1:
            if total > 0:
                print(
                    colored(f"Joke: {i + 1}/{data['total_jokes']}", color="light_green")
                )  # Print number of joke in the list
            else:
                raise IndexError(
                    f'There are no jokes in database for term: "{search_term}"'
                )

            print(
                colored(data["results"][i]["joke"], color="light_cyan")
            )  # Print actual joke
            next_joke = input(colored("Go to next joke (Y/n): ", color="grey")).lower()

            if (next_joke == "Y".lower()) and (i == total - 1):
                print(
                    colored(
                        "You've reached the end of the jokes list!",
                        color="light_green",
                    )
                )
                break
            elif next_joke == "Y".lower():
                i += 1
            else:
                print(colored("Hope you enjoyed and see you soon!!", color="magenta"))
                break

    except IndexError as err:
        print(colored(err, color="red"))


print(colored(figlet_format("DAD JOKES 3000"), color="light_magenta"))
topic = input("Please provide a topic: ")

filter_jokes(topic)
