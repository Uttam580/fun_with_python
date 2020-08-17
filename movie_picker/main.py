import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie
print('import successfull')

# imdb url
URL = 'https://www.imdb.com/chart/top'


def main():
    response = requests.get(URL)
    html = response.text  # getting raw html
    soup = BeautifulSoup(html,'html.parser')# beautify the html
    movie_tags = soup.select('td.titleColumn')# getting movie name with tags titleColumn
    innermovie_tags = soup.select('td.titleColumn a') # getting a tag from titlecolumn , it contains actor /movie name 
    rating_tags = soup.select('td.posterColumn span[name=ir]')# contains rating fot movie

    # function to get year from titlecolumn tag
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    # list containing years , actor_name , titles and rating 
    years = [get_year(tag) for tag in movie_tags]
    actors_list = [tag['title'] for tag in innermovie_tags]
    titles = [tag.text for tag in innermovie_tags]
    ratings  = [float(tag['data-value']) for tag in rating_tags]
    n_movies = len(titles)
    #print(n_movies)we have 250 movies

    while(True):
        # generating random number between  0 to total number of movie
        idx = random.randrange(0, n_movies)
        # display movie name(idx from randomly generated movie) on screen  
        print(f'Movie : {titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')
        #asking for user to continue
        user_input = input('Do you want another movie (y/[n])? ')
        #
        if user_input != 'y':
            break

if __name__ == "__main__":
    main()
    