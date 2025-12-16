const content = document.getElementById("content");

function loadMovies() {
    fetch("/api/trending/movies")
        .then(res => res.json())
        .then(data => showItems(data.results));
}

function loadTV() {
    fetch("/api/trending/tv")
        .then(res => res.json())
        .then(data => showItems(data.results));
}

function showItems(items) {
    content.innerHTML = "";

    items.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";

        const title = item.title || item.name;
        const img = item.poster_path
            ? `https://image.tmdb.org/t/p/w300${item.poster_path}`
            : "";

        card.innerHTML = `
            <img src="${img}" alt="${title}">
            <h3>${title}</h3>
            <p>⭐ ${item.vote_average}</p>
        `;

        content.appendChild(card);
    });
}
