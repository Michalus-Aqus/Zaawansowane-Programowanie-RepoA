# Use "python -m flask run" to run server
from flask import Flask
import gunicorn
from FlaskProject.rest_movie import Server as Movies
from FlaskProject.rest_links import Server as Links
from FlaskProject.rest_tags import Server as Tags
from FlaskProject.rest_ratings import Server as Ratings

FILE_LINKS = open("data/links.csv", "r", encoding="utf-8").read()
FILE_MOVIES = open("data/movies.csv", "r", encoding="utf-8").read()
FILE_RATINGS = open("data/ratings.csv", "r", encoding="utf-8").read()
FILE_TAGS = open("data/tags.csv", "r", encoding="utf-8").read()

SERVER_MOVIE = Movies(FILE_MOVIES)
SERVER_LINK = Links(FILE_LINKS)
SERVER_TAGS = Tags(FILE_TAGS)
SERVER_RATINGS = Ratings(FILE_RATINGS)

app = Flask(__name__)


@app.route("/<ServerName>/")
def movie(ServerName):
    if ServerName == "movie":
        return SERVER_MOVIE.endpoint()
    elif ServerName == "link":
        return SERVER_LINK.endpoint()
    elif ServerName == "tags":
        return SERVER_TAGS.endpoint()
    elif ServerName == "ratings":
        return SERVER_RATINGS.endpoint()
    else:
        return ""
