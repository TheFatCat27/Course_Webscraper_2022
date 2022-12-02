import requests
from bs4 import BeautifulSoup


def main():
    list_of_links = []
    website_html = requests.get("https://www.calendar.auckland.ac.nz/en/courses/subject-index.html").content
    soup = BeautifulSoup(website_html, "html.parser", from_encoding="utf-8")

    for i in soup.select("td a"):
        if i["href"].count("/") == 6:
            list_of_links.append(str(i["href"]))

    '''
    Line below clears duplicate of links due the uni's inability to keep an organised website 
    '''
    list_of_links = list(dict.fromkeys(list_of_links))


if __name__ == "__main__":
    main()
