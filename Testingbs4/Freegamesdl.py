from bs4 import BeautifulSoup
import requests
import sys

pages = int(sys.argv[1])
print('''
press 1 for new games
2 for search
3 for popular games
''')
user_input = int(input('press: '))
print(user_input)

genre = str(input('Enter genre: ')) # for user input 2 i don't want to ask again in loop


def show_games(res):
    soup = BeautifulSoup(res, 'lxml')

    game_contents = soup.select('.geekmag-xl-article-right')

    for idx, games in enumerate(game_contents):
        game_name = games.find('h3').a.text
        game_link = games.find('h3').a['href']
        game_desc = games.find('p').text

        print(f'{idx}. Game_name : {game_name}')
        print(f'Game_desc : {game_desc}')
        print(f'Game_link : {game_link}')
        print()


def show_popular_games(res):
    soup = BeautifulSoup(res, 'lxml')

    popular_games = soup.find_all('li', style = 'overflow:hidden')

    for idx, games in enumerate(popular_games):
        game_name = games.find('a').getText()
        game_link = games.find('a')['href']
        game_views = games.getText() # this gets game name and views

        print(f'{idx}. Game_name : {game_name}')
        print(f'Game_link : {game_link}')
        print(f'Game_views : {game_views}')


for pageNum in range(pages):
    try:                                                        # should not be 0
        if user_input == 1:
            res = requests.get(f'https://www.freegamesdl.net/page/{pageNum+1}/').text
            show_games(res)

        if user_input == 2:
                print(genre)
                res = requests.get(f'https://www.freegamesdl.net/cat/{genre}/page/{pageNum+1}/').text
                show_games(res)

        if user_input == 3:
            res = requests.get(f'https://www.freegamesdl.net/').text
            show_popular_games(res)

    except:
        print('typoo!!')
