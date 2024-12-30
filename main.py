from fastapi import FastAPI
import random

app = FastAPI()

# Hardcoded movie data
movies = {
    "action": ["Mad Max: Fury Road","Die Hard","John Wick","The Dark Knight","Inception","The Matrix","Gladiator","The Lord of the Rings: The Two Towers","The Lord of the Rings: The Return of the King","Avengers: Endgame","The Avengers","Spider-Man: Into the Spider-Verse","Raiders of the Lost Ark","The Bourne Ultimatum","Terminator 2: Judgment Day","Logan","Casino Royale","Skyfall","Guardians of the Galaxy","Black Panther","Doctor Strange","Captain America: The Winter Soldier","Captain America: Civil War","Avengers: Infinity War","Iron Man","Thor: Ragnarok","Wonder Woman","Mission: Impossible - Fallout","Mission: Impossible - Rogue Nation","Mission: Impossible - Ghost Protocol","Top Gun: Maverick","Dunkirk","The Batman","The Incredibles","The Incredibles 2","Spider-Man: No Way Home","Spider-Man 2","Batman Begins","The Prestige","Interstellar","Edge of Tomorrow","Warrior","Kill Bill: Vol. 1","Kill Bill: Vol. 2","Aliens","Star Wars: Episode IV - A New Hope","Star Wars: Episode V - The Empire Strikes Back","Star Wars: Episode VI - Return of the Jedi","Rogue One: A Star Wars Story","The Force Awakens","Pacific Rim","300","Sin City","Deadpool","Deadpool 2","The Wolverine","X-Men: Days of Future Past","X2: X-Men United","The Lego Batman Movie","Shazam!","Aquaman","The Hunger Games","The Hunger Games: Catching Fire","The Hunger Games: Mockingjay - Part 1","The Hunger Games: Mockingjay - Part 2","The Raid: Redemption","The Raid 2","13 Assassins","Hero","House of Flying Daggers","Crouching Tiger, Hidden Dragon","Seven Samurai","Heat","Léon: The Professional","Oldboy","Hard Boiled","Fury","1917","Platoon","Apocalypse Now","Saving Private Ryan","Full Metal Jacket","Django Unchained","Once Upon a Time in Hollywood","Pulp Fiction","Reservoir Dogs","The Hateful Eight","The Revenant","The Equalizer","The Equalizer 2","Taken","Taken 2","Taken 3","True Lies","The Fugitive","Speed","Heat","Collateral","Warrior","The Book of Eli"],
    "comedy": ["Superbad", "Step Brothers", "The Big Lebowski"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
    "sci-fi": ["Interstellar", "The Matrix", "Blade Runner 2049"]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}

@app.get("/recommendations/")
def get_recommendations(genre: str):
    # Return 3 random movies for the requested genre
    if genre.lower() in movies:
        selected_movies = random.sample(movies[genre.lower()], 3)  # Select 3 random movies
        return {"genre": genre, "recommendations": selected_movies}
    else:
        return {"error": "Genre not found. Try 'action', 'comedy', 'drama', or 'sci-fi'."}
