import magazine.utils

class Order:
    def __init__(self,item):
        self.item=item
    def __str__(self):
        return magazine.utils.obj2str("Order",self.item)
