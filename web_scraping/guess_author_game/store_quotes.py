from scrape_quotes import scrape_quotes
from csv import DictWriter


csv_file = (
    "/Users/panos/Desktop/PythonCourse/web_scraping/guess_author_game/all_quotes.csv"
)


def store_quotes():
    scraped_quotes = scrape_quotes()
    with open(csv_file, "w") as file:
        headers = ["quote", "author", "bio_link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in scraped_quotes:
            csv_writer.writerow(quote)


if __name__ == "__main__":
    store_quotes()
