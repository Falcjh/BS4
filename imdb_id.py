from bs4 import BeautifulSoup
import requests


class imdb_id:

    # Collecting URL from the search page
    movie = movie_name
    url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all'
    movie_id = []

    page = requests.get(url)

    # Get raw data from URL
    soup = BeautifulSoup(page.text, 'html.parser')

    # Search for movie id so we can get the link to the movie detail page
    # look for a
    search = soup.find('table')
    table = search.find_all('a', limit=1)

    # extract the movie id from the href and store it in a list to use it later.

    for link in table:
        movie_id.append(link.get('href'))
