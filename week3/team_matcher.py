# team_matcher.py
import requests

import random


class TeamMatcher:

    def __init__(self, path):
        self.path = path
        self.result_of_request = TeamMatcher.make_request(self.path)

    def make_request(path):
        req = requests.get(path, verify=False)
        if req.status_code == 200:
            result = req.json()
            return result

    def list_courses(self):
        courses = []
        #result_of_request = self.make_request()
        for each in self.result_of_request:
            for course in each['courses']:
                if course['name'] not in courses:
                    courses.append(course['name'])
        return courses

    def print_courses(self):
        for index, value in enumerate(self.list_courses()):
            print (index + 1, value)

    def get_people(self, course_name, group_time):
        people_in_course = []
        for each in self.result_of_request:
            # if each['available']:
            for course in each['courses']:
                if((course['name'] == course_name) and (
                        course['group'] == group_time)):
                    people_in_course.append(each['name'])
        return people_in_course

    def match_teams(self, course_id, team_size, group_time):
        course_name = self.list_courses()[course_id]
        people = self.get_people(course_name, group_time)
        random.shuffle(people)
        start = 0
        step = team_size
        while (start + step < len(people)):
            for each in people[start: start + step]:
                print (each)
            print ('======')
            start += step
        if start + step == len(people):
            for each in people[start:start + step]:
                print(each)
            print ("======")
        else:
            for each in people[start: len(people)]:
                print (each)

    def main_function(self):
        print(
            "Hello, you can use one the the following commands:" +
            " list_courses - this lists all the courses that are" +
            " available now. match_teams < course_id > ," +
            " < team_size > , < group_time >"
        )
        while True:
            option = input("Enter command>")
            option = option.split(" ")
            #courses = self.list_courses()
            #print(option)
            if option[0] == "list_courses":
                self.print_courses()
            elif option[0] == "match_teams":
                course_id = int(option[1]) - 1
                team_size = int(option[2])
                group_time = int(option[3])
                if group_time > 2 or group_time < 1:
                    print("error")
                    break
                elif course_id >= len(self.list_courses()):
                    print("error")
                    break
                else:
                    self.match_teams(course_id, team_size, group_time)
                    break

#def make_request(path):
#    req = requests.get(path, verify=False)
#    if req.status_code == 200:
#        result = req.json()
#        return result


#def list_courses():
#    result_of_request = make_request('https://hackbulgaria.com/api/students/')
#    courses = []
#    for each in result_of_request:
#        for course in each['courses']:
#            if course['name'] not in courses:
#                courses.append(course['name'])
#    return courses


#def print_courses(courses_list):
#    for index, value in enumerate(courses_list):
#        print (index + 1, value)


#def get_people(result, course_name, group_time):
#    people_in_course = []
#    for each in result:
#        # if each['available']:
#        for course in each['courses']:
#            if((course['name'] == course_name) and (
#                    course['group'] == group_time)):
#                people_in_course.append(each['name'])
#    return people_in_course


#def match_teams(course_id, team_size, group_time):
#    result = make_request('https://hackbulgaria.com/api/students/')
#    course_name = list_courses()[course_id]
#    people = get_people(result, course_name, group_time)
#    make_teams(people, team_size)


#def make_teams(all_people, size):
#    random.shuffle(all_people)
#    start = 0
#    step = size
#    while (start + step < len(all_people)):
#        for each in all_people[start: start + step]:
#            print (each)
#        print ('======')
#        start += step
#    if start + step == len(all_people):
#        for each in all_people[start:start + step]:
#            print(each)
#        print ("======")
#    else:
#        for each in all_people[start: len(all_people)]:
#            print (each)


#def main_function():
#    print(
#        "Hello, you can use one the the following commands:" +
#        " list_courses - this lists all the courses that are" +
#        " available now. match_teams < course_id > ," +
#        " < team_size > , < group_time >"
#    )
#    #result = make_request('https://hackbulgaria.com/api/students/')
#    while True:
#        option = input("Enter command>")
#        option = option.split(" ")
#        courses = list_courses()
#        print(option)
#        if option[0] == "list_courses":
#            print_courses(courses)
#        elif option[0] == "match_teams":
#            course_id = int(option[1]) - 1
#            team_size = int(option[2])
#            group_time = int(option[3])
#            if group_time > 2 or group_time < 1:
#                print("error")
#                break
#            elif course_id >= len(list_courses()):
#                print("error")
#                break
#            else:
#                match_teams(course_id, team_size, group_time)
#                break


def main():
#    main_function()
    matcher = TeamMatcher('https://hackbulgaria.com/api/students/')
    matcher.main_function()


if __name__ == '__main__':
    main()
