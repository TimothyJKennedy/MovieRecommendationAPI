### MovieRecommendationAPI
API that recommends movies based on user input genre (Action, Drama, Comedy or Sci-fi)

Timothy's Movie Recommendation API - README

This README file explains how to set up and run the Movies API, which provides endpoints to fetch movie titles by genre from a hardcoded list of 100 films for each genre to simplify setup.

### Prerequisites:
Before running this API, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

### Setup Instructions

## Clone the Repository:
- git clone <repository-url>
- cd <repository-folder>

## Create a Virtual Environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

## Install Dependencies:
- Install the required Python packages listed in requirements.txt:

- pip install -r requirements.txt

Run the API Server:

Use the following command to start the Flask server:

python app.py

The server will start at http://127.0.0.1:5000 by default.

API Endpoints

1. Get Movies by Genre

Endpoint: /movies/<genre>

Method: GET

Description: Fetches a list of movie titles for a specific genre.

Example Request:

GET http://127.0.0.1:5000/movies/Action

Example Response:

["Mad Max: Fury Road", "Die Hard"]

Testing

Use a tool like Postman or cURL to test the endpoints.

Example cURL request:

curl http://127.0.0.1:5000/movies/Action

Notes

Add additional genres and movies to the hardcoded movies by genre as needed or create a database using something like sqlite3 to manage the data better.

Make sure to keep movies.db in the same directory as app.py.

Feel free to reach out if you encounter issues or have questions!

