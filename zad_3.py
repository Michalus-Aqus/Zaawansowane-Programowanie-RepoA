class Property:
    
    def __init__(self,area,rooms,price,address):
        self.area:float = area
        self.rooms:int = rooms
        self.price:float = price
        self.address:str = address
        
    def __str__(self):
        text = ""
        text += "Property("
        text += "area = " + str(self.area) + ";"
        text += "rooms = " + str(self.rooms) + ";"
        text += "price = " + str(self.price) + ";"
        text += "address = " + str(self.address)# + ";"
        text += ")"
        return text
        
class House(Property):
    
    def __init__(self,area,rooms,price,address,plot):
        super().__init__(area,rooms,price,address)
        self.plot:int=plot

    def __str__(self):
        text = ""
        text += "House("
        text += "area = " + str(self.area) + ";"
        text += "rooms = " + str(self.rooms) + ";"
        text += "price = " + str(self.price) + ";"
        text += "address = " + str(self.address) + ";"
        text += "plot = " + str(self.plot)# + ";"
        text += ")"
        return text


class Flat(Property):
    
    def __init__(self,area,rooms,price,address,floor):
        super().__init__(area,rooms,price,address)
        self.floor:int=floor
        
    def __str__(self):
        text = ""
        text += "Flat("
        text += "area = " + str(self.area) + ";"
        text += "rooms = " + str(self.rooms) + ";"
        text += "price = " + str(self.price) + ";"
        text += "address = " + str(self.address) + ";"
        text += "floor = " + str(self.floor)# + ";"
        text += ")"
        return text

    
def main():
    properties = []
    properties += [House(1000,6,2000000,"Zakopane ul.Spokojna 6",1600)]
    properties += [Flat(1000,6,100000,"Zakopane ul.Spokojna 18/3",800)]
    for p in properties:
        print(p)

if __name__ == "__main__":
    main()
