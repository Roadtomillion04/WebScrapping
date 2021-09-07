from bs4 import BeautifulSoup
import requests
import pprint
import sys

pages = int(sys.argv[1])


for num in range(pages):                                    #because page should not be 0
    res = requests.get(f'https://news.ycombinator.com/news?p={num+1}').text

    soup = BeautifulSoup(res, 'lxml')

    #select returns in list
    story_link = soup.select('.storylink')
    subtext = soup.select('.subtext') #class subtext has scores class


    def get_hacker_news(links:list, subtext:list):
        hn:list = []
                      #enumerate gives index as well every end of loop idx increases by 1
        for idx, news in enumerate(links):
            title = story_link[idx].getText()
            href = story_link[idx]['href']

            points = subtext[idx].select('.score')

            if len(points): # Sometimes the new post may not have points it will throw list out of range error
                            #points[0] because select returns in list
                votes = int(points[0].getText().replace(' points', ''))

                if votes > 99: # to get only popular news!
                    hn.append({'title' : title, 'link' : href, 'points' : votes})

        return sorted(hn, key = lambda x : x['points'], reverse=True)

    #prettyprint prints in nicer way
    pprint.pprint(get_hacker_news(story_link, subtext))
