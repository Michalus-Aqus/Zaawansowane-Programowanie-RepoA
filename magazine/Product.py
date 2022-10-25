import magazine.utils

class Product:
    def __init__(self,item):
        self.item=item
    def __str__(self):
        return magazine.utils.obj2str("Product",self.item)
