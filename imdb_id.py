from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint


# Collecting URL from the search page
movie = "fc de kampioenen"
search_url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all'

movie_id = []

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
    movie_id.append(link.get('href'))
    print(movie_id)
# put the script to sleep so it looks more human
    for z in range(0, 3):
        print("acting human")
        sleep(randint(1, 4))
# make another request to the movie info page
