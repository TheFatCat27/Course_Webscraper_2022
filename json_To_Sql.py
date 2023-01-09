import json
import os
import sqlite3


def json_to_sqlite(file_name):

    course_no = 0

    connection = sqlite3.connect("database.db")
    cursor1 = connection.cursor()

    sqlite_delete_all_query = """DELETE FROM courses"""
    cursor1.execute(sqlite_delete_all_query)

    f = open(file_name)
    data = json.load(f)

    #this part takes out the data from the json file and inserts it into the database

    for degree in data:
        courses = data[degree]
        for course in courses:
            course_degree = degree
            course_id = course_no
            course_code = course
            course_title = courses[course][0]
            course_description = courses[course][1]
            points = float(courses[course][2].split()[0])

            sqlite_insert_query = """INSERT INTO courses (Course_Degree, Course_ID, Course_Code, Course_Title, Course_Description, Points) VALUES (?,?,?,?,?,?)"""

            with connection as conex:
                cursor1.execute(sqlite_insert_query, [course_degree, course_id, course_code, course_title, course_description, points])
                conex.commit()

            course_no += 1

    print("Finished insertion!")
