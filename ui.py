import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.set_page_config(page_title="Trending Movies & TV", layout="wide")

st.title("🎬 Trending Movies & TV Explorer")

media = st.selectbox("Select Media Type", ["movie", "tv"])
language = st.text_input("Language code (en, hi, ja)", "")
top_rated = st.checkbox("Top Rated Only")

query = st.text_input("🔍 Search")

if st.button("Fetch Results"):
    if query:
        res = requests.get(f"{API_URL}/search", params={
            "query": query,
            "media_type": media
        })
    else:
        res = requests.get(f"{API_URL}/trending", params={
            "media_type": media,
            "language": language if language else None,
            "top_rated": top_rated
        })

    data = res.json()

    if "results" in data:
        cols = st.columns(5)
        for i, item in enumerate(data["results"][:20]):
            with cols[i % 5]:
                title = item.get("title") or item.get("name")
                poster = item.get("poster_path")
                rating = item.get("vote_average")

                if poster:
                    st.image(f"https://image.tmdb.org/t/p/w300{poster}")
                st.caption(f"⭐ {rating}")
                st.text(title)
