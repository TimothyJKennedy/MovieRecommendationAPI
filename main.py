from fastapi import FastAPI

app = FastAPI()

# Hardcoded movie data
movies = {
    "action": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
    "comedy": ["Superbad", "Step Brothers", "The Big Lebowski"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
    "sci-fi": ["Interstellar", "The Matrix", "Blade Runner 2049"]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}

@app.get("/recommendations/")
def get_recommendations(genre: str):
    # Return movies for the requested genre
    if genre.lower() in movies:
        return {"genre": genre, "recommendations": movies[genre.lower()]}
    else:
        return {"error": "Genre not found. Try 'action', 'comedy', 'drama', or 'sci-fi'."}
