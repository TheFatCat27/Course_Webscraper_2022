import requests
import json
from bs4 import BeautifulSoup
from Scraper import dict_of_courses
from json_To_Sql import json_to_sqlite

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
    dict_of_course = dict_of_courses(list_of_links)
    print(*dict_of_course, sep="\n")

    open("myfile.json", "w").close()
    with open("myfile.json", "w") as f:
        json.dump(dict_of_course, f, indent=6)

    json_to_sqlite("myfile.json")

if __name__ == "__main__":
    main()
