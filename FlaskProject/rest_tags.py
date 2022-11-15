class Server:
    def __init__(self, csv):
        self.csv = csv

    def endpoint(self):
        return "<p>" + self.csv + "</p>"
