import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def trending(media_type="movie", language=None, genre=None, top_rated=False):
    if top_rated:
        endpoint = f"/{media_type}/top_rated"
    else:
        endpoint = f"/trending/{media_type}/day"

    params = {"api_key": API_KEY}

    if language:
        params["with_original_language"] = language

    if genre:
        params["with_genres"] = genre

    response = requests.get(BASE_URL + endpoint, params=params)
    return response.json()


def search_tmdb(query, media_type="movie"):
    endpoint = f"/search/{media_type}"
    params = {
        "api_key": API_KEY,
        "query": query
    }
    return requests.get(BASE_URL + endpoint, params=params).json()
