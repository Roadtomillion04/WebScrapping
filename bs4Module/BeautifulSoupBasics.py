from bs4 import BeautifulSoup

with open('./bs4Module/home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    #instancing BeautifulSoup class
                         #String,  #format - lxml not html because lxml can also get broken html code
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify()) #prettify  makes it nice to read

    # courses_html_tag = soup.find_all('h5') #Finds all code starting with h5 returns in a list
    # #print(courses_html_tag)
    #
    # for course in courses_html_tag:
    #     print(course.text) #grabs the text part in html file

    '''To grab name and price of the courses'''
                #the thing line starts,  # we provided class_ because default class is in-built
    course_cards = soup.find_all('div', class_ = 'card')

    for course in course_cards:
        course_name = course.h5.text #h5 and a are line starts with
        course_price = course.a.text.split()[-1] #As it is a string and -1 index grabs last element i.e 20$

       #print(course_name, course_price) #To make it more dynamic
        print(f'{course_name} costs {course_price}')