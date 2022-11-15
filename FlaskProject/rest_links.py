Genralized_fields = []


class Genralized:
    def __init__(self, data: list):
        self.d = {}
        for f in Genralized_fields:
            self.d[f] = data.pop(0)

    def __dict__(self):
        return self.d


def parse(csv: str):
    obj = []
    Genralized_fields = csv.split('\n')[0].split(',')
    print(Genralized_fields)
    for line in csv.split('\n')[1:]:
        if len(line.split(',')) >= 3:
            obj += [Genralized(line.split(','))]
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
