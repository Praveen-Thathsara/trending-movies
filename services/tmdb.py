import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_trending_movies():
    url = f"{BASE_URL}/trending/movie/day"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def get_trending_tv():
    url = f"{BASE_URL}/trending/tv/day"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    return response.json()
