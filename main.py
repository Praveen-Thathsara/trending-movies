from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services.tmdb import get_trending_movies, get_trending_tv

app = FastAPI(title="Trending Movies & TV")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/trending/movies")
def trending_movies():
    return get_trending_movies()

@app.get("/api/trending/tv")
def trending_tv():
    return get_trending_tv()
