from bs4 import BeautifulSoup
import requests

BASE_URL = "https://quotes.toscrape.com/"

all_quotes = []


def scrape_quotes():
    url = "/page/1"
    while True:
        html = requests.get(BASE_URL + url)
        soup = BeautifulSoup(html.text, "html.parser")

        quotes = soup.find_all(class_="quote")
        page_quotes = []
        for quote in quotes:
            quote_text = quote.find(class_="text").get_text()
            quote_author = quote.find(class_="author").get_text()
            bio_link = quote.find("a")["href"]
            page_quotes.append(
                {
                    "author": quote_author,
                    "quote": quote_text,
                    "bio_link": bio_link,
                }
            )

        all_quotes.extend(page_quotes)

        next_btn = soup.find(class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            url = next_page
        else:
            break
    return all_quotes
