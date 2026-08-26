
# 🎬 Trending Movies & TV Explorer

A movie and TV discovery application built with **Python, FastAPI, Streamlit, and the TMDB API**.

The application allows users to explore trending and top-rated movies and TV shows, search for titles, filter content by language, and retrieve movie and TV information through a REST API.

This project was developed as a learning and portfolio project to practice **Python backend development, REST APIs, API integration, environment configuration, and interactive web interfaces**.

---

## ✨ Features

### 1. Trending Movies & TV Shows
- Browse trending movies and TV shows.
- Switch between movie and TV content.
- Retrieve current content from the TMDB API.
- Display titles, posters, ratings, and other available information.

### 2. Movie & TV Search
- Search for movies by title.
- Search for TV shows by title.
- Retrieve search results directly from the TMDB API.

### 3. Top-Rated Content
- Explore highly rated movies.
- Explore highly rated TV shows.
- Display ratings alongside the retrieved content.

### 4. Language Filtering
- Filter content based on the original language.
- Support language-based movie and TV discovery.

### 5. FastAPI REST API
- Backend API developed using FastAPI.
- Provides endpoints for trending content and search.
- Automatically generated interactive API documentation.
- Uses Uvicorn as the ASGI development server.

### 6. Streamlit User Interface
- Interactive web interface built with Streamlit.
- Allows users to select content types.
- Provides search and filtering controls.
- Displays movie and TV results in an easy-to-use interface.

### 7. TMDB API Integration
- Retrieves movie and TV information from TMDB.
- Uses a dedicated service module for TMDB API requests.
- API credentials are managed through environment variables.

### 8. Environment-Based Configuration
- API credentials are stored outside the source code.
- `.env` is used for local configuration.
- Sensitive environment files are excluded from Git.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| FastAPI | REST API backend |
| Uvicorn | ASGI server |
| Streamlit | Interactive web interface |
| Requests | HTTP requests |
| python-dotenv | Environment variable management |
| TMDB API | Movie and TV data |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📋 Prerequisites

Before running the project, make sure you have the following installed:
- **Python 3.10 or newer**
- **Git**
- **pip**
- A **TMDB API key**

Check your Python version with:
```bash
python --version

```

Check Git with:

```bash
git --version

```

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/Praveen-Thathsara/trending-movies.git](https://github.com/Praveen-Thathsara/trending-movies.git)
cd trending-movies

```

### 2. Create a Virtual Environment

Using a virtual environment is recommended to keep project dependencies isolated.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt

```

### 4. Configure the TMDB API

Create a file named `.env` in the root directory of the project.
Add your TMDB API key:

```env
TMDB_API_KEY=your_tmdb_api_key

```

> **🔐 Security Warning:** Never upload your `.env` file or virtual environment folder (`venv/`) to GitHub! Ensure they are included in your `.gitignore`.

---

## ▶️ Running the Application

This project requires both the FastAPI backend and Streamlit interface to run concurrently.

```text
                    TMDB API
                       ▲
                       │ API Requests
              ┌────────┴────────┐
              │  FastAPI Backend │
              │     main.py      │
              └────────┬────────┘
                       │ HTTP Requests
              ┌────────┴────────┐
              │  Streamlit UI    │
              │      ui.py       │
              └─────────────────┘

```

### Step 1: Start the FastAPI Backend

Open your first terminal, ensure your virtual environment is activated, and run:

```bash
uvicorn main:app --reload

```

* The backend will run at: `http://127.0.0.1:8000`
* Interactive API documentation (Swagger UI) is available at: `http://127.0.0.1:8000/docs`

### Step 2: Start the Streamlit Interface

Open a second terminal, activate your virtual environment, and run:

```bash
streamlit run ui.py

```

* The Streamlit application will open in your browser at: `http://localhost:8501`

---

## 🔌 API Endpoints

The FastAPI backend provides the following core endpoints:

* **Trending Content:** `GET /api/trending`
* **Trending Movies:** `GET /api/trending?media_type=movie`
* **Trending TV Shows:** `GET /api/trending?media_type=tv`
* **Top-Rated Movies:** `GET /api/trending?media_type=movie&top_rated=true`
* **Top-Rated TV Shows:** `GET /api/trending?media_type=tv&top_rated=true`
* **Search Movies:** `GET /api/search?query=avatar&media_type=movie`
* **Search TV Shows:** `GET /api/search?query=breaking%20bad&media_type=tv`

---

## 🏗️ Project Structure

```text
trending-movies/
│
├── services/
│   └── tmdb.py
│
├── static/
│   ├── script.js
│   └── styles.css
│
├── templates/
│   └── index.html
│
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
└── ui.py

```

---

## 🐛 Troubleshooting

### `ModuleNotFoundError`

Make sure your virtual environment is activated and dependencies are installed:

```bash
venv\Scripts\activate  # Windows
pip install -r requirements.txt

```

### TMDB API Key Error

Verify that your `.env` file is placed in the project root directory, uses the exact variable name `TMDB_API_KEY`, and contains a valid API key.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## 📄 License

This project is created for educational and portfolio purposes.

---

## 👨‍💻 Author

**Praveen Thathsara**

*Software Developer | Full-Stack Development | AWS & DevOps*

* GitHub: [Praveen-Thathsara](https://github.com/Praveen-Thathsara)
* Portfolio: [praveenr.live](https://praveenr.live)

---

*Movie and TV data is provided by The Movie Database (TMDB). This project is not endorsed or certified by TMDB.*

```

```
