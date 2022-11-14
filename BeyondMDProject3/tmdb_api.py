import os
import requests
import random
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def get_movie_info():
    """
    the landing page of the app will call this function and make an API call to the movie database
    the movie database will send back a JSON containing trending movies of the day
    each movie contains information scuh as movie title, poster file name, release date, and more
    """
    movie_request_url = (
        "https://api.themoviedb.org/3/trending/movie/day?api_key=" + os.getenv("TMDB_KEY")
    )

    movie_response = requests.get(movie_request_url)
    movie_response_json = movie_response.json()
    movies = movie_response_json['results']

    movie_title = []
    poster_path = []
    release_date = []

    for movie in movies:
        movie_title.append(movie["original_title"])
        poster_path.append(get_movie_poster(movie["poster_path"]))
        release_date.append(movie["release_date"])

    info = zip(movie_title, poster_path, release_date)
    
    return random.choice(list(info))

def get_movie_poster(poster_file_name):
    """
    the poster information on the movie only contains the file name
    to display the image we need the full path of the image and not just the file name
    while it's possible to just build a simple string to get the URL I don't think that's a good idea
    """
    poster_request_url = (
        "https://api.themoviedb.org/3/configuration?api_key=" + os.getenv("TMDB_KEY")
    )

    poster_response = requests.get(poster_request_url)
    poster_response_json = poster_response.json()
    poster_response_json = poster_response_json["images"]

    base_url = poster_response_json["secure_base_url"]
    poster_size = poster_response_json["poster_sizes"][4]

    return base_url + poster_size + poster_file_name