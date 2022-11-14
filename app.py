from flask import Flask
import csv

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
    return str([obj for obj in r])


@app.route("/tags")
def get_links():
    r = csv.DictReader(FILE_TAGS.split('\n'), delimiter=',')
    return str([obj for obj in r])


@app.route("/ratings")
def get_links():
    r = csv.DictReader(FILE_RATINGS.split('\n'), delimiter=',')
    return str([obj for obj in r])
