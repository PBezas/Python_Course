from bs4 import BeautifulSoup
import requests
from scrape_quotes import BASE_URL


def get_author_details(quote):
    bio_page_url = BASE_URL + quote["bio_link"]
    bio_page_html = requests.get(bio_page_url)
    bio_soup = BeautifulSoup(bio_page_html.text, "html.parser")
    birthday = bio_soup.find(class_="author-born-date").get_text()
    birthplace = bio_soup.find(class_="author-born-location").get_text()

    return {
        "birthdate": birthday,
        "birthplace": birthplace,
    }
