class Factor(dict):

    shopping_price = {}
    shopping_count = {}
    factor = {}

    @classmethod
    def get_shopping_price(cls,shopping,price):
        cls.shopping_price = dict(zip(shopping, price))
        return cls.shopping_price

    @classmethod
    def get_shopping_count(cls, shopping, count):
        cls.shopping_count = dict(zip(shopping, count))
        return cls.shopping_count

    
    @classmethod
    def final_factor(cls, shopping, price, count):
        total = 0
        price_list = cls.get_shopping_price(shopping, price)
        count_list = cls.get_shopping_count(shopping, count)
        for item, prices in price_list.items():
            for item2, count in count_list.items():
                if item == item2:
                    cls.factor[item] = prices * count
                    total += prices * count
                    print(f'{item} -> count : {count} , price : {prices} $,total : {prices * count} $') 
                    print(50 * '-')
        print(f' total of all items : {total} $')

    
        
    
# lis = ['a', 'b', 's']
# lia = [1, 2, 3]
# lid = [2, 4, 5]
# Factor.get_shopping_price(lis, lia)
# Factor.get_shopping_count(lis, lid)
# print(Factor.shopping_price)
# print(Factor.shopping_count)
# Factor.final_factor(lis, lia, lid )
# print(Factor.factor)
