class Movie:
    def __init__(self, data):
        self.movieId = data["movieId"]
        self.title = data["title"]
        self.genres = data["genres"]

    def __dict__(self):
        return {"movieId": self.movieId, "title": self.title, "genres": self.genres, "OK": True}
