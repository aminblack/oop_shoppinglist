
class Product(dict):
    product_list = {}

    def __init__(self, name:str, quantity: int, price: int, dimension: str)-> None:
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dimension = dimension
        Product.product_list["quantity"] = quantity
        Product.product_list["price"] = price
        Product.product_list["dimension"] = dimension


    def increase_quantity(self, value):
        self.product["quantity"] += value

    def increase_price(self, value):
        self.product_list["price"] += value

    def decrease__quantity(self, value):
        self.product_list["quantity"] -= value

    def decrease__price(self, value):
        self.product_list["price"] -= value





class Fruits(Product):


    def __str__(self):
        return self.name

    def __repr__(self):
        return {f'{self.__class__.__name__}({self.name},{self.quantity},{self.price},{self.dimension})'}

class Liquate(Product):

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name},{self.quantity},{self.price},{self.dimension})'


# moz = Fruits('moz', 20, 10, 'kg')
# # water = Liquate('water', 20, 10, 'but')
# print(moz.product_list)
# d = {}
# d['moz'] = moz.product_list
# print(d)


