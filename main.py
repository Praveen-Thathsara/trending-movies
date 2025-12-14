from fastapi import FastAPI
from services.tmdb import get_trending_movies, get_trending_tv

app = FastAPI(title="Trending Movies & TV API")

@app.get("/")
def home():
    return {"message": "Trending API is running 🚀"}

@app.get("/trending/movies")
def trending_movies():
    return get_trending_movies()

@app.get("/trending/tv")
def trending_tv():
    return get_trending_tv()
