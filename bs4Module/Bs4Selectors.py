from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news').text

soup = BeautifulSoup(res, 'lxml')
#print(soup.prettify())
print(soup.title.text)
#print(soup.body.text)

'''selectors - refer css but works same as find all and returns in list'''
#print(soup.select('.votelinks')) . is class

story_title = soup.select('.storylink')[0].text
story_link = soup.select('.storylink')[0]['href'] #href grabs the link part
votes = soup.select('.score')[0]
print(story_title, story_link, votes)

# you can get specific value
print(votes.get('id'))