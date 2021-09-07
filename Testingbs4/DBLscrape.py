from bs4 import BeautifulSoup
import requests

'''its complicated maybe ill solve it future'''

data = requests.get('https://gamepress.gg/dblegends/tier-list').text

soup = BeautifulSoup(data, 'lxml')
tiers = soup.find_all('div', class_ = "gp-tier-container clearfix gp-tier-container-2-col-desktop gp-tier-container-2-col-mobile dbl-stats-tier-container")

def show_tier_list():
    for idx, character in enumerate(tiers):

        chars = character.find('div', class_ = 'tier-list-cell-row')#.get('data-title')
        chars.data_position = '2'
        print(chars.get('data-title'))

show_tier_list()