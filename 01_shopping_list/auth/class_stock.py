from pprint import pprint
import json
class Stock(dict):
    stock = {}

    @staticmethod
    def read_stock():
        with open('stuck.json', 'r') as sj:
            Stock.stock = json.load(sj)
        return Stock.stock

    @classmethod
    def search_stock(cls,value):
        search = cls.read_stock()
        existent = False
        for key in search.keys():
            if key == value:
                existent = True
        return existent

    @classmethod
    def price_supply(cls, value):
        search = cls.read_stock()
        for key,vlu in search.items():
            if key == value:
                for key2,vlu2 in vlu.items():
                    if key2 == "price":
                        return vlu2





