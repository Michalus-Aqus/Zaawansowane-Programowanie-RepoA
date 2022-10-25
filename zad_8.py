def raf_load(page: str):
    import requests
    return requests.get(page).json()


class Brewery:
    new_id: int = 0

    def __init__(self, name, location, type):
        self.name: str = name
        self.location: dict = location
        self.type: str = type
        self.id = Brewery.new_id
        Brewery.new_id += 1

    def print(self):
        print("Brewery ", self.id, "(", self.name, ",", self.location, ",", self.type, ")")


def load():
    # breweries_json=raf_load('https://api.openbrewerydb.org/breweries')
    breweries_json = raf_load('https://api.openbrewerydb.org/breweries/random?size=20')
    res = []
    for b in breweries_json:
        name = b['name']
        location = {"state": b['state'], "city=": b['city'], "street": b['street']}
        type = b['brewery_type']

        brewery_obj = Brewery(name, location, type)
        res.append(brewery_obj)
    return res


def load_by_city(city):
    print("CITY=", city)
    page = 'https://api.openbrewerydb.org/breweries?by_city=' + city.replace(" ", "")
    print(page)
    breweries_json = raf_load(page)
    res = []
    for b in breweries_json:
        name = b['name']
        location = {"state": b['state'], "city=": b['city'], "street": b['street']}
        type = b['brewery_type']

        brewery_obj = Brewery(name, location, type)
        res.append(brewery_obj)
    return res


def main(city: str):
    breweries = []
    if city == "":
        print("-city pram not passed")
        breweries = load()
    else:
        breweries = load_by_city(city)
    for b in breweries:
        b.print()


import sys

if __name__ == "__main__":
    city = ""
    for i in range(len(sys.argv)):
        print("param=", sys.argv[i])
        if sys.argv[i] == "-city":
            if i + 1 in range(len(sys.argv)):
                city = sys.argv[i + 1]
    main(city)
