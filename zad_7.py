def raf_load(page:str):
    #import urllib.request
    #with urllib.request.urlopen(page) as response:
    #    html = response.read()
    #    return ht
    import requests
    return requests.get(page).json()

class Brewery:
    name:str=""
    location:dict=""
    type:str=""
    def __init__(self,n,l,t):
        self.name=n
        self.location=l
        self.type=t

def load():
    breweries=raf_load('https://api.openbrewerydb.org/breweries')
    for b in breweries:
        print("name=", b['name'])
        print("state=",b['state'],"city=", b['city'],"street=",b['street'])
        print("type=", b['brewery_type'])
        obj=Brewery.new(b['name'],{b['name']},b['brewery_type'])

load()
