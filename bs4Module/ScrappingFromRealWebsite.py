from bs4 import BeautifulSoup
import requests
                                 # THis is a link from TimesJobs - python Jobs search
html_text = requests.get(url = r'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
#at end of url link we put .text to grab html data

soup = BeautifulSoup(html_text, 'lxml')

'''Inspect the jobs to view html code'''
# job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')          #space, 'empty
# company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(" ", '')
# skill_requirements = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
#published_date = job.find('span', class_ = 'sim-posted').span.text # Because it has another child span inside
# print(company_name, skill_requirements, published_date)



'''Job filtering Project'''
# we can store job details in separate files using enumerate
import time

print(f'tell which skills you are unfamiliar with')
unfamiliar_skills = str(input('> '))
list_of_unfamiliar_skills = unfamiliar_skills.split()
print(f'filtering  out {unfamiliar_skills}')


'''as all jobs has same class_ find_all returns in list'''
def find_jobs():
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') #this probably get only 1st page as all jobs are paginated

    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date: # we only want latest jobs few days ago
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(" ", '')
            skill_requirements = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            location = job.find('span').get('title')
            #This is another way of getting data we go to header, get h2, get a and ['href'] grabs the link part
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skill_requirements:
                print(f'Company Name : {company_name.strip()}')
                print(f'Skills required : {skill_requirements.strip()}')
                print(f'location: {location}')
                print(f'more info : {more_info}')
                print() #FOr nice space between each


if __name__ == '__main__':
    while True:
        find_jobs()
        wait_time = 10
        print(f'Waiting for {wait_time} minutes..')
        time.sleep(wait_time * 60) #sleeps accepts sec
        # waits for 10 min now