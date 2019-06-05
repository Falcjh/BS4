from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint


# Collecting URL from the search page
movie = "the hulk"
search_url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all'


name = ''
year = ''
genre = ''

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
    print(movie_id)
# put the script to sleep so it looks more human
    for z in range(0, 3):
        print("acting human")
        sleep(randint(1, 4))
# make another request to the movie info page
    movie_url = 'https://www.imdb.com' + movie_id + '?ref_=fn_al_tt_1'
    page2 = requests.get(movie_url)

    soup2 = BeautifulSoup(page2.text, 'html.parser')
    search_name = soup2.find('div', class_='title_wrapper')

    print(search_name)
