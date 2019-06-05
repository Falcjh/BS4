from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
import os

folder = input('Where are your movies stored? \n')
list_movies = os.listdir(folder)

for movie in list_movies:
    # Collecting URL from the search page
    search_url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all'

    page = requests.get(search_url)
    # Get raw data from URL
    soup = BeautifulSoup(page.text, 'html.parser')
    # Search for movie id so we can get the link to the movie detail page
    # look for a
    search = soup.find('table')
    table = search.find_all('a', limit=1)
    # extract the movie id from the href and store it in a list to use it later.
    for link in table:
        movie_id = (link.get('href'))
        print(f'{movie} has following id link: {movie_id}')
    # put the script to sleep so it looks more human
        for z in range(1):
            print("reading webpage")
            sleep(randint(1, 4))
    # make another request to the movie info page
        movie_url = 'https://www.imdb.com' + movie_id + '?ref_=fn_al_tt_1'
        page2 = requests.get(movie_url)
    # search name and genre of the movie
        soup2 = BeautifulSoup(page2.text, 'html.parser')
        search_name = soup2.find('div', class_='title_wrapper')
        movie_title = search_name.h1.text
        search_genre = soup2.find('div', class_='subtext')
        movie_genre = search_genre.a.text

        print(f'{movie_title} has following genre: {movie_genre}')

    for z in range(1):
        print("Searching next movie in list")
        sleep(randint(1, 3))

print('All movies have been renamed and filed')
