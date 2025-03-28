from csv import DictReader
from store_quotes import csv_file

def read_quotes_from_csv():
    with open(csv_file, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)
