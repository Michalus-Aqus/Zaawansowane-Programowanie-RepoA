from flask import Flask
import csv
from MovieApp.Movie import Movie

FILE_LINKS = open("data/links.csv", "r", encoding="utf-8").read()
FILE_MOVIES = open("data/movies.csv", "r", encoding="utf-8").read()
FILE_TAGS = open("data/tags.csv", "r", encoding="utf-8").read()
FILE_RATINGS = open("data/ratings.csv", "r", encoding="utf-8").read()

app = Flask(__name__)


@app.route("/links")
def get_links():
    r = csv.DictReader(FILE_LINKS.split('\n'), delimiter=',')
    return str([obj for obj in r])


@app.route("/movies")
def get_movies():
    r = csv.DictReader(FILE_MOVIES.split('\n'), delimiter=',')
    Movies = [Movie(movie_dictionary) for movie_dictionary in r]
    return str([m.__dict__() for m in Movies])


@app.route("/tags")
def get_tags():
    r = csv.DictReader(FILE_TAGS.split('\n'), delimiter=',')
    return str([obj for obj in r])


@app.route("/ratings")
def get_ratings():
    r = csv.DictReader(FILE_RATINGS.split('\n'), delimiter=',')
    return str([obj for obj in r])
