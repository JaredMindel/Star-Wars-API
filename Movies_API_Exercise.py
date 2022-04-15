from dataclasses import dataclass, field
from datetime import datetime
import requests
import json
import datetime

def json_reader(website):
    response = requests.get(website)
    json_data = json.loads(response.text)
    return json_data

@dataclass
class StarWarsFilm:
    title: str
    episode: int
    opening_crawl: str
    director: str
    release_date: str
    actors: list
    plot: str
    rt_score: str
    box_office_gross: str

    def __init__(self, title, episode, opening_crawl, director, release_date, actors, plot, rt_score, box_office_gross):
        self._title = title
        self._episode = episode
        self._opening_crawl = opening_crawl
        self._director = director
        self._release_date = release_date
        self._actors = actors
        self._plot = plot
        self._rt_score = rt_score
        self._box_office_gross = box_office_gross

    def __repr__(self):
        return 'StarWarsFilm(%s, %i, %s, %s, %s, %s, %s, %s, %s)' % (self._title, self._episode, self._opening_crawl, self._director, 
        self._release_date, self._actors, self._plot, self._rt_score, self._box_office_gross)

    def __gt__(self, other):
        print('__gt__ called - self: %s, other: %s' % (self, other))
        if self._episode > other._episode:
            return True
        else:
            return False
    
    def __eq__(self, other):
        print('__eq__ called - self: %s, other: %s' % (self, other))
        if self._episode == other._episode:
            return True
        else:
            return False
    
    def __ge__(self, other):
        print('__ge__ called - self: %s, other: %s' % (self, other))
        if self._episode == other._episode:
            return True
        else:
            return False

@dataclass
class Character:
    name: str
    height: int = field(metadata = {'units':'cm'})
    mass: int = field(metadata = {'units': 'kg'})
    hair_color: str
    eye_color: str
    birth_year: int
    gender: str

    def __str__(self):
        return f'character name: {self.name}, {self.height}, {self.mass}, {self.hair_color}, {self.eye_color}, {self.birth_year}, {self.gender}'

character_list = []

@dataclass
class Library:
    list_of_movies: list
    last_updated: datetime
    OMDb_site: str = 'http://www.omdbapi.com/?i=tt3896198&apikey=58556f28&t=Star+Wars'
    swapi_people: str = 'https://swapi.dev/api/people/'
    swapi_films: str = 'https://swapi.dev/api/films'
    movie_dictionary: dict = {}
    last_updated = datetime.datetime.now()
    
    def get_characters(self):
        api_call = json_reader((self.swapi_people['results]']).text)
        character_list.append(api_call)

    def get_movies(self):
        return self.movie_dictionary


star_wars_database = 'http://www.omdbapi.com/?apikey=58556f28&t='
star_wars_movie_titles = ['Star+Wars+Episode+I', 'Star+Wars+Episode+II', 'Star+Wars+Episode+III', 'Star+Wars', \
    'Star+Wars+Episode+V', 'Star+Wars+Episode+VI', 'Star+Wars+Episode+VII', 'Star+Wars+Episode+VIII', 'Star+Wars+Episode+IX']

star_wars_movies = []

ep_num = 1

for movie in star_wars_movie_titles:
    new_film = star_wars_database + movie
    json_film = json_reader(new_film)
    new_film = StarWarsFilm(json_film['Title'], ep_num, None, json_film['Director'], json_film['Released'], json_film['Actors'], 
    json_film['Plot'], json_film['Ratings'][1]['Value'],
    json_film['BoxOffice'])
    star_wars_movies.append(new_film)
    ep_num += 1

star_wars_characters = json_reader('https://swapi.dev/api/people')['results']

character_list = []

for x in range(len(star_wars_characters)):
    new_character = star_wars_characters[x]
    new_character = Character(new_character['name'],
    int(new_character['height']),
    int(new_character['mass']),
    new_character['hair_color'],
    new_character['eye_color'],
    new_character['birth_year'],
    new_character['gender'])
    character_list.append(new_character)

print(character_list)
print(character_list[1])