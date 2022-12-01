import requests
from bs4 import BeautifulSoup


def main():
    website_html = requests.get("https://www.calendar.auckland.ac.nz/en/courses/subject-index.html").content
    soup = BeautifulSoup(website_html, "html.parser", from_encoding="utf-8")


if __name__ == "__main__":
    main()
