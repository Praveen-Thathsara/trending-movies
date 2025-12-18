from fastapi import FastAPI
from services.tmdb import trending, search_tmdb

app = FastAPI(title="Movie & TV Explorer API")


@app.get("/api/trending")
def get_trending(
    media_type: str = "movie",
    language: str | None = None,
    genre: int | None = None,
    top_rated: bool = False
):
    return trending(media_type, language, genre, top_rated)


@app.get("/api/search")
def search(query: str, media_type: str = "movie"):
    return search_tmdb(query, media_type)
