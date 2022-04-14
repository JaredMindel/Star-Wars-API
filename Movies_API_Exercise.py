from dataclasses import dataclass, field
from datetime import datetime
from numpy import character
import requests
import json


@dataclass
class StarWarsFilm:
    title: str
    director: str
    release_data: str
    actors: list
    plot: str
    rt_score: str = field(metadata = {'units':'percent'})
    box_office_gross: str = field(metadata = {'units': '$'})

@dataclass
class Character:
    name: str
    height: int = field(metadata = {'units':'cm'})
    mass: int = field(metadata = {'units': 'kg'})
    hair_color: str
    eye_color: str
    birth_year: int
    gender: str

@dataclass
class Library:
    list_of_movies: list
    last_updated: datetime

star_wars_database = 'http://www.omdbapi.com/?apikey=58556f28&t='
star_wars_movie_titles = ['Star+Wars+Episode+I', 'Star+Wars+Episode+II', 'Star+Wars+Episode+III', 'Star+Wars', \
    'Star+Wars+Episode+V', 'Star+Wars+Episode+VI', 'Star+Wars+Episode+VII', 'Star+Wars+Episode+VIII', 'Star+Wars+Episode+IX']

def json_reader(website):
    response = requests.get(website)
    json_data = json.loads(response.text)
    return json_data

star_wars_movies = []

for movie in star_wars_movie_titles:
    new_film = star_wars_database + movie
    json_film = json_reader(new_film)
    new_film = StarWarsFilm(json_film['Title'], json_film['Director'], json_film['Released'], json_film['Actors'], 
    json_film['Plot'], json_film['Ratings'][1]['Value'],
    json_film['BoxOffice'])
    star_wars_movies.append(new_film)

star_wars_characters = json_reader('https://swapi.dev/api/people')['results']

print(star_wars_characters[0])

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