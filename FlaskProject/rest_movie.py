class Movie:
    def __init__(self, data):
        self.movieId = data[0]
        self.title = data[1]
        self.genre = data[2]

    def __dict__(self):
        return {"movieId": self.movieId,
                "title": self.title,
                "genre": self.genre,
                }


def parse(csv: str):
    obj = []
    for line in csv.split('\n')[1:]:
        if len(line.split(',')) >= 3:
            obj += [Movie(line.split(','))]
    res = []
    for o in obj:
        res += [o.__dict__()]

    return res


class Server:
    def __init__(self, csv):
        self.csv = csv
        self.obj = parse(csv)

    def endpoint(self):
        return "<p>" + str(self.obj) + "</p>"
