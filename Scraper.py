import requests
from bs4 import BeautifulSoup

def dict_of_courses(list_of_links):
    course_dict = {}
    for link in list_of_links:
        paper_dict = {}
        URL = link
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="regs")
        course_name = results.find("h1")
        course_papers = results.find_all("div", class_="coursePaper section")
        for course in course_papers:
            if course.find("p", class_="prerequisite") == True:
                paper = course.find("div", class_="courseA")
                title = course.find("p", class_="title")
                descr = course.find("p", class_="description")
                prerq = course.find("p", class_="prerequisite")
                points = course.find("div", class_="points")
                paper_dict[paper.text.strip()] = [title.text.strip(), descr.text.strip(), prerq.text.strip(), points.text.strip()]
            else:
                paper = course.find("div", class_="courseA")
                title = course.find("p", class_="title")
                descr = course.find("p", class_="description")
                points = course.find("div", class_="points")
                paper_dict[paper.text.strip()] = [title.text.strip(), descr.text.strip(), points.text.strip()]
        course_dict[course_name.text.strip()] = paper_dict
    return course_dict

