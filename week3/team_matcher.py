# team_matcher.py
import requests
import random


def make_request(path):
    req = requests.get(path, verify=False)
    if req.status_code == 200:
        result = req.json()
        return result


def list_courses():
    result_of_request = make_request('https://hackbulgaria.com/api/students/')
    courses = []
    for each in result_of_request:
        for course in each['courses']:
            if course['name'] not in courses:
                courses.append(course['name'])
    return courses


def print_courses(courses_list):
    for index, value in enumerate(courses_list):
        print (index + 1, value)


def get_people(result, course_name, group_time):
    people_in_course = []
    for each in result:
        # if each['available']:
        for course in each['courses']:
            if((course['name'] == course_name) and (
                    course['group'] == group_time)):
                people_in_course.append(each['name'])
    return people_in_course


def match_teams(course_id, team_size, group_time):
    result = make_request('https://hackbulgaria.com/api/students/')
    course_name = list_courses()[course_id]
    people = get_people(result, course_name, group_time)
    make_teams(people, team_size)


def make_teams(all_people, size):
    random.shuffle(all_people)
    start = 0
    step = size
    while (start + step < len(all_people)):
        for each in all_people[start: start + step]:
            print (each)
        print ('======')
        start += step
    if start + step == len(all_people):
        for each in all_people[start:start + step]:
            print(each)
        print ("======")
    else:
        for each in all_people[start: len(all_people)]:
            print (each)


def main_function():
    print(
        "Hello, you can use one the the following commands:" +
        " list_courses - this lists all the courses that are" +
        " available now. match_teams < course_id > ," +
        " < team_size > , < group_time >"
    )
    #result = make_request('https://hackbulgaria.com/api/students/')
    while True:
        option = input("Enter command>")
        option = option.split(" ")
        courses = list_courses()
        print(option)
        if option[0] == "list_courses":
            print_courses(courses)
        elif option[0] == "match_teams":
            course_id = int(option[1]) - 1
            team_size = int(option[2])
            group_time = int(option[3])
            if group_time > 2 or group_time < 1:
                print("error")
                break
            elif course_id >= len(list_courses()):
                print("error")
                break
            else:
                match_teams(course_id, team_size, group_time)
                break


def main():
    main_function()


if __name__ == '__main__':
    main()
